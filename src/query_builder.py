import falcon
import json
from helper.log import logger
from helper.utils import Constants


class RunQuery:
    def __init__(self, database):
        self.database = database

    def on_get(self, req, resp):
        gene_name = req.get_param(Constants.name.value, None)
        species = req.get_param(Constants.species.value, None)
        http_status = falcon.HTTP_400
        if gene_name and len(gene_name) >= Constants.min_keyword_count.value:
            query = "select  stable_id as id, display_label as name, species  from %s where display_label like '%s'" \
                    % (Constants.database.value + "." + Constants.table.value, gene_name.lower() + "%")
            query += " and species = '" + species + "';" if species else ";"
            try:
                http_status = falcon.HTTP_200
                response_body = json.dumps(self.database.get_data(query), ensure_ascii=False)
            except Exception as exp:
                logger.info(str(exp))
                http_status = falcon.HTTP_400
                response_body = json.dumps({Constants.error.value: str(exp)})
        else:
            response_body = json.dumps({Constants.error.value: "Search param 'name' cannot be none or less than 3 chars"})
        resp.content_type = falcon.MEDIA_JSON
        resp.status = http_status
        resp.body = response_body
