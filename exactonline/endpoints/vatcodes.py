from .base import APIEndpoint

from exactonline.models.vat import VATPercentageList, VATPercentage, VATCode, VATCodeList

class VATCodeMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'vat/VATCodes', VATCode, VATCodeList)
    

    def get(self, id, select=[]):

        # 1: retrieve VATCode
        vatCode = super().get(id, select)

        # 2: retrieve Percentages
        url = "{endpoint}(guid'{entryId}')/VATPercentages".format(endpoint=self.endpoint, entryId=vatCode.ID)
        status, headers, respJson = self.api.get(url)

        if status != 200: return VATPercentageList().parseError(status, respJson)
        VATPercentages = VATPercentageList().parse(respJson['d']['results'])

        vatCode.VATPercentages = VATPercentages

        return vatCode