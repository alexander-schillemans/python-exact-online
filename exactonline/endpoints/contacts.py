from .base import APIEndpoint

from exactonline.models.contacts import Contact, ContactList

class ContactMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'crm/Contacts', Contact, ContactList)