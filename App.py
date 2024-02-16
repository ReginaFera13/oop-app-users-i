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
        '1. Profile',
        '2. Friends',
        '3. Posts',
        '4. Feed',
        '5. Logout'
    ]
    
    PROFILE =  [
        '1. Change username',
        '2. Change password',
        '3. Change first name',
        '4. Change last name',
        '5. Change email',
        '6. Menu'
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
        users = []
        with open(file, mode='r', newline='') as csvfile:
            user_data_reader = csv.DictReader(csvfile)
            for row in user_data_reader:
                user = User(
                    username = row['username'],
                    password = row['password'],
                    first_name = row['first_name'],
                    last_name = row['last_name'],
                    dob = row['dob'],
                    email = row['email'],
                )
                users.append(user)
        return users
    
    # def home(self, user):
    #     menu_selction = 0
    #     user = user
    #     while menu_selction < 5:
    #         for item in self.HOME:
    #             print(item)
            
    #         if menu_selction == 0:
    #             try:
    #                 menu_selction = int(input('Enter menu number: '))
    #             except ValueError:
    #                 print('Invalid selection. Please try again.')
    #                 menu_selction = 0
    #         if menu_selction == 1:
    
    # def home(self, user):
    #     menu_selction = 0
    #     user = user
    #     while menu_selction < 5:
    #         for item in self.HOME:
    #             print(item)
            
    #         if menu_selction == 0:
    #             try:
    #                 menu_selction = int(input('Enter menu number: '))
    #             except ValueError:
    #                 print('Invalid selection. Please try again.')
    #                 menu_selction = 0
    #         if menu_selction == 1:
    
    def profile(self, user):
        menu_selction = 0
        user = user
        while menu_selction < 5:
            print(f'---Your Profile--- \nName: {user.get_full_name} \nUsername: {user.get_username} \nEmail: {user.get_email}')
            for item in self.PROFILE:
                print(item)
            
            if menu_selction == 0:
                try:
                    menu_selction = int(input('Enter menu number: '))
                except ValueError:
                    print('Invalid selection. Please try again.')
                    menu_selction = 0
            if menu_selction == 1:
                print(f'Current username: {user.get_username}')
                user.set_username = input('Username: ')
                print(f'New username: {user.get_username}')
                menu_selction = 0
            if menu_selction == 2:
                print(f'Current password: {user.get_password}')
                user.set_password = input('Password: ')
                print(f'New password: {user.get_password}')
                menu_selction = 0
            if menu_selction == 3:
                print(f'Current first name: {user.get_first_name}')
                user.set_first_name = input('First name: ')
                print(f'New first name: {user.get_first_name}')
                menu_selction = 0
            if menu_selction == 4:
                print(f'Current last name: {user.get_last_name}')
                user.set_last_name = input('Last name: ')
                print(f'New last name: {user.get_last_name}')
                menu_selction = 0
            if menu_selction == 5:
                print(f'Current email: {user.get_email}')
                user.set_email = input('Email: ')
                print(f'New email: {user.get_email}')
                menu_selction = 0
            if menu_selction == 6:
                self.home(user)

    
    def home(self, user):
        menu_selction = 0
        user = user
        while menu_selction < 5:
            print(f'---Welcome {user.get_first_name} to ArdaConnect!---',)
            for item in self.HOME:
                print(item)
            
            if menu_selction == 0:
                try:
                    menu_selction = int(input('Enter menu number: '))
                except ValueError:
                    print('Invalid selection. Please try again.')
                    menu_selction = 0
            if menu_selction == 1:
                self.profile(user)
                
    def run_app(self):
        menu_selction = 0
        user = None
        while menu_selction < 3:
            for item in self.MENU:
                print(item)
            
            if menu_selction == 0:
                try:
                    menu_selction = int(input('Enter menu number: '))
                except ValueError:
                    print('Invalid selection. Please try again.')
                    menu_selction = 0
            if menu_selction == 1:
                user = User.get_user_by_username()
                if user:
                    password = user.password_login()
                    if password == True:
                        print(user)
                        self.home(user)
                    else:
                        print('Login Failed: Your user ID or password is incorrect')
                        menu_selction == 1
                    