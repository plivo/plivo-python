
from plivo.utils.validators import *

from ..base import ListResponseObject, PlivoResource, PlivoResourceInterface, ResponseObject
from ..exceptions import *
from ..utils import *

class NumberPool(PlivoResource):
    _name = 'NumberPool'
    _identifier_string = 'number_pool_id'
    shortcodes = None
    numbers = None
    tollfree = None
    def __init__(self, client, number_pool_id):
        self.shortcodes = Shortcode(client, number_pool_id)
        self.numbers = Numbers(client, number_pool_id)
        self.tollfree = Tollfree(client, number_pool_id)
    
    
class Numbers(PlivoResource):
    _name = 'Numbers'
    _identifier_string = 'number_pool_id'

    def buy_add_number(self,
        pattern=None,
        country_iso2=None,
        type=None, 
        region=None, 
        number='',
        service=None):
        params = {}
        params['rent'] = 'true'
        if service:
            params['service'] = service
        if self.number_pool_id != "":   
            if number !="":
                return self.client.request(
                'POST', ('NumberPool',self.number_pool_id,'Number', number),params,
                response_type=None,
                objects_type=None)
            else :
                phonenumberparam = {}
                if pattern:
                    phonenumberparam['pattern'] = pattern
                if type:
                    phonenumberparam['type'] = type
                if country_iso2:
                    phonenumberparam['country_iso'] = country_iso2
                if region:
                    phonenumberparam['region'] = region
                if service:
                    phonenumberparam['service'] = service
                number_response = self.client.request(
                        'GET',
                        ('PhoneNumber', ),
                        phonenumberparam,
                        objects_type=None,
                        response_type=None, )
                if len(number_response)< 1:
                    raise  ResourceNotFoundError('Resource not found')
                number = number_response[0]['number']
                return self.client.request(
                'POST', ('NumberPool',self.number_pool_id,'Number', number),params,
                response_type=None,
                objects_type=None)
        else:
            raise ResourceNotFoundError('Resource not found')
    
    @validate_args(
    number=[of_type(six.text_type)]
    )
    def remove(self,  number, unrent=False):
        params = {}
        params['unrent'] = unrent
        return self.client.request(
            'DELETE', ('NumberPool',self.number_pool_id,'Number', number), params,
            response_type=None,
            objects_type=None)

    @validate_args(
    number=[of_type(six.text_type)]
    )
    def add(self,  number, service=None):
        params = {}
        if service:
            params['service'] = service
        return self.client.request(
            'POST', ('NumberPool',self.number_pool_id,'Number', number), params,
            response_type=None,
            objects_type=None)
    
    @validate_args(
    number=[of_type(six.text_type)]
    )
    def find(self, number, service=None):
        params = {}
        if service:
            params['service'] = service
        return self.client.request(
            'GET', ('NumberPool',self.number_pool_id,'Number', number), params, 
            response_type=None,
            objects_type=None)
    
    def count(self,
        starts_with=None, 
        country_iso2=None,
        type=None,
        service=None):
        params ={}
        if starts_with:
            params['starts_with'] = starts_with
        if country_iso2:
            params['country_iso2'] = country_iso2
        if type:
            params['type'] = type
        if service:
            params['service'] = service
        
        try:
            response = self.client.request(
            'GET', ('NumberPool',self.number_pool_id,'Number'),
            params ,response_type=None,
            objects_type=None)
            return response['meta']['total_count']
        except:
            return 0

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
        starts_with=None, 
        country_iso2=None,
        type=None, limit=None, 
        offset=None, service=None):
        params ={}
        if starts_with:
            params['starts_with'] = starts_with
        if country_iso2:
            params['country_iso2'] = country_iso2
        if type:
            params['type'] = type
        if service:
            params['service'] = service
        if limit:
            params['limit']= limit
        if offset:
            params['offset'] = offset
        return self.client.request('GET', ('NumberPool',self.number_pool_id,'Number'),
                params ,response_type=None,
                objects_type=None)
         
class Shortcode(PlivoResource):
    _name = 'Shortcodes'
    _identifier_string = 'number_pool_id'

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
    def list(self, limit=None, offset=None):
        params = {}
        if limit:
            params['limit']= limit
        if offset:
            params['offset'] = offset
        return self.client.request('GET', ('NumberPool',self.number_pool_id,'Shortcode'),params,
            response_type=None,
            objects_type=None)

    @validate_args(shortcode=[of_type(six.text_type)])
    def find(self, shortcode):
        return self.client.request('GET', ('NumberPool',self.number_pool_id,'Shortcode', shortcode),
            response_type=None,
            objects_type=None)

    @validate_args(
    shortcode=[of_type(six.text_type)]
    )
    def remove(self, shortcode):
        return self.client.request(
            'DELETE', ('NumberPool',self.number_pool_id,'Shortcode', shortcode),
            response_type=None,
            objects_type=None)

class Tollfree(PlivoResource):
    _name = 'Tollfree'
    _identifier_string = 'number_pool_id'


    @validate_args(
    number=[of_type(six.text_type)]
    )
    def add(self,  number):
        return self.client.request(
            'POST', ('NumberPool',self.number_pool_id,'Tollfree', number),
            response_type=None,
            objects_type=None)

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
    def list(self, limit=None, offset=None):
        params = {}
        if limit:
            params['limit']= limit
        if offset:
            params['offset'] = offset
        return self.client.request('GET', ('NumberPool',self.number_pool_id,'Tollfree'),params,
            response_type=None,
            objects_type=None)

    @validate_args(tollfree=[of_type(six.text_type)])
    def find(self, tollfree):
        return self.client.request('GET', ('NumberPool',self.number_pool_id,'Tollfree', tollfree),
            response_type=None,
            objects_type=None)

    @validate_args(
    tollfree=[of_type(six.text_type)]
    )
    def remove(self, tollfree, unrent=False):
        params = {}
        params['unrent'] = unrent
        return self.client.request(
            'DELETE', ('NumberPool',self.number_pool_id,'Tollfree', tollfree), params,
            response_type=None,
            objects_type=None)

