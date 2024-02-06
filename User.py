class User:
    def __init__(self, name, email, license_num):
        self.name = name
        self.email = email
        self.license_num = license_num


mia = User('Mia Johnson', 'miajohnson@gmail.com', '233761131483')
alex = User('Alex Rodriguez', 'alexrodriguez@yahoo.com', '630508017326')
emily = User('Emily Chen', 'emilychen@outlook.com', '666048983857')
marcus = User('Marcus Thompson', 'marcusthompson@icloud.com', '182710058534')

print(mia.email)
print(alex.email)
print(emily.email)
print(marcus.email)