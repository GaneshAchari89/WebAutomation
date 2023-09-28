import jsonpath_ng.ext as jp
from Backend.utilities.csvUtil import CsvData


class ValidateUsersResponse:
    @staticmethod
    def validate_response(response,test_data_loc):
        test_data = CsvData.readCsv(test_data_loc)
        id_list = []
        first_names_list = []
        last_names_list = []
        emails_list = []
        city_list = []
        for match in jp.parse("users[*].id").find(response):
            id_list.append(match.value)
        for match in jp.parse("users[*].firstName").find(response):
            first_names_list.append(match.value)
        for match in jp.parse("users[*].lastName").find(response):
            last_names_list.append(match.value)
        for match in jp.parse("users[*].email").find(response):
            emails_list.append(match.value)
        for match in jp.parse("users[*].address.city").find(response):
            city_list.append(match.value)
        for i in range(len(test_data)):
            assert test_data[i][0] == str(id_list[i])
            assert test_data[i][1] == first_names_list[i]
            assert test_data[i][2] == last_names_list[i]
            assert test_data[i][3] == emails_list[i]
            assert test_data[i][4] == city_list[i]