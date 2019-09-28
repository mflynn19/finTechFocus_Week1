#important keys are name, phone, email, company, address
class Contact:
    def __init__(self, name, phone, email, company, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.company = company
        self.address = address
        
shwetaContact = Contact("Shweta", 2123456789, "shweta@gmail.com", "Goldman Sachs", "123 Main Street Small Town, NJ")
print(shwetaContact.name)