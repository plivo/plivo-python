from lxml import etree

from plivo.exceptions import PlivoXMLError


class PlivoXMLElement(object):
    def __init__(self):
        self.content = ''
        self.children = []

    def add(self, element):
        if not isinstance(element, PlivoXMLElement):
            raise PlivoXMLError('element must be a PlivoXMLElement')

        if element._name not in self._nestable:
            raise PlivoXMLError(
                '{} is not nestable in {} (allowed: {})'.format(
                    element._name, self._name, self._nestable))
        self.children.append(element)
        return self

    def continue_speak(self, body=None):
        return body.replace('<cont>', ' ').replace('</cont>', ' ')

    def to_string(self, pretty=True):
        s = self.continue_speak(etree.tostring(self._to_element(), pretty_print=pretty, encoding='unicode'))

        if not isinstance(s, str):
            s = s.encode('utf-8')
        return s

    def _to_element(self, parent=None):
        e = etree.SubElement(
            parent, self._name,
            **self.to_dict()) if parent is not None else etree.Element(
                self._name, **self.to_dict())
        if self.content:
            try:
                e.text = self.content.decode()
            except:
                e.text = self.content
        for child in self.children:
            child._to_element(parent=e)
        return e
