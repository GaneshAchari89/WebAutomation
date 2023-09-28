from Backend.common.CommonElements import CommonElements
from Backend.common.baseClass import BaseClass

from Backend.validateResponse.validate_test_users import ValidateUsersResponse


class Test_Users(CommonElements):

    def test_users(self):
        response = BaseClass.get_response(CommonElements.baseUrl)
        status_code = response[0]
        json_response = response[1]
        if status_code == 200:
            self.logger.info("**************** Validating json schema ****************")
            if CommonElements.validate_schema(json_response) is None:
                self.logger.info("**************** Json schema is matching ****************")
                ValidateUsersResponse.validate_response(json_response,CommonElements.users_test_data)
                assert True
            else:
                self.logger.info("**************** Json schema is not matching ****************")
                assert False
        else:
            self.logger.info("**************** Getting wrong status code ****************")
            assert False
