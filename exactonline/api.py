import base64
import requests
import json
import time

from . import config
from .cachehandler import CacheHandler
from .authhandler import AuthHandler
from .endpoints.salesentries import SalesEntryMethods

class ExactOnlineAPI:

    def __init__(self, clientId, clientSecret):

        self.clientId = clientId
        self.clientSecret = clientSecret
        self.division = None

        self.headers = {
            'Accept' : 'application/json',
            'Content-Type' : 'application/json',
        }

        self.baseUrl = config.BASE_URL
        self.cacheHandler = CacheHandler()
        self.authHandler = AuthHandler(self, self.clientId, self.clientSecret)

        self.salesEntries = SalesEntryMethods(self)

    def doRequest(self, method, url, data=None, headers=None, files=None):

        if headers:
            mergedHeaders = self.headers
            mergedHeaders.update(headers)
            headers = mergedHeaders
        else: headers = self.headers

        reqUrl = '{base}/{division}/{url}'.format(base=self.baseUrl, division=self.division, url=url)

        if method == 'GET':
            response = requests.get(reqUrl, params=data, headers=headers)
        elif method == 'POST':
            if files: response = requests.post(reqUrl, data=json.dumps(data), files=files, headers=headers)
            else: response = requests.post(reqUrl, data=json.dumps(data), headers=headers)
        elif method == 'PUT':
            response = requests.put(reqUrl, data=json.dumps(data), headers=headers)
        elif method == 'DELETE':
            response = requests.delete(reqUrl, params=json.dumps(data), headers=headers)

        return response

    def request(self, method, url, data=None, headers=None, files=None):

        self.authHandler.checkHeaderTokens()
        self.checkDivision()

        response = self.doRequest(method, url, data, headers, files)
        respContent = json.loads(response.content)
        
        return response.status_code, response.headers, respContent
    
    def checkDivision(self):
        if not self.division:
            url = '{base}/current/Me?$select=CurrentDivision'.format(base=self.baseUrl)
            response = requests.get(url, params=None, headers=self.headers)

            jsonResp = json.loads(response.content)
            self.division = jsonResp['d']['results'][0]['CurrentDivision']

    def get(self, url, data=None, headers=None):
        status, headers, response = self.request('GET', url, data, headers)
        return status, headers, response
    
    def post(self, url, data=None, headers=None, files=None):
        status, headers, response = self.request('POST', url, data, headers, files)
        return status, headers, response
    
    def put(self, url, data=None, headers=None):
        status, headers, response = self.request('PUT', url, data, headers)
        return status, headers, response
    
    def delete(self, url, data=None, headers=None):
        status, headers, response = self.request('DELETE', url, data, headers)
        return status, headers, response