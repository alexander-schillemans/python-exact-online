from .base import ObjectListModel, BaseModel

class SalesEntryList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=SalesEntry)
    

class SalesEntry(BaseModel):

    def __init__(self,
        EntryID=None,
        AmountDC=None,
        AmountFC=None,
        BatchNumber=None,
        Created=None,
        Creator=None,
        CreatorFullName=None,
        Currency=None,
        Customer=None,
        CustomerName=None,
        Description=None,
        Division=None,
        Document=None,
        DocumentNumber=None,
        DocumentSubject=None,
        DueDate=None,
        EntryDate=None,
        EntryNumber=None,
        ExternalLinkDescription=None,
        ExternalLinkReference=None,
        GAccountAmountFC=None,
        InvoiceNumber=None,
        IsExtraDuty=None,
        Journal=None,
        JournalDescription=None,
        Modified=None,
        Modifier=None,
        ModifierFullName=None,
        OrderNumber=None,
        PaymentCondition=None,
        PaymentConditionDescription=None,
        PaymentReference=None,
        ProcessNumber=None,
        Rate=None,
        ReportingPeriod=None,
        ReportingYear=None,
        Reversal=None,
        SalesEntryLines=None,
        Status=None,
        StatusDescription=None,
        Type=None,
        TypeDescription=None,
        VATAmountDC=None,
        VATAmountFC=None,
        WithholdingTaxAmountDC=None,
        WithholdingTaxBaseAmount=None,
        WithholdingTaxPercentage=None,
        YourRef=None
    ):

        super().__init__()

        self.EntryID = EntryID
        self.AmountDC = AmountDC
        self.AmountFC = AmountFC
        self.BatchNumber = BatchNumber
        self.Created = Created
        self.Creator = Creator
        self.CreatorFullName = CreatorFullName
        self.Currency = Currency
        self.Customer = Customer
        self.CustomerName = CustomerName
        self.Description = Description
        self.Division = Division
        self.Document = Document
        self.DocumentNumber = DocumentNumber
        self.DocumentSubject = DocumentSubject
        self.DueDate = DueDate
        self.EntryDate = EntryDate
        self.EntryNumber = EntryNumber
        self.ExternalLinkDescription = ExternalLinkDescription
        self.ExternalLinkReference = ExternalLinkReference
        self.GAccountAmountFC = GAccountAmountFC
        self.InvoiceNumber = InvoiceNumber
        self.IsExtraDuty = IsExtraDuty
        self.Journal = Journal
        self.JournalDescription = JournalDescription
        self.Modified = Modified
        self.Modifier = Modifier
        self.ModifierFullName = ModifierFullName
        self.OrderNumber = OrderNumber
        self.PaymentCondition = PaymentCondition
        self.PaymentConditionDescription = PaymentConditionDescription
        self.PaymentReference = PaymentReference
        self.ProcessNumber = ProcessNumber
        self.Rate = Rate
        self.ReportingPeriod = ReportingPeriod
        self.ReportingYear = ReportingYear
        self.Reversal = Reversal
        self.SalesEntryLines = SalesEntryLines if SalesEntryLines else SalesEntryLineList()
        self.Status = Status
        self.StatusDescription = StatusDescription
        self.Type = Type
        self.TypeDescription = TypeDescription
        self.VATAmountDC = VATAmountDC
        self.VATAmountFC = VATAmountFC
        self.WithholdingTaxAmountDC = WithholdingTaxAmountDC
        self.WithholdingTaxBaseAmount = WithholdingTaxBaseAmount
        self.WithholdingTaxPercentage = WithholdingTaxPercentage
        self.YourRef = YourRef

class SalesEntryLineList(ObjectListModel):
    
    def __init__(self):
        super().__init__(list=[], listObject=SalesEntryLine)

class SalesEntryLine(BaseModel):

    def __init__(self,
        ID=None,
        AmountFC=None,
        Asset=None,
        AssetDescription=None,
        CostCenter=None,
        CostCenterDescription=None,
        CostUnit=None,
        CostUnitDescription=None,
        Description=None,
        Division=None,
        EntryID=None,
        ExtraDutyAmountFC=None,
        ExtraDutyPercentage=None,
        From=None,
        GLAccount=None,
        GLAccountCode=None,
        GLAccountDescription=None,
        IntraStatArea=None,
        IntraStatCountry=None,
        IntraStatDeliveryTerm=None,
        IntraStatTransactionA=None,
        IntraStatTransactionB=None,
        IntraStatTransportMethod=None,
        LineNumber=None,
        Notes=None,
        Project=None,
        ProjectDescription=None,
        Quantity=None,
        SerialNumber=None,
        StatisticalNetWeight=None,
        StatisticalNumber=None,
        StatisticalQuantity=None,
        StatisticalValue=None,
        Subscription=None,
        SubscriptionDescription=None,
        TaxSchedule=None,
        To=None,
        TrackingNumber=None,
        TrackingNumberDescription=None,
        Type=None,
        VATAmountDC=None,
        VATAmountFC=None,
        VATBaseAmountDC=None,
        VATBaseAmountFC=None,
        VATCode=None,
        VATCodeDescription=None,
        VATPercentage=None
    ):

        super().__init__()

        self.ID = ID
        self.AmountFC = AmountFC
        self.Asset = Asset
        self.AssetDescription = AssetDescription
        self.CostCenter = CostCenter
        self.CostCenterDescription = CostCenterDescription
        self.CostUnit = CostUnit
        self.CostUnitDescription = CostUnitDescription
        self.Description = Description
        self.Division = Division
        self.EntryID = EntryID
        self.ExtraDutyAmountFC = ExtraDutyAmountFC
        self.ExtraDutyPercentage = ExtraDutyPercentage
        self.From = From
        self.GLAccount = GLAccount
        self.GLAccountCode = GLAccountCode
        self.GLAccountDescription = GLAccountDescription
        self.IntraStatArea = IntraStatArea
        self.IntraStatCountry = IntraStatCountry
        self.IntraStatDeliveryTerm = IntraStatDeliveryTerm
        self.IntraStatTransactionA = IntraStatTransactionA
        self.IntraStatTransactionB = IntraStatTransactionB
        self.IntraStatTransportMethod = IntraStatTransportMethod
        self.LineNumber = LineNumber
        self.Notes = Notes
        self.Project = Project
        self.ProjectDescription = ProjectDescription
        self.Quantity = Quantity
        self.SerialNumber = SerialNumber
        self.StatisticalNetWeight = StatisticalNetWeight
        self.StatisticalNumber = StatisticalNumber
        self.StatisticalQuantity = StatisticalQuantity
        self.StatisticalValue = StatisticalValue
        self.Subscription = Subscription
        self.SubscriptionDescription = SubscriptionDescription
        self.TaxSchedule = TaxSchedule
        self.To = To
        self.TrackingNumber = TrackingNumber
        self.TrackingNumberDescription = TrackingNumberDescription
        self.Type = Type
        self.VATAmountDC = VATAmountDC
        self.VATAmountFC = VATAmountFC
        self.VATBaseAmountDC = VATBaseAmountDC
        self.VATBaseAmountFC = VATBaseAmountFC
        self.VATCode = VATCode
        self.VATCodeDescription = VATCodeDescription
        self.VATPercentage = VATPercentage