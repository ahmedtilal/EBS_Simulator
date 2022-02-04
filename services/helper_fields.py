help_fields = {
        "applicationId" : "Unique Application Identifier provided to each application provider ",
        "UUID" : "Universally Unique Identifier. This field should be sent with every request and is unique per request. Example “1e056384-625a-43ba-9876-6ddd7d9a5d51”",
        "tranDateTime" : "This field should be sent with every request to indicate the transaction date and time.",
        "entityID" : """Used as a unique Id for the user and its’ value depends on the entityType, e.g.: “entityType”: "Phone No"
            “entityId”: “249123123456”
            """,
        "entityType" : """The type of entity used to authenticate the customer for non-PAN-based transactions, available values are:
            "Phone No", "Meter No", "Credit Card", “Cash Card” and “Mobile Wallet”
            Mobile Wallet: represents a customer account in the Mobile Payment system. This is only available through ‘Payment’ and ‘Service Payment’ services
            """,
        "entityGroup" : """1- allow this entity to be used with all channels
            0- use registered entity with this channel only
            The value is currently ignored 
            """,
        "userName" : "User name that is linked with a registered card.",
        "userPassword" : """Encrypted user password See Appendix C: Encryption for how to encrypt. It is used in financial requests to authenticate the customer, and is used in registration service as the desired password.""",
        "phoneNo" : "Customer phone number, used in registration authentication and for financial transactions notification.  In registration using physical cards, the phone number has to be the phone number linked with the card.",
        "financialInstitutionId" : """FID (Bank short name) to register the customer with i.e. give the customer a card that is issued by that bank.
            e.g. “financialInstitutionId”:”FARC” 
            """,
        "PAN" : "Primary Account Number of the customer card",
        "IPIN" : """Encrypted IPIN block. See Appendix C: Encryption for how to encrypt. 
            Used in financial requests to authenticate the customer
            """,
        "mbr" : """The card member (Number of times that the card got reissued). Will be 0 for new Cards and increases by 1 every time they are reissued. Current mbr value is usually printed on the physical card. 
            The field is optional for most transactions, and the exact card can be identified by the system using PAN and expDate, if the card is not issued twice within the same month (same expDate)
            """,
        "expDate" : "Card expiry date.",
        "panCategory" : """1-Standard , 2- Silver, 3- Golden, 4- Silver Agent 5- Golden Agent
            e.g.:
            "panCategory":"Golden Agent"
            """,
        "registrationType" : "Registration type requested by the customer, Valid registration types are 01, 12, 10",
        "fullName" : """Full Customer Name.""",
        "dateOfBirth" : """Date of birth. Should be sent in registration requests as part of the KYC data, Format: dd-mm-yyyy
            e.g. "dateOfBirth":"07-07-1976"
            """,
        "customerIdNumber" : """Identification number. Should be sent in registration requests as part of the KYC data.
            e.g. "customerIdNumber":"P01234658"
            """, 
        "customerIdType" : """Identification type. Should be sent in registration requests as part of the KYC data.
            Values: National ID
                    Passport
                    Driving License
                    e.g. “customerIdType”:”Driving License”
            """,
        "bankAccountNumber" : """Customer bank account number. Should be sent in registration requests as part of the KYC data.
            e.g. "bankAccountNumber":"22000588487"
            """,
        "bankAccountType" : """Customer Bank Account Type. Should be sent in registration requests as part of the KYC data, Types:
            Checking
            Savings
            Credit
            Bonus
            e.g. "bankAccountType":"Savings".
            """,
        "bankBranchId" : """Customer Bank Branch Id. Should be sent in registration requests as part of the KYC data.
            e.g. "bankBranchId":"102"
            """,
        "job" : "Customer's job title. Should be sent in registration requests as part of the KYC data.",
        "email" : "Customer email, can be used for authentication and notification",
        "extraInfo" : "See Appendix F: Extra Info",
        }