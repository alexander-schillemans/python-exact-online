import re
import datetime

#==============[HELPER FUNCTIONS]=================#


def getIndexWithValue(list, attribute, value):

    for index, obj in enumerate(list):
        if hasattr(obj, attribute):
            if getattr(obj, attribute) == value:
                return index
    
    return None

def getObjectWithValue(list, attribute, value):

    for index, obj in enumerate(list):
        if hasattr(obj, attribute):
            if getattr(obj, attribute) == value:
                return obj
    
    return None

def formatKey(string):
    return (string[0].upper() + string[1:]).replace('_', '@')


#==============[BASE MODELS]=================#

class BaseModel:
    
    def __init__(self):

        self.hasError = False
        self.error = None

    def parse(self, json):
        for key, value in json.items():
            lowerKey = ''.join(e.lower() for e in key if e.isalnum())
            lowerAttrs = { k.replace('_', '').lower() : k for k in self.__dict__.keys() }

            if lowerKey in lowerAttrs.keys():
                key = lowerAttrs[lowerKey]
                attrVal = getattr(self, key)

                if isinstance(attrVal, BaseModel):
                    setattr(self, key, attrVal.parse(value))
                else:

                    if value and 'Date' in str(value):
                        epoch = int(re.search(r"\((.*?)\)", value).group(1))
                        epoch = round((epoch/1000))
                        value = datetime.datetime.utcfromtimestamp(epoch)
                    
                    setattr(self, key, value)

        return self
    
    def getJSON(self):

        dikt = {}
        for k, v in self.__dict__.items():
            if v:
                k = formatKey(k)
                if isinstance(v, BaseModel):
                    json = v.getJSON()
                    if json: dikt[k] = json
                else:
                    if isinstance(v, datetime.datetime): v = v.strftime('%Y-%m-%dT%H:%M:%S')
                    dikt[k] = v

        return dikt if len(dikt) > 0 else None
    
    def parseError(self, json):

        from .errors import Error
        
        self.hasError = True
        self.error = Error(code=json['error']['code'], message=json['error']['message']['value'])

        return self

class ObjectListModel(BaseModel):

    def __init__(self, list=[], listObject=None):
        super().__init__()

        self.list = list
        self.listObject = listObject
        self.hasError = False
        self.error = None
    
    def add(self, item):
        self.list.append(item)
        return self.list
    
    def remove(self, item):
        self.list.remove(item)
        return self.list

    def getItemIndex(self, attribute, value):
        index = getIndexWithValue(self.list, attribute, value)
        return index
    
    def getItemObject(self, attribute, value):
        object = getObjectWithValue(self.list, attribute, value)
        return object
    
    def parse(self, json):

        if isinstance(json, dict):
            itemObj = self.listObject().parse(json)
            self.add(itemObj)
        elif isinstance(json, list):
            for item in json:
                itemObj = self.listObject().parse(item)
                self.add(itemObj)

        return self
    
    def getJSON(self):
        list = []

        for item in self.list:
            list.append(item.getJSON())
        
        return list if len(list) > 0 else None

    def items(self):
        return self.list