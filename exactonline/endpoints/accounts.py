from .base import APIEndpoint

from exactonline.models.accounts import Account, AccountList

class AccountMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'crm/Accounts', Account, AccountList)