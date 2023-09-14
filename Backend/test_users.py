from Backend.CommonElements import CommonElements
from Backend.baseClass import BaseClass

from jsonschema import validate
import json


class Test_Users(CommonElements):

    def test_users(self):
        response = BaseClass.get_response(CommonElements.baseUrl)
        status_code = response[0]
        json_response = response[1]
        if status_code == 200:
            self.logger.info("**************** Validating json schema ****************")
            if CommonElements.validate_schema(json_response) is None:
                self.logger.info("**************** Json schema is matching ****************")
                assert True
            else:
                self.logger.info("**************** Json schema is not matching ****************")
                assert False
        else:
            self.logger.info("**************** Getting wrong status code ****************")
            assert False
