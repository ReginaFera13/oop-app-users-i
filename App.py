import csv
from User import User
# App name: ArdaConnect

class App:
    MENU = [
        '---ArdaConnect---',
        '1. Login',
        '2. Create Account',
        '3. Exit'
    ]
    
    HOME = [
        '---Welcome to ArdaConnect!---',
        '1. Profile',
        '2. Friends',
        '3. Posts',
        '4. Feed',
        '5. Logout'
    ]
    
    PROFILE =  [
        '---Your Profile---',
        '1. Change username',
        '2. Change password',
        '3. Change first name',
        '4. Change last name',
        '5. Change email',
        '6. Change license number',
        '7. Menu'
    ]
    
    FRIENDS = [
        '---Your Friends---',
        '1. View friends',
        '2. Add friend',
        '3. Remove friend',
        '4. Menu'
    ]
    
    POSTS = [
        '---Your Posts---',
        '1. View posts',
        '2. Add post',
        '3. Delete post',
        '4. Menu'
    ]

    def __init__(self, app_name):
        self.users = self.load_data('users.csv')
        self.app_name = app_name
        
        User.load_users_from_app(self)
    
    def load_data(self, file):
        data_dict = {}
        with open(file, mode='r', newline='') as csvfile:
            user_data_reader = csv.DictReader(csvfile)
            for row in user_data_reader:
                username = row['username']
                    
                user_data = {
                    'username': username,
                    'password': row['password'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'dob': row['dob'],
                    'email': row['email'],
                    'license_num': row['license_num']
                }
                data_dict[username] = user_data
        return data_dict
    
    def home(self, user):
        menu_selction = 0
        user = user
        while menu_selction < 5:
            for item in App.HOME:
                print(item)
            
            if menu_selction == 0:
                try:
                    menu_selction = int(input('Enter menu number: '))
                except ValueError:
                    print('Invalid selection. Please try again.')
                    menu_selction = 0
        
    
    def run_app(self):
        menu_selction = 0
        user = None
        while menu_selction < 3:
            for item in App.MENU:
                print(item)
            
            if menu_selction == 0:
                try:
                    menu_selction = int(input('Enter menu number: '))
                except ValueError:
                    print('Invalid selection. Please try again.')
                    menu_selction = 0
            if menu_selction == 1:
                user = User.get_user_by_username()
                password = user.get_password
                print(password)
                menu_selction = 0
                # password = User.password_login(user)
                # if password == True:
                #     self.HOME(user)
                # else:
                #     print('Login Failed: Your user ID or password is incorrect')
                #     menu_selction == 1