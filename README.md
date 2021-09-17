# python-exact-online
Basic wrapper for the Exact Online REST API (v1)

## Limitations
Only functionalities that I need are worked out. No intention to develop any further.

# Getting started

### Install

Install with pip.

```python
pip install python-exact-online
```

### Import

Import the package and the ExactOnlineAPI.

```python
from exactonline.api import ExactOnlineAPI
```

### Setup connection

Make the connection with your provided CLIENTID and CLIENTSECRET.

```python
api = ExactOnlineAPI(CLIENTID, CLIENTSECRET)
```

Exact Online authentication is build on OAuth2. A basic script to obtain your first tokens can be found below. After you've obtained your tokens, the refresh tokens are automatically used to renew the token if needed. No manual action is required after that.

```python
from exactonline.api import ExactOnlineAPI

REDIRECT_URI = 'https://any-url-will-do.com/callback/'

api = ExactOnlineAPI(CLIENTID, CLIENTSECRET)

authUrl = api.authHandler.getAuthURL(REDIRECT_URI)
print('visit url: ', authUrl)

response = input('paste response: ')
token = api.authHandler.retrieveToken(response, redirectUri=REDIRECT_URI)
```

When using the script above, any REDIRECT_URI will do. Simply copy and paste the response URI so the handler can obtain the right tokens. 

!! The Redirect URI has to be registered in your Exact App Center.

# Available functionalities

| Object        | Endpoint | Actions       |
| ------------- | ------------- | ------------- |
| SalesEntry/SalesEntryLine  | salesEntries | List, Get, Filter, Create, Update, Delete |
| Documents/Attachments  | documents | List, Get, Filter, Create, Update, Delete  |
| Journals  | journals | List, Get, Filter, Create, Update, Delete  |
| GLAccounts  | glAccounts | List, Get, Filter, Create, Update, Delete  |
| Accounts  | accounts | List, Get, Filter, Create, Update, Delete  |
| Contacts  | contacts | List, Get, Filter, Create, Update, Delete  |
| VATCodes  | vatCodes | List, Get, Filter, Create, Update, Delete  |

## Basic setup

The above endpoints can be used together with their actions. The way to use them are similar to each other.
The examples below are used with the 'accounts' endpoint. Replace them with their respective endpoints in the table above to call other objects.

### List

```python
accounts = api.accounts.list()

for account in accounts.items():
    print(account.ID, account.Name)
```

### Get
```python
accounts = api.accounts.get('uid')
```

Specific fields can be selected while using the get function. This function takes an optional array which contains the fields that need to be returned.

```python
accounts = api.accounts.get('uid', select=['Name', 'Email'])
```

### Filter

Filter on field and value. Returns a list always.

```python
accounts = api.accounts.filter('Email', 'test@test.com')

for account in accounts.items():
    print(account.ID, account.Name)
```

This function also supports the optional select parameter.

```python
accounts = api.accounts.filter('Email', 'test@test.com', select=['Name', 'Email'])
```

### Create

Before creating an object in Exact Online, you need to create the object within Python itself.

```python
account = Account(
    Name='New Account',
    Status='C'
)

exactAccount = api.accounts.create(account)
```

### Update

You can retrieve an object, update its attributes and then push it back to Exact Online.

```python
account = api.accounts.get('uid')
account.Name = 'Updated Account'
api.account.update(acc)
```

Returns True if succeeded.

### Delete
```python
accounts = api.accounts.delete('uid')
```

Returns True if succeeded.


## Creating documents

Creating documents has a slightly different approach, because it allows you to also upload files directly to Exact, linked to the document. Multiple files are supported.

```python
doc = Document(
    Account='uid',
    Type=10,
    Subject='New Document',
)

exactDocument = api.documents.create(doc, ['/path/to/pdf/file.pdf'])
```

## Creating sales entries

When creating sales entries, the corresponding sales lines are expected to be given as well.

```python
salesEntry = SalesEntry(
    Customer='uid',
    Journal='700',
    YourRef='MyREF',
)

lines = SalesEntryLineList()
line1 = SalesEntryLine(AmountFC=100, GLAccount='uid')
line2 = SalesEntryLine(AmountFC=150, GLAccount='uid')

lines.add(line1)
lines.add(line2)

salesEntry.SalesEntryLines = lines

exactEntry = api.salesEntries.create(salesEntry)

print(exactEntry.EntryID, exactEntry.InvoiceNumber, exactEntry.AmountDC)
```

## Retrieving VATPercentages

VATCodes have VATPercentages linked to them. By default, these percentages are not given when requesting a list of VAT Codes.

```python
vatCodes = api.vatCodes.list()

for entry in vatCodes.items():
    for perc in entry.VATPercentages.items():
        # This will contain an empty VATPercentage object
        print(vars(perc))
```

To get the VATPercentages for a VATCode, you need to make a new GET request for that specific VATCode. You can then loop over all the available percentages.

```python
entry = api.vatCodes.get(UID)

for perc in entry.VATPercentages.items():
    print(vars(perc))
```

## Error handling

Basic error handling has been added.
You can check if an error has occured during a call by checking the hasError attribute on the object.
If the hasError attribute has been set to True, an Error object will be attached to the error attribute of the same object.
The Error object contains two attributes: code and message. Usually code will be empty. Message is the error message.

```python
account = api.accounts.get('uid')

if account.hasError:
    print(account.error.message)
else:
    print(account.ID)
```

## Documentation

Find the official Exact Online documentation here: https://start.exactonline.nl/docs/HlpRestAPIResources.aspx?SourceAction=10

You can find what is expected and required for each call.