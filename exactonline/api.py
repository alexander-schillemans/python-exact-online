import base64
import requests
import json
import time

from . import config
from .cachehandler import CacheHandler
from .authhandler import AuthHandler

from .endpoints.salesentries import SalesEntryMethods
from .endpoints.accounts import AccountMethods
from .endpoints.journals import JournalMethods
from .endpoints.glaccounts import GLAccountMethods
from .endpoints.documents import DocumentMethods
from .endpoints.contacts import ContactMethods
from .endpoints.vatcodes import VATCodeMethods

class ExactOnlineAPI:

    def __init__(self, client_id, client_secret, stall_if_rate_limit_exceeded=True):

        self.clientId = client_id
        self.clientSecret = client_secret
        self.division = None

        self.headers = {
            'Accept' : 'application/json',
            'Content-Type' : 'application/json',
        }

        self.api_rate_limits = {
            'minutely_remaining' : 10000000, # Insanely high number, will get updated after first call
            'daily_remaining' : 10000000, # Insanely high number, will get updated after first call
            'reset_at' : 0 # from epoch, in milliseconds
        }

        # Set to True to stall the program if the rate limit is exceeded
        # Otherwise, we'll throw an error
        self.stall_if_rate_limit_exceeded = stall_if_rate_limit_exceeded

        self.baseUrl = config.BASE_URL
        self.cacheHandler = CacheHandler()
        self.authHandler = AuthHandler(self, self.clientId, self.clientSecret)

        self.salesEntries = SalesEntryMethods(self)
        self.accounts = AccountMethods(self)
        self.journals = JournalMethods(self)
        self.glAccounts = GLAccountMethods(self)
        self.documents = DocumentMethods(self)
        self.contacts = ContactMethods(self)
        self.vatCodes = VATCodeMethods(self)

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

        # Check the rate limit headers and update internally
        if 'X-RateLimit-Minutely-Remaining' in response.headers:
            self.api_rate_limits['minutely_remaining'] = int(response.headers['X-RateLimit-Minutely-Remaining'])
        
        if 'X-RateLimit-Remaining' in response.headers:
            self.api_rate_limits['daily_remaining'] = int(response.headers['X-RateLimit-Remaining'])

        if 'X-RateLimit-Reset' in response.headers:
            self.api_rate_limits['reset_at'] = int(response.headers['X-RateLimit-Reset'])

        # Check if we need to stall
        if self.api_rate_limits['minutely_remaining'] < 1:
            if self.stall_if_rate_limit_exceeded:
                time.sleep(60) # Minutely rate limit exceeded, stall for a minute
            else:
                raise Exception('Minutely Rate limit exceeded')
        elif self.api_rate_limits['daily_remaining'] < 1:
            raise Exception('Daily Rate limit exceeded. Stalling not supported.')
        
        return response

    def request(self, method, url, data=None, headers=None, files=None):

        self.authHandler.checkHeaderTokens()
        self.checkDivision()

        response = self.doRequest(method, url, data, headers, files)
        respContent = json.loads(response.content) if response.content else None

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