from .base import APIEndpoint

from exactonline.models.accounts import Account, AccountList

class AccountMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'crm/Accounts')
    
    def list(self, select=[]):
        url = self.endpoint
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return AccountList().parseError(respJson)

        return AccountList().parse(respJson['d']['results'])

    def get(self, id, select=[]):

        url = "{endpoint}?$filter=ID eq guid'{id}'".format(endpoint=self.endpoint, id=id)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return Account().parseError(respJson)

        return Account().parse(respJson['d']['results'][0])

    def create(self, account):
        url = self.endpoint
        data = account.getJSON()

        status, headers, respJson = self.api.post(url, data)

        if status not in [200, 201]: return Account().parseError(respJson)

        return Account().parse(respJson['d'])