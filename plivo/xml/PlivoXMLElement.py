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

    def to_string(self):
        s = etree.tostring(self._to_element(), pretty_print=True)
        return s.decode('utf-8')

    def _to_element(self, parent=None):
        e = etree.SubElement(
            parent, self._name,
            **self.to_dict()) if parent is not None else etree.Element(
                self._name, **self.to_dict())
        e.text = self.content
        for child in self.children:
            child._to_element(parent=e)
        return e
