from .base import ObjectListModel, BaseModel

class GLAccountList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=GLAccount)

class GLAccount(BaseModel):

    def __init__(self,
        ID=None,
        AssimilatedVATBox=None,
        BalanceSide=None,
        BalanceType=None,
        BelcotaxType=None,
        Code=None,
        Compress=None,
        Costcenter=None,
        CostcenterDescription=None,
        Costunit=None,
        CostunitDescription=None,
        Created=None,
        Creator=None,
        CreatorFullName=None,
        DeductibilityPercentages=None,
        Description=None,
        Division=None,
        ExcludeVATListing=None,
        ExpenseNonDeductiblePercentage=None,
        IsBlocked=None,
        Matching=None,
        Modified=None,
        Modifier=None,
        ModifierFullName=None,
        PrivateGLAcount=None,
        PrivatePercentage=None,
        ReportingCode=None,
        RevalueCurrency=None,
        SearchCode=None,
        Type=None,
        TypeDescription=None,
        UseCostcenter=None,
        UseCostunit=None,
        VATCode=None,
        VATDescription=None,
        VATGLAccountType=None,
        VATNonDeductibleGLAccount=None,
        VATNonDeductiblePercentage=None,
        VATSystem=None,
        YearEndCostGLAccount=None,
        YearEndReflectionGLAccount=None
    ):

        super().__init__()

        self.ID = ID
        self.AssimilatedVATBox = AssimilatedVATBox
        self.BalanceSide = BalanceSide
        self.BalanceType = BalanceType
        self.BelcotaxType = BelcotaxType
        self.Code = Code
        self.Compress = Compress
        self.Costcenter = Costcenter
        self.CostcenterDescription = CostcenterDescription
        self.Costunit = Costunit
        self.CostunitDescription = CostunitDescription
        self.Created = Created
        self.Creator = Creator
        self.CreatorFullName = CreatorFullName
        self.DeductibilityPercentages = DeductibilityPercentages
        self.Description = Description
        self.Division = Division
        self.ExcludeVATListing = ExcludeVATListing
        self.ExpenseNonDeductiblePercentage = ExpenseNonDeductiblePercentage
        self.IsBlocked = IsBlocked
        self.Matching = Matching
        self.Modified = Modified
        self.Modifier = Modifier
        self.ModifierFullName = ModifierFullName
        self.PrivateGLAcount = PrivateGLAcount
        self.PrivatePercentage = PrivatePercentage
        self.ReportingCode = ReportingCode
        self.RevalueCurrency = RevalueCurrency
        self.SearchCode = SearchCode
        self.Type = Type
        self.TypeDescription = TypeDescription
        self.UseCostcenter = UseCostcenter
        self.UseCostunit = UseCostunit
        self.VATCode = VATCode
        self.VATDescription = VATDescription
        self.VATGLAccountType = VATGLAccountType
        self.VATNonDeductibleGLAccount = VATNonDeductibleGLAccount
        self.VATNonDeductiblePercentage = VATNonDeductiblePercentage
        self.VATSystem = VATSystem
        self.YearEndCostGLAccount = YearEndCostGLAccount
        self.YearEndReflectionGLAccount = YearEndReflectionGLAccount