class User:
    all_users = {}
    
    @classmethod
    def load_users_from_app(cls, app):
        cls.all_users = app.users
    
    @classmethod
    def get_user_by_username(cls):
        username = input('Username: ')
        user= cls.all_users.get(username)
        if user is None:
            print('User not found.')
        return user
    
    @classmethod
    def create_user(cls) -> dict:
        pass

    def __init__(self, username, password, first_name, last_name, dob, email, license_num=None): #first_name, last_name, dob, email, license_num=None
        User.total_users = len(User.all_users)
        self.set_username = username
        self.set_password = password
        self.set_first_name = first_name
        self.set_last_name = last_name
        self.set_dob = dob
        self.set_email = email
        self.set_license_num = license_num
    
    def __str__(self):
        return f'\n{self.get_username}: password: {self.get_password}, {self.get_full_name} born on {self.get_dob} their email is {self.get_email} and their license number is {self.get_license_num}.'
    
    def __repr__(self):
        return f'\n{self.get_username}: password: {self.get_password}, {self.get_full_name} born on {self.get_dob} their email is {self.get_email} and their license number is {self.get_license_num}.'
    
    @property
    def get_username(self):
        return self._username
    
    @get_username.setter
    def set_username(self):
        new_username = input('Username: ')
        if isinstance(new_username, str):
            if new_username not in User.all_users:
                self._username = new_username
            else: 
                print('Username taken. Try again')
                return self.set_username()
        else:
            print('Username must be a string.')
            return self.set_username()
    
    @property
    def get_password(self):
        return self._password
    
    @get_password.setter
    def set_password(self):
        new_password = input('Password: ')
        if isinstance(new_password, str):
            self._password = new_password
        else:
            print('Password must be a string.')
            return self.set_password()
    
    # def password_login(self):
    #     auth = False
    #     password = input('Password: ')
    #     if password == self.get_password:
    #         auth = True
    #     return auth
            
    @property
    def get_first_name(self):
        return self._first_name
    
    @get_first_name.setter
    def set_first_name(self):
        new_name = input('First name: ')
        if isinstance(new_name, str):
            self._first_name = new_name.capitalize()
        else:
            print('Name must be a string.')
            return self.set_first_name()
            
    @property
    def get_last_name(self):
        return self._last_name
    
    @get_last_name.setter
    def set_last_name(self):
        new_name = input('Last name: ')
        if isinstance(new_name, str):
            self._last_name = new_name.capitalize()
        else:
            print('Name must be a string.')
            return self.set_last_name()
            
    @property
    def get_full_name(self):
        self._full_name = f"{self.get_first_name} {self.get_last_name}"
        return self._full_name
    
    @property
    def get_dob(self):
        return self._dob
    
    @get_dob.setter
    def set_dob(self):
        new_dob = input('Date of birth: ')
        if isinstance(new_dob, str):
            self._dob = new_dob.capitalize()
        else:
            print('Date of birth must be a string.')
            return self.set_dob()
    
    @property 
    def get_email(self):
        return self._email
    
    @get_email.setter
    def set_email(self):
        new_email = input('Email: ')
        if isinstance(new_email, str):
            self._email = new_email
        else:
            print('Email must be a string.')
            return self.set_email()
    
    @property
    def get_license_num(self):
        return self._license_num
    
    @get_license_num.setter
    def set_license_num(self):
        num = int(input('License number: '))
        if isinstance(num, int) or num is None:
            self._license_num = num
        else:
            print('License number must be an integer or None.')
            self.set_license_num()