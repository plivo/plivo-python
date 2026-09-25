# -*- coding: utf-8 -*-
"""
Auto-pagination tests for PlivoResourceInterface.__iter__.

The Call and Recording list endpoints are moving to cursor (keyset)
pagination behind two deployment-wide switches, so at any given moment a
deployment is serving one of three shapes:

  OFFSET  (legacy)  offset applied; meta.next -> '?limit=20&offset=20'
  HYBRID            offset applied; meta.next -> '?limit=20&cursor=<token>'
  CURSOR            offset IGNORED (page 1 returned instead, HTTP 200);
                    meta.next -> '?limit=20&cursor=<token>'

meta.total_count is already absent from these responses. Cursors are
opaque and limit still caps at 20.

These tests never touch a real server: FakeListBackend stands in for
client.calls.list / client.recordings.list. That is deliberate -- QA is
currently on HYBRID, where offset is still applied and iteration looks
perfectly healthy, so a live QA call cannot reproduce the CURSOR-mode
defect.
"""

import base64

from plivo.base import ListResponseObject, ResponseObject
from tests.base import PlivoResourceTestCase

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


# How many list() calls we let a walk make before declaring it runaway.
# Every scenario below needs 3, so 10 is generous headroom.
RUNAWAY_THRESHOLD = 10


class PaginationRunaway(Exception):
    """Raised instead of letting a non-terminating walk hang the suite."""


class FakeListBackend(object):
    """A stand-in for a list endpoint, in any of the three pagination modes."""

    def __init__(self,
                 client,
                 mode,
                 total=45,
                 page_size=20,
                 path='/v1/Account/MAXXXXXXXXXXXXXXXXXX/Call/',
                 id_field='call_uuid'):
        self.client = client
        self.mode = mode
        self.total = total
        self.page_size = page_size
        self.path = path
        self.id_field = id_field
        self.call_log = []

    # -- opaque cursor tokens ------------------------------------------------
    def _encode(self, index):
        token = base64.urlsafe_b64encode(str(index).encode('utf-8'))
        return token.decode('utf-8').rstrip('=')

    def _decode(self, token):
        padded = token + '=' * (-len(token) % 4)
        return int(base64.urlsafe_b64decode(padded.encode('utf-8')))

    def _next_url(self, next_index, limit):
        if self.mode == 'offset':
            query = [('limit', limit), ('offset', next_index)]
        else:
            query = [('limit', limit), ('cursor', self._encode(next_index))]
        return self.path + '?' + urlencode(query)

    def list(self, limit=20, offset=0, cursor=None, **kwargs):
        self.call_log.append({'limit': limit, 'offset': offset,
                              'cursor': cursor})
        if len(self.call_log) > RUNAWAY_THRESHOLD:
            raise PaginationRunaway(
                'list() called {0} times walking {1} records in {2} mode -- '
                'iteration is not terminating'.format(
                    len(self.call_log), self.total, self.mode))

        limit = min(limit or 20, self.page_size)

        if self.mode == 'cursor':
            # A client-supplied offset is ignored outright: page 1 comes
            # back instead. HTTP 200, well-formed body, wrong rows.
            start = self._decode(cursor) if cursor else 0
        elif offset is not None:
            # OFFSET and HYBRID both still apply offset. When an offset
            # arrives alongside a cursor the offset is what takes effect,
            # so a client that sends offset=0 with its cursor is pinned to
            # page 1 -- which is exactly why the walk must omit offset once
            # it is following a cursor.
            start = offset
        else:
            start = self._decode(cursor) if cursor else 0

        objects = [{self.id_field: 'id-{0:03d}'.format(i)}
                   for i in range(start, min(start + limit, self.total))]
        next_index = start + limit

        meta = {
            'limit': limit,
            'offset': start if self.mode != 'cursor' else None,
            'previous': None,
            # total_count is already gone from these responses.
            'next': (self._next_url(next_index, limit)
                     if next_index < self.total else None),
        }

        return ListResponseObject(self.client, {
            'api_id': 'fake-api-id',
            'meta': ResponseObject(meta),
            'objects': [ResponseObject(o) for o in objects],
        })


class MetaLessListBackend(object):
    """A list endpoint whose responses carry no meta at all.

    Not every resource that inherits __iter__ returns meta, so the walk
    still has to handle its absence by incrementing offset and stopping
    on the first empty page.
    """

    def __init__(self, client, total=45, page_size=20):
        self.client = client
        self.total = total
        self.page_size = page_size
        self.call_log = []
        self.mode = 'offset (no meta)'
        self.id_field = 'call_uuid'

    def list(self, limit=20, offset=0, cursor=None, **kwargs):
        self.call_log.append({'limit': limit, 'offset': offset,
                              'cursor': cursor})
        if len(self.call_log) > RUNAWAY_THRESHOLD:
            raise PaginationRunaway(
                'list() called {0} times walking {1} records with no meta -- '
                'iteration is not terminating'.format(
                    len(self.call_log), self.total))
        limit = min(limit or 20, self.page_size)
        start = offset or 0
        objects = [{self.id_field: 'id-{0:03d}'.format(i)}
                   for i in range(start, min(start + limit, self.total))]
        return ListResponseObject(self.client, {
            'api_id': 'fake-api-id',
            'objects': [ResponseObject(o) for o in objects],
        })


class AutoPaginationTest(PlivoResourceTestCase):
    def _walk(self, interface, backend):
        interface.list = backend.list
        return [item for item in interface]

    def _assert_full_clean_walk(self, interface, backend):
        ids = [obj[backend.id_field] for obj in self._walk(interface,
                                                           backend)]
        expected = ['id-{0:03d}'.format(i) for i in range(backend.total)]
        self.assertEqual(
            len(ids), len(set(ids)),
            'walk yielded duplicate records in {0} mode'.format(backend.mode))
        self.assertEqual(
            ids, expected,
            'walk did not yield every record exactly once in {0} '
            'mode'.format(backend.mode))

    # -- the defect ---------------------------------------------------------
    def test_calls_iteration_terminates_in_cursor_mode(self):
        backend = FakeListBackend(self.client, mode='cursor')
        try:
            self._assert_full_clean_walk(self.client.calls, backend)
        except PaginationRunaway as exc:
            self.fail(str(exc))

    def test_recordings_iteration_terminates_in_cursor_mode(self):
        backend = FakeListBackend(
            self.client,
            mode='cursor',
            path='/v1/Account/MAXXXXXXXXXXXXXXXXXX/Recording/',
            id_field='recording_id')
        try:
            self._assert_full_clean_walk(self.client.recordings, backend)
        except PaginationRunaway as exc:
            self.fail(str(exc))

    # -- the other two live modes ------------------------------------------
    def test_calls_iteration_in_hybrid_mode(self):
        backend = FakeListBackend(self.client, mode='hybrid')
        try:
            self._assert_full_clean_walk(self.client.calls, backend)
        except PaginationRunaway as exc:
            self.fail(str(exc))

    def test_calls_iteration_in_offset_mode(self):
        backend = FakeListBackend(self.client, mode='offset')
        self._assert_full_clean_walk(self.client.calls, backend)

    def test_no_offset_is_sent_alongside_a_cursor(self):
        backend = FakeListBackend(self.client, mode='cursor')
        try:
            self._walk(self.client.calls, backend)
        except PaginationRunaway as exc:
            self.fail(str(exc))
        cursor_calls = [c for c in backend.call_log if c['cursor']]
        self.assertTrue(cursor_calls, 'walk never followed a cursor')
        for call in cursor_calls:
            self.assertIsNone(
                call['offset'],
                'offset={0!r} was sent alongside cursor={1!r}; under HYBRID '
                'that offset is still applied and pins the walk to page '
                '1'.format(call['offset'], call['cursor']))

    def test_iteration_stops_when_meta_next_is_null(self):
        """One exact page: meta.next is null, so there is nothing to follow."""
        backend = FakeListBackend(self.client, mode='cursor', total=20)
        self.client.calls.list = backend.list
        try:
            self.assertEqual(len([item for item in self.client.calls]), 20)
        except PaginationRunaway as exc:
            self.fail(str(exc))

    def test_iteration_falls_back_when_response_has_no_meta(self):
        """Meta-less list responses keep the plain offset walk."""
        backend = MetaLessListBackend(self.client, total=45)
        self.client.calls.list = backend.list
        try:
            ids = [obj['call_uuid'] for obj in self.client.calls]
        except PaginationRunaway as exc:
            self.fail(str(exc))
        self.assertEqual(ids, ['id-{0:03d}'.format(i) for i in range(45)])


class CursorParamTest(PlivoResourceTestCase):
    def test_calls_list_accepts_cursor(self):
        self.client.set_expected_response(200, {'api_id': 'x', 'meta': {},
                                                'objects': []})
        self.client.calls.list(cursor='b3BhcXVl')
        self.assertIn('cursor=b3BhcXVl', self.client.current_request.url)

    def test_recordings_list_accepts_cursor(self):
        self.client.set_expected_response(200, {'api_id': 'x', 'meta': {},
                                                'objects': []})
        self.client.recordings.list(cursor='b3BhcXVl')
        self.assertIn('cursor=b3BhcXVl', self.client.current_request.url)

    def test_calls_list_still_accepts_offset(self):
        self.client.set_expected_response(200, {'api_id': 'x', 'meta': {},
                                                'objects': []})
        self.client.calls.list(limit=10, offset=30)
        self.assertIn('offset=30', self.client.current_request.url)
        self.assertIn('limit=10', self.client.current_request.url)

    def test_recordings_list_still_accepts_offset(self):
        self.client.set_expected_response(200, {'api_id': 'x', 'meta': {},
                                                'objects': []})
        self.client.recordings.list(limit=10, offset=30)
        self.assertIn('offset=30', self.client.current_request.url)
        self.assertIn('limit=10', self.client.current_request.url)
