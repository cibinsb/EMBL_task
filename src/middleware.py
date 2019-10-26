import falcon
import json
from helper.log import logger
from helper.utils import Constants


class HttpMethodValidator(object):
    def process_request(self, req, resp):
        if req.method not in ["GET"]:
            logger.info("")
            resp.status = falcon.HTTP_405
            resp.body = json.dumps({Constants.error.value: "API supports only [GET,]"})
