class User:
    all_users = []
    total_users = 0
    def __init__(self, username, first_name, last_name, dob, email, license_num=None): #first_name, last_name, dob, email, license_num=None
        User.total_users += 1
        self.set_username = username
        User.all_users.append(self)
        self.set_first_name = first_name
        self.set_last_name = last_name
        self.set_dob = dob
        self.set_email = email
        self.set_license_num = license_num
    
    def __str__(self):
        return f'\n{self.get_username}: {self.get_full_name} born on {self.get_dob} their email is {self.get_email} and their license number is {self.get_license_num}.'
    
    def __repr__(self):
        return str(self)
    
    @property
    def get_username(self):
        return self._username
    
    @get_username.setter
    def set_username(self, new_username):
        if isinstance(new_username, str):
            if new_username not in User.all_users:
                self._username = new_username
            else: 
                print('Username taken. Try again')
        else:
            print('Username must be a string.')
    
    @property
    def get_first_name(self):
        return self._first_name
    
    @get_first_name.setter
    def set_first_name(self, new_name):
        if isinstance(new_name, str):
            self._first_name = new_name.capitalize()
        else:
            print('Name must be a string.')
            
    @property
    def get_last_name(self):
        return self._last_name
    
    @get_last_name.setter
    def set_last_name(self, new_name):
        if isinstance(new_name, str):
            self._last_name = new_name.capitalize()
        else:
            print('Name must be a string.')
            
    @property
    def get_full_name(self):
        self._full_name = f"{self.get_first_name} {self.get_last_name}"
        return self._full_name
    
    @property
    def get_dob(self):
        return self._dob
    
    @get_dob.setter
    def set_dob(self, birthday):
        if isinstance(birthday, str):
            self._dob = birthday.capitalize()
        else:
            print('Date of birth must be a string.')
    
    @property 
    def get_email(self):
        return self._email
    
    @get_email.setter
    def set_email(self, new_email):
        if isinstance(new_email, str):
            self._email = new_email
        else:
            print('Email must be a string.')
    
    @property
    def get_license_num(self):
        return self._license_num
    
    @get_license_num.setter
    def set_license_num(self, num):
        if isinstance(num, int) or num is None:
            self._license_num = num
        else:
            print('License number must be an integer or None.')

user1 = User('ringbearer', 'frodo', 'baggins', 'september 22nd','frodobaggins@hotmail.com', 1234567890)
user2 = User('gamgeegardens', 'samwise', 'gamgee', 'april 6th', 'samwise.gamgee@gmail.com') 
print('all users:', User.all_users)
