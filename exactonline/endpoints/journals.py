from .base import APIEndpoint

from exactonline.models.journals import Journal, JournalList

class JournalMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'financial/Journals', Journal, JournalList)