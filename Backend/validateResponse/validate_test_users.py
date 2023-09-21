from jsonpath_ng import jsonpath
import jsonpath_ng.ext as jp


class ValidateResponse:
    @staticmethod
    def validate_response(response):
        for match in jp.parse("users[*].firstName").find(response):
            print("$$$$$$",match.value)
