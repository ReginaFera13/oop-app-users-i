from App import App

ARDACONNECT = App('ArdaConnect')
ARDACONNECT.load_data('users.csv')
print(ARDACONNECT.users)
print(ARDACONNECT.run_app())