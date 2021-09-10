from .base import ObjectListModel, BaseModel

class JournalList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=Journal)

class Journal(BaseModel):

    def __init__(self,
        ID=None,
        AllowVariableCurrency=None,
        AllowVariableExchangeRate=None,
        AllowVAT=None,
        AutoSave=None,
        Bank=None,
        BankAccountBICCode=None,
        BankAccountCountry=None,
        BankAccountDescription=None,
        BankAccountIBAN=None,
        BankAccountID=None,
        BankAccountIncludingMask=None,
        BankAccountUseSEPA=None,
        BankAccountUseSepaDirectDebit=None,
        BankName=None,
        Code=None,
        Created=None,
        Creator=None,
        CreatorFullName=None,
        Currency=None,
        CurrencyDescription=None,
        Description=None,
        Division=None,
        GLAccount=None,
        GLAccountCode=None,
        GLAccountDescription=None,
        GLAccountType=None,
        IsBlocked=None,
        Modified=None,
        Modifier=None,
        ModifierFullName=None,
        PaymentInTransitAccount=None,
        PaymentServiceAccountIdentifier=None,
        PaymentServiceProvider=None,
        PaymentServiceProviderName=None,
        Type=None
    ):

        super().__init__()

        self.ID = ID
        self.AllowVariableCurrency = AllowVariableCurrency
        self.AllowVariableExchangeRate = AllowVariableExchangeRate
        self.AllowVAT = AllowVAT
        self.AutoSave = AutoSave
        self.Bank = Bank
        self.BankAccountBICCode = BankAccountBICCode
        self.BankAccountCountry = BankAccountCountry
        self.BankAccountDescription = BankAccountDescription
        self.BankAccountIBAN = BankAccountIBAN
        self.BankAccountID = BankAccountID
        self.BankAccountIncludingMask = BankAccountIncludingMask
        self.BankAccountUseSEPA = BankAccountUseSEPA
        self.BankAccountUseSepaDirectDebit = BankAccountUseSepaDirectDebit
        self.BankName = BankName
        self.Code = Code
        self.Created = Created
        self.Creator = Creator
        self.CreatorFullName = CreatorFullName
        self.Currency = Currency
        self.CurrencyDescription = CurrencyDescription
        self.Description = Description
        self.Division = Division
        self.GLAccount = GLAccount
        self.GLAccountCode = GLAccountCode
        self.GLAccountDescription = GLAccountDescription
        self.GLAccountType = GLAccountType
        self.IsBlocked = IsBlocked
        self.Modified = Modified
        self.Modifier = Modifier
        self.ModifierFullName = ModifierFullName
        self.PaymentInTransitAccount = PaymentInTransitAccount
        self.PaymentServiceAccountIdentifier = PaymentServiceAccountIdentifier
        self.PaymentServiceProvider = PaymentServiceProvider
        self.PaymentServiceProviderName = PaymentServiceProviderName
        self.Type = Type