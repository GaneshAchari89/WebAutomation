import requests


class BaseClass:

    @staticmethod
    def get_response(url):
        response = requests.get(url)
        response_json = response.json()
        return response_json
