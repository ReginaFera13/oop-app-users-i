from App import App

ARDACONNECT = App('ArdaConnect')
ARDACONNECT.load_data('users.csv')
# print(ARDACONNECT.users)
# for user in ARDACONNECT.users:
#     print(user.get_username)
print(ARDACONNECT.run_app())