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

## Available functionalities

| Object        | Endpoint | Actions       |
| ------------- | ------------- | ------------- |
| SalesEntry/SalesEntryLine  | salesEntries | List, Get, Filter, Create, Update, Delete |
| Documents/Attachments  | documents | List, Get, Filter, Create, Update, Delete  |
| Journals  | journals | List, Get, Filter, Create, Update, Delete  |
| GLAccounts  | glAccounts | List, Get, Filter, Create, Update, Delete  |
| Accounts  | accounts | List, Get, Filter, Create, Update, Delete  |
| Contacts  | contacts | List, Get, Filter, Create, Update, Delete  |

## Basic setup

The above endpoints can be used together with their actions. The way to use them are similar to each other.
The examples below are used with the 'accounts' endpoint. Replace them with their respective endpoints in the table above to call other objects.

### List
```python
accounts = api.accounts.list()
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