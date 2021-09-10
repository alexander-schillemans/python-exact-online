from .base import ObjectListModel, BaseModel

class ContactList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=Contact)

class Contact(BaseModel):

    def __init__(self,
        ID=None,
        Account=None,
        AccountIsCustomer=None,
        AccountIsSupplier=None,
        AccountMainContact=None,
        AccountName=None,
        AddressLine2=None,
        AddressStreet=None,
        AddressStreetNumber=None,
        AddressStreetNumberSuffix=None,
        AllowMailing=None,
        BirthDate=None,
        BirthName=None,
        BirthNamePrefix=None,
        BirthPlace=None,
        BusinessEmail=None,
        BusinessFax=None,
        BusinessMobile=None,
        BusinessPhone=None,
        BusinessPhoneExtension=None,
        City=None,
        Code=None,
        Country=None,
        Created=None,
        Creator=None,
        CreatorFullName=None,
        Division=None,
        Email=None,
        EndDate=None,
        FirstName=None,
        FullName=None,
        Gender=None,
        HID=None,
        IdentificationDate=None,
        IdentificationDocument=None,
        IdentificationUser=None,
        Initials=None,
        IsAnonymised=None,
        IsMailingExcluded=None,
        IsMainContact=None,
        JobTitleDescription=None,
        Language=None,
        LastName=None,
        LeadPurpose=None,
        LeadSource=None,
        MarketingNotes=None,
        MiddleName=None,
        Mobile=None,
        Modified=None,
        Modifier=None,
        ModifierFullName=None,
        Nationality=None,
        Notes=None,
        PartnerName=None,
        PartnerNamePrefix=None,
        Person=None,
        Phone=None,
        PhoneExtension=None,
        Picture=None,
        PictureName=None,
        PictureThumbnailUrl=None,
        PictureUrl=None,
        Postcode=None,
        SocialSecurityNumber=None,
        StartDate=None,
        State=None,
        Title=None
    ):

        super().__init__()
        
        self.ID = ID
        self.Account = Account
        self.AccountIsCustomer = AccountIsCustomer
        self.AccountIsSupplier = AccountIsSupplier
        self.AccountMainContact = AccountMainContact
        self.AccountName = AccountName
        self.AddressLine2 = AddressLine2
        self.AddressStreet = AddressStreet
        self.AddressStreetNumber = AddressStreetNumber
        self.AddressStreetNumberSuffix = AddressStreetNumberSuffix
        self.AllowMailing = AllowMailing
        self.BirthDate = BirthDate
        self.BirthName = BirthName
        self.BirthNamePrefix = BirthNamePrefix
        self.BirthPlace = BirthPlace
        self.BusinessEmail = BusinessEmail
        self.BusinessFax = BusinessFax
        self.BusinessMobile = BusinessMobile
        self.BusinessPhone = BusinessPhone
        self.BusinessPhoneExtension = BusinessPhoneExtension
        self.City = City
        self.Code = Code
        self.Country = Country
        self.Created = Created
        self.Creator = Creator
        self.CreatorFullName = CreatorFullName
        self.Division = Division
        self.Email = Email
        self.EndDate = EndDate
        self.FirstName = FirstName
        self.FullName = FullName
        self.Gender = Gender
        self.HID = HID
        self.IdentificationDate = IdentificationDate
        self.IdentificationDocument = IdentificationDocument
        self.IdentificationUser = IdentificationUser
        self.Initials = Initials
        self.IsAnonymised = IsAnonymised
        self.IsMailingExcluded = IsMailingExcluded
        self.IsMainContact = IsMainContact
        self.JobTitleDescription = JobTitleDescription
        self.Language = Language
        self.LastName = LastName
        self.LeadPurpose = LeadPurpose
        self.LeadSource = LeadSource
        self.MarketingNotes = MarketingNotes
        self.MiddleName = MiddleName
        self.Mobile = Mobile
        self.Modified = Modified
        self.Modifier = Modifier
        self.ModifierFullName = ModifierFullName
        self.Nationality = Nationality
        self.Notes = Notes
        self.PartnerName = PartnerName
        self.PartnerNamePrefix = PartnerNamePrefix
        self.Person = Person
        self.Phone = Phone
        self.PhoneExtension = PhoneExtension
        self.Picture = Picture
        self.PictureName = PictureName
        self.PictureThumbnailUrl = PictureThumbnailUrl
        self.PictureUrl = PictureUrl
        self.Postcode = Postcode
        self.SocialSecurityNumber = SocialSecurityNumber
        self.StartDate = StartDate
        self.State = State
        self.Title = Title