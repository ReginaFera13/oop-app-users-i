class User:
    all_users = []
    
    @classmethod
    def load_users_from_app(cls, app):
        cls.all_users = app.users
    
    @classmethod
    def get_user_by_username(cls):
        username = input('Username: ')
        for user in cls.all_users:
            if user.get_username == username:
                return user
        print('User not found.')
        return None
    
    @classmethod
    def create_user(cls) -> dict:
        pass

    def __init__(self, username, password, first_name, last_name, dob, email):
        User.total_users = len(User.all_users)
        self._username = username
        self._password = password
        self._first_name = first_name
        self._last_name = last_name
        self._dob = dob
        self._email = email

    
    def __str__(self):
        return f'\n{self.get_username}: password: {self.get_password}, {self.get_full_name} born on {self.get_dob} and their email is {self.get_email}.'
    
    def __repr__(self):
        return f'\n{self.get_username}: password: {self.get_password}, {self.get_full_name} born on {self.get_dob} and their email is {self.get_email}.'
    
    @property
    def get_username(self):
        return self._username
    
    @get_username.setter
    def set_username(self, new_username):
        if isinstance(new_username, str):
            if new_username not in [user.get_username for user in User.all_users]:
                self._username = new_username
            else: 
                print('Username taken. Try again')
                self.set_username = input('Username: ')
        else:
            print('Username must be a string.')
            self.set_username = input('Username: ')
    
    @property
    def get_password(self):
        return self._password
    
    @get_password.setter
    def set_password(self, new_password):
        if isinstance(new_password, str):
            self._password = new_password
        else:
            print('Password must be a string.')
            self.set_password = input('Password: ')
    
    def password_login(self):
        auth = False
        password = input('Password: ')
        if password == self.get_password:
            auth = True
        return auth
            
    @property
    def get_first_name(self):
        return self._first_name
    
    @get_first_name.setter
    def set_first_name(self, new_name):
        if isinstance(new_name, str):
            self._first_name = new_name.capitalize()
        else:
            print('Name must be a string.')
            self.set_first_name = input('First name: ')
            
    @property
    def get_last_name(self):
        return self._last_name
    
    @get_last_name.setter
    def set_last_name(self, new_name):
        if isinstance(new_name, str):
            self._last_name = new_name.capitalize()
        else:
            print('Name must be a string.')
            self.set_last_name = input('Last name: ')
            
    @property
    def get_full_name(self):
        self._full_name = f"{self.get_first_name} {self.get_last_name}"
        return self._full_name
    
    @property
    def get_dob(self):
        return self._dob
    
    @get_dob.setter
    def set_dob(self, new_dob):
        if isinstance(new_dob, str):
            self._dob = new_dob.capitalize()
        else:
            print('Date of birth must be a string.')
            self.set_dob = input('Date of birth: ')
    
    @property 
    def get_email(self):
        return self._email
    
    @get_email.setter
    def set_email(self, new_email):
        if isinstance(new_email, str):
            self._email = new_email
        else:
            print('Email must be a string.')
            self.set_email = input('Email: ')