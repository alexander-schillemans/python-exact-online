import time
import json

from requests_oauthlib import OAuth2Session

from . import config
from .constants.errors import NotFoundError

class AuthHandler:

    def __init__(self, api, clientId, clientSecret):
        self.clientId = clientId

        self.clientSecret = clientSecret
        self.api = api
        self.cacheHandler = api.cacheHandler

        self.authUrl = config.AUTH_URL
        self.tokenUrl = config.ACCESS_TOKEN_URL
        self.redirectUri = None

        self.state = None
        self.oauthToken = None
        self.token = None
        self.refreshToken = None
        self.expiresOn = 9999999999999

        self.initParams()

    def initParams(self):

        # Check if we already have tokens stored in cache
        # If so, put them in the right variables

        cacheContent = self.cacheHandler.getCache(self.clientId)
        if cacheContent:
            self.token = cacheContent['token']
            self.refreshToken = cacheContent['refreshToken']
            self.expiresOn = cacheContent['expiresOn']

            # Check if token hasnt already expired
            if not self.isTokenDueRenewal():
                self.setTokenHeader(self.token)
            else:
                self.acquireNewToken()

    def isTokenDueRenewal(self):
        currTime = int(time.time())
        if currTime > (self.expiresOn - 30): return True
        return False

    def getAuthURL(self, redirectUri):
        self.redirectUri = redirectUri

        oauth = OAuth2Session(self.clientId, redirect_uri=self.redirectUri)
        authorizationUrl, self.state = oauth.authorization_url(self.authUrl)
        return authorizationUrl

    def tokenSaver(self, oauth):

        self.token = oauth._client.access_token
        self.refreshToken = oauth._client.refresh_token
        self.expiresOn = int(time.time() + float(oauth._client.expires_in))

        cacheContent = { 'token' : self.token, 'refreshToken' : self.refreshToken, 'expiresOn' : self.expiresOn }

        self.cacheHandler.setCache(self.clientId, cacheContent)
        self.setTokenHeader(self.token)

        return self.token
    
    def retrieveToken(self, response, state=None, redirectUri=None):
        if not redirectUri: 
            if not self.redirectUri: raise NotFoundError('redirect uri is not found. init the auth flow first or give the uri as a parameter.')
            redirectUri = self.redirectUri
        
        if not state: 
            if not self.state: raise NotFoundError('state is not found. init the auth flow first or give the state as a parameter.')
            state = self.state

        oauth = OAuth2Session(self.clientId, state=state, redirect_uri=redirectUri)
        self.oauthToken = oauth.fetch_token(self.tokenUrl, client_secret=self.clientSecret, authorization_response=response)

        token = self.tokenSaver(oauth)

        return token
    
    def acquireNewToken(self):

        tempToken = {
            'access_token' : self.token,
            'refresh_token' : self.refreshToken,
            'token_type' : 'Bearer',
            'expires_in' : '-30'
        }

        oauth = OAuth2Session(self.clientId, token=tempToken)
        self.oauthToken = oauth.refresh_token(self.tokenUrl, client_id=self.clientId, client_secret=self.clientSecret)

        token = self.tokenSaver(oauth)

        return token
    
    def getToken(self):

        if self.token: return self.token
        raise NotFoundError('token is not found. init the auth flow first.')
    
    def setTokenHeader(self, token):
        bearerStr = 'Bearer {token}'.format(token=token)
        self.api.headers.update({'Authorization' : bearerStr})
    
    def checkHeaderTokens(self):

        # Check if token is due for renewal
        if self.isTokenDueRenewal():
            token = self.acquireNewToken()

        # If no authorization header is found, we need to include the token
        if 'Authorization' not in self.api.headers:
            
            # Check if we have a token stored in cache, if not, acquire one
            # If we do, set it in the header
            cacheContent = self.cacheHandler.getCache(self.clientId)
            token = cacheContent['token'] if cacheContent else None

            if token is None: token = self.getToken()
            self.setTokenHeader(token)