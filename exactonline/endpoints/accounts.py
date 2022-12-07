from .base import APIEndpoint, RequiresFiltering

from exactonline.models.accounts import Account, AccountList

class AccountMethods(RequiresFiltering, APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'crm/Accounts', Account, AccountList)