from .base import APIEndpoint

from exactonline.models.documents import Document,DocumentAttachment, DocumentAttachmentList, DocumentList, DocumentType, DocumentTypeCategory, DocumentTypeCategoryList, DocumentTypeList
from exactonline.utils import encodeFileToB64, getFileName

class DocumentMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'documents', Document, DocumentList)
    
    def list(self, select=[]):
        url = "{endpoint}/Documents".format(endpoint=self.endpoint)
        if select: url = '{url}/Documents&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return DocumentList().parseError(status, respJson)

        return DocumentList().parse(respJson['d']['results'])
    
    def listTypes(self, select=[]):
        url = "{endpoint}/DocumentTypes".format(endpoint=self.endpoint)
        if select: url = '{url}/DocumentTypes&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return DocumentTypeList().parseError(status, respJson)
        
        return DocumentTypeList().parse(respJson['d']['results'])

    def listTypeCategories(self, select=[]):
        url = "{endpoint}/DocumentTypeCategories".format(endpoint=self.endpoint)
        if select: url = '{url}/DocumentTypeCategories&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return DocumentTypeCategoryList().parseError(status, respJson)
        
        return DocumentTypeCategoryList().parse(respJson['d']['results'])

    def get(self, id, select=[]):

        url = "{endpoint}/Documents?$filter=ID eq guid'{id}'".format(endpoint=self.endpoint, id=id)
        if select: url = '{url}&$select={select}'.format(url=url, select=",".join(select))

        status, headers, respJson = self.api.get(url)

        if status != 200: return Document().parseError(status, respJson)

        return Document().parse(respJson['d']['results'][0])

    def create(self, document, attachments=[]):
    
        url = "{endpoint}/Documents".format(endpoint=self.endpoint)
        data = document.getJSON()

        # 1: create Document
        status, headers, respJson = self.api.post(url, data)
        if status not in [200, 201]: return Document().parseError(status, respJson)
        
        document = Document().parse(respJson['d'])

        # 2: create and link Attachments
        for attachment in attachments:
            dAttachment = DocumentAttachment(
                Attachment=encodeFileToB64(attachment),
                Document=document.ID,
                FileName=getFileName(attachment)
            )

            data = dAttachment.getJSON()
            url = "{endpoint}/DocumentAttachments".format(endpoint=self.endpoint)
            status, headers, respJson = self.api.post(url, data)
            
            if status in [200, 201]: document.Attachments.add(dAttachment)
        
        return document