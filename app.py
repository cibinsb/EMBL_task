import falcon
import json
import pathlib
from helper.log import logger
from src.middleware import HttpMethodValidator
from helper.utils import Constants
from src.query_builder import RunQuery
from src.db import DataBase
from falcon_swagger_ui import register_swaggerui_app

try:
    logger.info("Connecting to Database")
    database = DataBase(True)
    logger.info(database)
    logger.info("Connection successful")
except Exception as ex:
    logger.info("Error " + str(ex))
    raise Exception("Error Couldn't connect to %s Database" % (Constants.database.value))


class Home:
    def on_get(self, req, resp):
        logger.info("Sending response")
        resp.status = falcon.HTTP_200
        resp.body = json.dumps([{Constants.message.value: "server works"}], ensure_ascii=False)


SWAGGERUI_URL = '/swagger'
SCHEMA_URL = '/static/v1/swagger.json'
STATIC_PATH = pathlib.Path(__file__).parent / 'static'

home = Home()
search = RunQuery(database)
api = falcon.API(middleware=[HttpMethodValidator()])
api.add_static_route('/static', str(STATIC_PATH))
api.add_route('/', home)
api.add_route('/api/v1/embl/search', search)
page_title = 'EMBL search API doc'


register_swaggerui_app(
    api, SWAGGERUI_URL, SCHEMA_URL,
    page_title=page_title,
    config={'supportedSubmitMethods': ['get'], }
)