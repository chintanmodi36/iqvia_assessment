from flask import Flask
from flask_restful import Resource, Api
import xml.etree.ElementTree as ET
import requests


app = Flask(__name__)
api = Api(app)


class TraverseXML(Resource):
    def __init__(self):
        self.url = "https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d={}&lup_d=&sel_rss=new14&cond={}&count=10000"

    def get(self, disease, no_of_days):
        url = self.url.format(no_of_days, disease)
        response_xml_as_string = requests.get(url).text
        responseXml = ET.fromstring(response_xml_as_string)
        items = responseXml.find('channel').findall('item')
        result_string = "{} modifications for disease {} in last {} days".format(len(items), disease, no_of_days)
        result = {'result': result_string}
        return result, 200


class DefaultURL(Resource):
    def get(self):
        return "Modify your URL like 'http://0.0.0.0:5000/disease_name/number_of_days'"


api.add_resource(TraverseXML, '/<string:disease>/<int:no_of_days>')
api.add_resource(DefaultURL, '/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
