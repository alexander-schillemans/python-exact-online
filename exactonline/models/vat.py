from .base import ObjectListModel, BaseModel

class VATPercentageList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=VATPercentage)
    

class VATPercentage(BaseModel):

    def __init__(self,
        ID=None,
        VATCodeID=None,
        Type=None,
        StartDate=None,
        Percentage=None,
        ModifierFullName=None,
        Modifier=None,
        Modified=None,
        LineNumber=None,
        EndDate=None,
        Division=None,
        CreatorFullName=None,
        Creator=None,
        Created=None
    ):

        super().__init__()

        self.ID = ID
        self.VATCodeID = VATCodeID
        self.Type = Type
        self.StartDate = StartDate
        self.Percentage = Percentage
        self.ModifierFullName = ModifierFullName
        self.Modifier = Modifier
        self.Modified = Modified
        self.LineNumber = LineNumber
        self.EndDate = EndDate
        self.Division = Division
        self.CreatorFullName = CreatorFullName
        self.Creator = Creator
        self.Created = Created

class VATCodeList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=VATCode)

class VATCode(BaseModel):

    def __init__(self,
        ID=None,
        Account=None,
        AccountCode=None,
        AccountName=None,
        CalculationBasis=None,
        Charged=None,
        Code=None,
        Country=None,
        Created=None,
        Creator=None,
        CreatorFullName=None,
        Description=None,
        Division=None,
        EUSalesListing=None,
        GLDiscountPurchase=None,
        GLDiscountPurchaseCode=None,
        GLDiscountPurchaseDescription=None,
        GLDiscountSales=None,
        GLDiscountSalesCode=None,
        GLDiscountSalesDescription=None,
        GLToClaim=None,
        GLToClaimCode=None,
        GLToClaimDescription=None,
        GLToPay=None,
        GLToPayCode=None,
        GLToPayDescription=None,
        IntraStat=None,
        IntrastatType=None,
        IsBlocked=None,
        LegalText=None,
        Modified=None,
        Modifier=None,
        ModifierFullName=None,
        OssCountry=None,
        Percentage=None,
        TaxReturnType=None,
        Type=None,
        VatDocType=None,
        VatMargin=None,
        VATPartialRatio=None,
        VATPercentages=None,
        VATTransactionType=None
    ):

        super().__init__()

        self.ID = ID
        self.Account = Account
        self.AccountCode = AccountCode
        self.AccountName = AccountName
        self.CalculationBasis = CalculationBasis
        self.Charged = Charged
        self.Code = Code
        self.Country = Country
        self.Created = Created
        self.Creator = Creator
        self.CreatorFullName = CreatorFullName
        self.Description = Description
        self.Division = Division
        self.EUSalesListing = EUSalesListing
        self.GLDiscountPurchase = GLDiscountPurchase
        self.GLDiscountPurchaseCode = GLDiscountPurchaseCode
        self.GLDiscountPurchaseDescription = GLDiscountPurchaseDescription
        self.GLDiscountSales = GLDiscountSales
        self.GLDiscountSalesCode = GLDiscountSalesCode
        self.GLDiscountSalesDescription = GLDiscountSalesDescription
        self.GLToClaim = GLToClaim
        self.GLToClaimCode = GLToClaimCode
        self.GLToClaimDescription = GLToClaimDescription
        self.GLToPay = GLToPay
        self.GLToPayCode = GLToPayCode
        self.GLToPayDescription = GLToPayDescription
        self.IntraStat = IntraStat
        self.IntrastatType = IntrastatType
        self.IsBlocked = IsBlocked
        self.LegalText = LegalText
        self.Modified = Modified
        self.Modifier = Modifier
        self.ModifierFullName = ModifierFullName
        self.OssCountry = OssCountry
        self.Percentage = Percentage
        self.TaxReturnType = TaxReturnType
        self.Type = Type
        self.VatDocType = VatDocType
        self.VatMargin = VatMargin
        self.VATPartialRatio = VATPartialRatio
        self.VATPercentages = VATPercentages if VATPercentages else VATPercentageList()
        self.VATTransactionType = VATTransactionType