BASE_PATH = 'data/'
USER_PATH = BASE_PATH + 'user/'
DB_PATH = BASE_PATH + 'db/'

def login():

    import getpass

    user_name = raw_input('Enter the User Name : ')
    password = getpass.getpass()

    if validate_login(user_name, password) :
        return load_auth_file(user_name)
    else :
        login_choise = raw_input('Do you want register? [Y/N][N] : ')
        if (login_choise.lower() == 'y'):
            return register_profile(user_name, password)
        else :
            return login()

def register_profile(user_name, password):
    import model
    import pickle

    user_name = raw_input('Enter your name : ')
    password = raw_input('Password : ')

    create_dir(USER_PATH)
    create_dir(DB_PATH)
    model.user_profile['name'] = user_name
    model.user_profile['password'] = password

    write_file = open(get_file_path(user_name), 'wb')
    pickle.dump(model.user_profile, write_file)
    write_file.close()
    return model.user_profile

def validate_login(user_name, password):
    import os.path
    valid_user = os.path.isfile(get_file_path(user_name))

    if not valid_user:
        return False

    metadata = load_auth_file(user_name)

    return metadata['password'] == password

def load_auth_file(file_name):
    import pickle

    auth_path = get_file_path(file_name)
    with open(auth_path, 'rb') as auth_file:
        auth_dict = pickle.load(auth_file)
    
    if auth_dict['is_new']:
        auth_dict['is_new'] = False
    
    return auth_dict

def get_file_path(file_name):
    return USER_PATH + file_name + '.auth'

def create_dir(path):

    import os
    import errno

    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise