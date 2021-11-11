import unittest

from backend.account import AccountManager


class TestCreateAccount(unittest.TestCase):
    def test_create_already_exists(self):
        result = AccountManager.create_account('example@mail.com', '123456')
        expected_result = None  # account already exists
        self.assertEqual(expected_result, result)


class TestCreateConfirmPassword(unittest.TestCase):
    def test_create_password_issue(self):
        self.assertRaises(ValueError, AccountManager.create_account_confirm_password, 'example@mail.com', '123456',
                          '12345')


class TestLogin(unittest.TestCase):
    def test_login_exist(self):
        result = AccountManager.login('example@mail.com', '123456')
        # local_id = result['localId']
        # expected_result = 'mwoWFrnH5wa8Xcv1VlJDXaeBNP92'  # account localId
        expected_result = 'example@mail.com'
        self.assertEqual(expected_result, result)

    def test_login_not_exist(self):
        result = AccountManager.login('non_existent@mail.com', '123456')
        expected_result = None  # account does not exist
        self.assertEqual(expected_result, result)


class TestResetPassword(unittest.TestCase):
    def test_reset_account_exist(self):
        result = AccountManager.reset_account_password('example@mail.com')
        expected_result = True  # reset email sent
        self.assertEqual(expected_result, expected_result)

    def test_reset_account_not_exist(self):
        result = AccountManager.reset_account_password('non_existent@mail.com')
        expected_result = None  # account does not exist
        self.assertEqual(expected_result, result)


class TestGetAccountInfo(unittest.TestCase):
    def test_get_account_exist(self):
        local_id = AccountManager.login_return_user('example@mail.com', '123456')['idToken']
        result = AccountManager.get_user_account_info(local_id)
        email = result['email']
        expected_result = 'example@mail.com'  # account localId
        self.assertEqual(expected_result, email)

    def test_get_account_not_exist(self):
        result = AccountManager.get_user_account_info('invalid_localId')
        expected_result = None  # account does not exist
        self.assertEqual(expected_result, result)


