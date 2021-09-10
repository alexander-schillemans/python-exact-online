from .base import ObjectListModel, BaseModel

class DocumentList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=Document)

class Document(BaseModel):

    def __init__(self,
        ID=None,
        Account=None,
        AccountCode=None,
        AccountName=None,
        AmountFC=None,
        Body=None,
        Category=None,
        CategoryDescription=None,
        Contact=None,
        ContactFullName=None,
        Created=None,
        Creator=None,
        CreatorFullName=None,
        Currency=None,
        Division=None,
        DocumentDate=None,
        DocumentFolder=None,
        DocumentFolderCode=None,
        DocumentFolderDescription=None,
        DocumentViewUrl=None,
        ExpiryDate=None,
        FinancialTransactionEntryID=None,
        HasEmptyBody=None,
        HID=None,
        Language=None,
        Modified=None,
        Modifier=None,
        ModifierFullName=None,
        Opportunity=None,
        Project=None,
        ProjectCode=None,
        ProjectDescription=None,
        SalesInvoiceNumber=None,
        SalesOrderNumber=None,
        SendMethod=None,
        ShopOrderNumber=None,
        Subject=None,
        Type=None,
        TypeDescription=None,
        Attachments=None
    ):

        super().__init__()

        self.ID = ID
        self.Account = Account
        self.AccountCode = AccountCode
        self.AccountName = AccountName
        self.AmountFC = AmountFC
        self.Body = Body
        self.Category = Category
        self.CategoryDescription = CategoryDescription
        self.Contact = Contact
        self.ContactFullName = ContactFullName
        self.Created = Created
        self.Creator = Creator
        self.CreatorFullName = CreatorFullName
        self.Currency = Currency
        self.Division = Division
        self.DocumentDate = DocumentDate
        self.DocumentFolder = DocumentFolder
        self.DocumentFolderCode = DocumentFolderCode
        self.DocumentFolderDescription = DocumentFolderDescription
        self.DocumentViewUrl = DocumentViewUrl
        self.ExpiryDate = ExpiryDate
        self.FinancialTransactionEntryID = FinancialTransactionEntryID
        self.HasEmptyBody = HasEmptyBody
        self.HID = HID
        self.Language = Language
        self.Modified = Modified
        self.Modifier = Modifier
        self.ModifierFullName = ModifierFullName
        self.Opportunity = Opportunity
        self.Project = Project
        self.ProjectCode = ProjectCode
        self.ProjectDescription = ProjectDescription
        self.SalesInvoiceNumber = SalesInvoiceNumber
        self.SalesOrderNumber = SalesOrderNumber
        self.SendMethod = SendMethod
        self.ShopOrderNumber = ShopOrderNumber
        self.Subject = Subject
        self.Type = Type
        self.TypeDescription = TypeDescription
        self.Attachments = Attachments if Attachments else DocumentAttachmentList()

class DocumentAttachmentList(ObjectListModel):
    def __init__(self):
        super().__init__(list=[], listObject=DocumentAttachment)

class DocumentAttachment(BaseModel):

    def __init__(self,
        ID=None,
        Attachment=None,
        Document=None,
        FileName=None,
        FileSize=None,
        Url=None,
    ):

        self.ID = ID
        self.Attachment = Attachment
        self.Document = Document
        self.FileName = FileName
        self.FileSize = FileSize
        self.Url = Url

class DocumentTypeList(ObjectListModel):
    def __init__(self):
        super().__init__(list=[], listObject=DocumentType)

class DocumentType(BaseModel):

    def __init__(self,
        ID=None,
        Description=None,
        DocumentIsCreatable=None,
        DocumentIsDeletable=None,
        DocumentIsUpdatable=None,
        DocumentIsViewable=None,
        Modified=None,
        TypeCategory=None
    ):


        self.ID = ID
        self.Description = Description
        self.DocumentIsCreatable = DocumentIsCreatable
        self.DocumentIsDeletable = DocumentIsDeletable
        self.DocumentIsUpdatable = DocumentIsUpdatable
        self.DocumentIsViewable = DocumentIsViewable
        self.Modified = Modified
        self.TypeCategory = TypeCategory


class DocumentTypeCategoryList(ObjectListModel):
    def __init__(self):
        super().__init__(list=[], listObject=DocumentTypeCategory)


class DocumentTypeCategory(BaseModel):

    def __init__(self,
        ID=None,
        Created=None,
        Description=None,
        Modified=None
    ):

        self.ID = ID
        self.Created = Created
        self.Description = Description
        self.Modified = Modified