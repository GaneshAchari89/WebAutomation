import json
from Backend.utilities.readProperties import ReadConfig
from Backend.utilities.customLogger import LogGenerator
from jsonschema import validate


class CommonElements():
    baseUrl = ReadConfig.getBaseUrl()
    logger = LogGenerator.generateLogger()

    users_schema = ReadConfig.getUsersSchema()

    @staticmethod
    def validate_schema(response):
        with open(CommonElements.users_schema, 'r') as f:
            schema = json.load(f)
        return validate(instance=response, schema=schema)


