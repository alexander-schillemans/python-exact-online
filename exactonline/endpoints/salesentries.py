from .base import APIEndpoint

from exactonline.models.salesentries import SalesEntryLineList, SalesEntryList, SalesEntry, SalesEntryLine

class SalesEntryMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'salesentry/SalesEntries', SalesEntry, SalesEntryList, pkField='EntryID')

    def get(self, id, select=[]):

        # 1: retrieve Sales Entry
        salesEntry = super().get(id, select)

        # 2: retrieve Sales Lines
        url = "{endpoint}(guid'{entryId}')/SalesEntryLines".format(endpoint=self.endpoint, entryId=salesEntry.EntryID)
        status, headers, respJson = self.api.get(url)

        if status != 200: return SalesEntryLineList().parseError(status, respJson)
        salesEntryLines = SalesEntryLineList().parse(respJson['d']['results'])

        salesEntry.SalesEntryLines = salesEntryLines

        return salesEntry