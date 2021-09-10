from .base import APIEndpoint

from exactonline.models.glaccounts import GLAccountList, GLAccount

class GLAccountMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'financial/GLAccounts')
    
    def list(self, select=[]):
        url = self.endpoint
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return GLAccountList().parseError(respJson)

        return GLAccountList().parse(respJson['d']['results'])

    def get(self, id, select=[]):

        url = "{endpoint}?$filter=ID eq guid'{id}'".format(endpoint=self.endpoint, id=id)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return GLAccount().parseError(respJson)

        return GLAccount().parse(respJson['d']['results'][0])

    def create(self, glAccount):
        url = self.endpoint
        data = glAccount.getJSON()

        status, headers, respJson = self.api.post(url, data)

        if status not in [200, 201]: return GLAccount().parseError(respJson)

        return GLAccount().parse(respJson['d'])
