from .base import APIEndpoint

from exactonline.models.glaccounts import GLAccountList, GLAccount

class GLAccountMethods(APIEndpoint):

    def __init__(self, api):
        super().__init__(api, 'financial/GLAccounts', GLAccount, GLAccountList)