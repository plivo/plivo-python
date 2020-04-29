from ..base import PlivoResourceInterface
from requests import Request
from plivo.exceptions import ValidationError


FEEDBACK_API_PATH = "v1/Call/{}/Feedback/"


class CallFeedback(PlivoResourceInterface):
    def create(self, call_uuid, rating, issues=[], notes=""):
        if len(call_uuid) == 0:
            raise ValidationError('call_uuid cannot be empty')
        if not rating:
            raise ValidationError('rating cannot be empty')
        request_path = FEEDBACK_API_PATH.format(call_uuid)
        params_dict = {}
        params_dict['rating'] = rating
        if len(issues) > 0:
            params_dict['issues'] = issues
        if len(notes) > 0:
            params_dict['notes'] = notes
        params_dict['is_callinsights_request'] = True
        params_dict['callinsights_request_path'] = request_path
        return self.client.request('POST', ('Call', ), params_dict)
