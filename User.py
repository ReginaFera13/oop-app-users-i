class User:
    def __init__(self, first_name, last_name, dob, email, license_num=None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.license_num = license_num
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        


mia = User('Mia', 'Johnson', '3 March 1987', 'miajohnson@gmail.com', '233761131483')
alex = User('Alex', 'Rodriguez', '24 January 1976', 'alexrodriguez@yahoo.com', '630508017326')
emily = User('Emily', 'Chen', '27 June 1999', 'emilychen@outlook.com')
marcus = User('Marcus', 'Thompson', '11 August 1967', 'marcusthompson@icloud.com', '182710058534')

print(mia.full_name())
print(mia.email)
print(alex.full_name())
print(alex.email)
print(emily.full_name())
print(emily.email)
print(marcus.full_name())
print(marcus.email)
