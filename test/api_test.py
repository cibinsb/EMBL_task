import unittest
import falcon
from falcon import testing
from app import api
from helper.log import logger


class EMBLTestCase(testing.TestCase):
    def setUp(self):
        super(EMBLTestCase, self).setUp()
        self.app = api

class TestEMBL(EMBLTestCase):
    def test_get_all_records(self):
        logger.info("Searching for gene name tbx")
        result = self.simulate_get('/api/v1/embl/search?name=tbx')
        self.assertEqual(result.status, falcon.HTTP_200)

    def test_validate_params(self):
        logger.info("Validating parameters")
        output={u"error": u"Search param 'name' cannot be none or less than 3 chars"}
        result = self.simulate_get('/api/v1/embl/search?name=tb')
        self.assertEqual(result.json, output)

    def test_http_methods(self):
        logger.info("Testing Http methods like POST, PUT, DELETE")
        result = self.simulate_post('/api/v1/embl/search?name=tbx')
        self.assertEqual(result.status, falcon.HTTP_405)
        result = self.simulate_put('/api/v1/embl/search?name=tbx')
        self.assertEqual(result.status, falcon.HTTP_405)
        result = self.simulate_delete('/api/v1/embl/search?name=tbx')
        self.assertEqual(result.status, falcon.HTTP_405)

if __name__ == '__main__':
        unittest.main()