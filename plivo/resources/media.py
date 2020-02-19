# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import ListResponseObject, PlivoResource, PlivoResourceInterface
from ..exceptions import *
from ..utils import *


class Media(PlivoResource):
    _name = 'Media'
    _identifier_string = 'media_id'

    def get(self):
        return self.client.medias.get(self.id)


class Media(PlivoResourceInterface):
    _resource_type = Media

    @validate_args(
        media_file=[optional(of_type_exact(list))])
    def upload(self, media_file):
        if media_file:
            fileList = []
            for media_url in media_file:
                file_extension = media_url.strip().split('.')[-1].lower()
                if file_extension not in ['jpeg', 'jpg', 'png', 'xcf', 'plain', 'pdf', 'mpeg', 'mp4']:
                    raise ValidationError(
                        'File format of the file to be uploaded should be one of JPG, JPEG, PNG or PDF'
                    )
                content_types = {
                    'jpeg': 'image/jpeg',
                    'jpg': 'image/jpeg',
                    'png': 'image/png',
                    'pdf': 'application/pdf',
                    'xcf': 'image/xcf',
                    'text': 'text/plain',
                    'mpeg': 'video/mpeg',
                    'mp4': 'video/mp4'
                }
                print(media_url)
                import os
                files = (
                    'file', (media_url.split(os.sep)[-1], open(
                        media_url, 'rb'), content_types[file_extension])
                )
                fileList.append(files)
        data_to_send = {}
        return self.client.request(
            'POST', ('Media', ), data_to_send, files=fileList)

    @validate_args(media_id=[of_type(six.text_type)])
    def get(self, media_id):
        return self.client.request(
            'GET', ('Media', media_id), response_type=None)

    @validate_args(
        limit=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda limit: 0 < limit <= 20, '0 < limit <= 20')))
        ],
        offset=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda offset: 0 <= offset, '0 <= offset')))
        ])
    def list(self,
             limit=20,
             offset=0):
        return self.client.request(
            'GET', ('Media', ),
            to_param_dict(self.list, locals()),
            response_type=None)
