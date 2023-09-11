from Backend.CommonElements import CommonElements
from Backend.baseClass import BaseClass


class Test_Users(CommonElements):

    def test_users(self):
        response = BaseClass.get_response(CommonElements.baseUrl)
        print(response)
