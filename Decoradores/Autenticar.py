
# Create an @authenticated decorator that only
# allows the function to run is user1 has 'valid'
# set to True:
user1 = {
    'name': 'Sorna',
    'valid': False
}

user2 = {
    'name': 'Ticon',
    'valid': True
}

def authenticated(fn):
    def autenticador(*args,**kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return autenticador

@authenticated
def message_friends(user):
    print(user['name'])
    print('Putos todos')

message_friends(user1)
message_friends(user2)
