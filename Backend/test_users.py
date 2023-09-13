from Backend.CommonElements import CommonElements
from Backend.baseClass import BaseClass

from jsonschema import validate
import json


class Test_Users(CommonElements):

    def test_users(self):
        response = BaseClass.get_response(CommonElements.baseUrl)
        self.logger.info("**************** Validating json schema ****************")
        if CommonElements.validate_schema(response) is None:
            self.logger.info("**************** Json schema is matching ****************")
            assert True
        else:
            self.logger.info("**************** Json schema is not matching ****************")
            assert False




