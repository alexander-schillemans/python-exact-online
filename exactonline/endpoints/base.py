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
        
    def list(self, select=[], filter=None, filter_operator='and'):
        url = '{0}'.format(self.endpoint)
        
        if filter:
            if filter_operator not in ['and', 'or']:
                raise ValueError("'filter_operator' can only be 'and' or 'or'.")

            url = '{url}?$filter='.format(url=url)
            count = 0
            for field, value in filter.items():
                
                # if not boolean, put single quotes around value
                if value.lower() not in ['false', 'true']:
                    value = "'{value}'".format(value=value)
                
                if count == 0:
                    url = "{url}{field} eq {value}".format(url=url, field=field, value=value)
                else:
                    url = "{url} {operator} {field} eq {value}".format(url=url, operator=filter_operator, field=field, value=value)
                    
                count += 1
        
        if select:
            url = '{url}&$select={select}'.format(url=url, select=",".join(select))
        
        status, headers, respJson = self.api.get(url)
        if status != 200: return self.listObject().parseError(status, respJson)
        listObj = self.listObject().parse(respJson['d']['results'])

        while('__next' in respJson['d']):
            nextUrl = respJson['d']['__next']
            nextUrl = nextUrl.replace('https://start.exactonline.be/api/v1/{0}/'.format(self.api.division), '')

            status, headers, respJson = self.api.get(nextUrl)
            if status != 200: return self.listObject().parseError(status, respJson)
            tempListObj = self.listObject().parse(respJson['d']['results'])

            for entryObj in tempListObj.items():
                listObj.add(entryObj)
        
        return listObj

    def get(self, id, select=[]):

        url = "{endpoint}?$filter={pkField} eq guid'{id}'".format(endpoint=self.endpoint, pkField=self.pkField, id=id)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return self.singleObject().parseError(status, respJson)

        return self.singleObject().parse(respJson['d']['results'][0])
    
    def filter(self, field, value, select=[]):
        url = "{endpoint}?$filter={field} eq {value}".format(endpoint=self.endpoint, field=field, value=value)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)
        if status != 200: return self.listObject().parseError(status, respJson)
        listObj = self.listObject().parse(respJson['d']['results'])

        while('__next' in respJson['d']):
            nextUrl = respJson['d']['__next']
            nextUrl = nextUrl.replace('https://start.exactonline.be/api/v1/{0}/'.format(self.api.division), '')

            status, headers, respJson = self.api.get(nextUrl)
            if status != 200: return self.listObject().parseError(status, respJson)
            tempListObj = self.listObject().parse(respJson['d']['results'])

            for entryObj in tempListObj.items():
                listObj.add(entryObj)
        
        return listObj

    def create(self, object):
        url = self.endpoint
        data = object.getJSON()

        status, headers, respJson = self.api.post(url, data)

        if status not in [200, 201]: return self.singleObject().parseError(status, respJson)

        return self.singleObject().parse(respJson['d'])
    
    def update(self, object):
        id = getattr(object, self.pkField)
        url = "{endpoint}(guid'{id}')".format(endpoint=self.endpoint, id=id)
        data = object.getJSON()

        status, headers, respJson = self.api.put(url, data)

        if status not in [200, 204]: return self.singleObject().parseError(status, respJson)
        return True

    def delete(self, id):
        url = "{endpoint}(guid'{id}')".format(endpoint=self.endpoint, id=id)
        data = None

        status, headers, respJson = self.api.delete(url, data)

        if status not in [200, 204]: return self.singleObject().parseError(status, respJson)
        return True

class RequiresFiltering:
    
   def list(self, select=[], filter=None, filter_operator='and'):
        if not filter:
            raise ValueError("Listing requires mandatory filtering. Specify a filter using the filter param. Syntax: { 'filter_field' : 'filter_value' }. ")
        
        return super().list(select, filter, filter_operator)