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


class TestSignIn(unittest.TestCase):
    def test_sign_in_exist(self):
        result = AccountManager.sign_in('example@mail.com', '123456')
        local_id = result['localId']
        expected_result = 'mwoWFrnH5wa8Xcv1VlJDXaeBNP92'  # account localId
        self.assertEqual(expected_result, local_id)

    def test_sign_in_not_exist(self):
        result = AccountManager.sign_in('non_existent@mail.com', '123456')
        expected_result = None  # account does not exist
        self.assertEqual(expected_result, result)