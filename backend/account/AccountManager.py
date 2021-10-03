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
    :return:
    """
    if password != confirm_password:
        print('Passwords do not match.')
    else:
        create_account(email, password)


def create_account(email, password):
    """
    Create an account.
    :param email: Sign up email
    :param password: Account password
    :return:
    """
    try:
        auth.create_user_with_email_and_password(email, password)
        print('Successfully created account.')
    except:
        print('Email already exists.')


def sign_in(email, password):
    """
    Sign in to an account.
    :param email: Sign in email
    :param password: Account password
    :return:
    """
    try:
        auth.sign_in_with_email_and_password(email, password)
        print('Successfully logged in.')
    except:
        print('Invalid email or password.')


sign_in('exampl3e@mail.com', '123456')
# sign_up('exampl1e@mail.com', '123456')
# create_account_confirm_password('exampl3e@mail.com', '123456', '123456')
