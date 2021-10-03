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


def sign_in(email, password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        print('Successfully logged in.')
    except:
        print('Invalid email or password.')


sign_in('example@mail.com', '123456')
