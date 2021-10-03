import json
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyBUtttg0k-sJRCbGd4VTR0vEVU-28bqNmc",
    "authDomain": "smartrun-1f871.firebaseapp.com",
    "databaseURL": "smartrun-1f871.firebaseio.com",
    "projectId": "smartrun-1f871",
    "storageBucket": "smartrun-1f871.appspot.com",
    "messagingSenderId": "896848036380",
    "appId": "1:896848036380:web:5f7e0927e65c502768d5d9"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def create_account_confirm_password(email, password, confirm_password):
    """
    Create an account with password confirmation.
    :param email: Sign up email
    :param password: Account password
    :param confirm_password: Confirm account password
    :return: user
    """
    if password != confirm_password:
        print('Passwords do not match.')
    else:
        return create_account(email, password)


def create_account(email, password):
    """
    Create an account.
    :param email: Sign up email
    :param password: Account password
    :return: user
    """
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print('Successfully created account.')
        return user
    except:
        print('Email already exists.')


def sign_in(email, password):
    """
    Sign in to an account.
    :param email: Sign in email
    :param password: Account password
    :return: user
    """
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print('Successfully logged in.')
        return user
    except:
        print('Invalid email or password.')


def reset_account_password(email):
    """
    Request for password reset. Email will be sent to users email.
    :param email: User's email
    :return: True if successful. False if account does not exist.
    """
    try:
        print(auth.send_password_reset_email(email))
        return True
    except:
        print('Account does not exist.')
        return False


def get_user_account_info(idToken):
    """
    Get user object.
    :param idToken: idToken from user object.
    :return: True if successful. False if idToken invalid.
    """
    try:
        return auth.get_account_info(idToken)
    except:
        return False


def save_user(user):
    with open("user.json", "w") as write:
        json.dump(user, write)


def load_user():
    data = open('user.json',)
    user = json.load(data)

    if not is_user_valid(user):
        return None
    return user


def is_user_valid(user):
    if get_user_account_info(user['idToken']) is not None:
        return True
    else:
        return False




# print(sign_in('example@mail.com', '123456'))
# print(create_account('example@mail.com', '123456'))
# print(create_account_confirm_password('example@mail.com', '123456', '123456'))
# print(reset_account_password('example@mail.com'))
# get_user_account_info(sign_in('example@mail.com', '123456')['idToken'])
#save_user_login(sign_in('example@mail.com', '123456'))
print(load_user())