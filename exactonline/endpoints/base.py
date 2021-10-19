class APIEndpoint:

    def __init__(self, 
        api, 
        endpoint,
        singleObject,
        listObject,
        pkField='ID'
    ):

        self.api = api
        self.endpoint = endpoint
        self.singleObject = singleObject
        self.listObject = listObject
        self.pkField = pkField
    
    def list(self, select=[]):
        url = self.endpoint
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)
        if status != 200: return self.listObject().parseError(respJson)
        listObj = self.listObject().parse(respJson['d']['results'])

        while('__next' in respJson['d']):
            nextUrl = respJson['d']['__next']
            nextUrl = nextUrl.replace('https://start.exactonline.be/api/v1/{0}/'.format(self.api.division), '')

            status, headers, respJson = self.api.get(nextUrl)
            if status != 200: return self.listObject().parseError(respJson)
            tempListObj = self.listObject().parse(respJson['d']['results'])

            for entryObj in tempListObj.items():
                listObj.add(entryObj)
        
        return listObj

    def get(self, id, select=[]):

        url = "{endpoint}?$filter={pkField} eq guid'{id}'".format(endpoint=self.endpoint, pkField=self.pkField, id=id)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return self.singleObject().parseError(respJson)

        return self.singleObject().parse(respJson['d']['results'][0])
    
    def filter(self, field, value, select=[]):
        url = "{endpoint}?$filter={field} eq {value}".format(endpoint=self.endpoint, field=field, value=value)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)
        if status != 200: return self.listObject().parseError(respJson)
        listObj = self.listObject().parse(respJson['d']['results'])

        while('__next' in respJson['d']):
            nextUrl = respJson['d']['__next']
            nextUrl = nextUrl.replace('https://start.exactonline.be/api/v1/{0}/'.format(self.api.division), '')

            status, headers, respJson = self.api.get(nextUrl)
            if status != 200: return self.listObject().parseError(respJson)
            tempListObj = self.listObject().parse(respJson['d']['results'])

            for entryObj in tempListObj.items():
                listObj.add(entryObj)
        
        return listObj

    def create(self, object):
        url = self.endpoint
        data = object.getJSON()

        status, headers, respJson = self.api.post(url, data)

        if status not in [200, 201]: return self.singleObject().parseError(respJson)

        return self.singleObject().parse(respJson['d'])
    
    def update(self, object):
        id = getattr(object, self.pkField)
        url = "{endpoint}(guid'{id}')".format(endpoint=self.endpoint, id=id)
        data = object.getJSON()

        status, headers, respJson = self.api.put(url, data)

        if status not in [200, 204]: return self.singleObject().parseError(respJson)
        return True

    def delete(self, id):
        url = "{endpoint}(guid'{id}')".format(endpoint=self.endpoint, id=id)
        data = None

        status, headers, respJson = self.api.delete(url, data)

        if status not in [200, 204]: return self.singleObject().parseError(respJson)
        return True