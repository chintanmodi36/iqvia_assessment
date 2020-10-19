import unittest
from unittest.mock import patch
import app


class TestTraversXML(unittest.TestCase):

    def setUp(self):
        self.url = "https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d={}&lup_d=&sel_rss=new14&cond={}&count=10000"

    @patch("app.TraverseXML")
    def test_traverseXML(self, mock):
        obj = mock()
        fake_json = {'result': 'modifications'}
        obj.get.return_value.status_code = 200
        obj.get.return_value.data = fake_json
        response = obj.get('/AlzheimerDisease/14')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, fake_json)

    def test_get(self):
        disease = "AlzheimerDisease"
        no_of_days = 14
        actual = app.TraverseXML.get(self, disease, no_of_days)
        expected = ({'result': '0 modifications for disease AlzheimerDisease in last 14 days'}, 200)
        self.assertEqual(actual, expected)

    def test_get_activity(self):
        disease = "Amnesia"
        no_of_days = 1
        actual = app.TraverseXML.get(self, disease, no_of_days)
        expected = ({'result': '1 modifications for disease Amnesia in last 1 days'}, 200)
        self.assertNotEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
