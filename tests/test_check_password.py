import unittest
from unittest.mock import patch
from check_password import check_passwords
import requests

class TestCheckPassword(unittest.TestCase):
    @patch('check_password.requests.get')
    def test_check_passwords_compromised(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '5BAA61E4D5A9F3E6:1\n'
        
        passwords = ["password"]
        results = check_passwords(passwords)
        
        self.assertIn("password", results)
        self.assertTrue(results["password"])

    @patch('check_password.requests.get')
    def test_check_passwords_not_compromised(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '5BAA61E4D5A9F3E6:0\n'
        
        passwords = ["password"]
        results = check_passwords(passwords)
        
        self.assertIn("password", results)
        self.assertFalse(results["password"])

    @patch('check_password.requests.get')
    def test_check_passwords_api_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("API Error")
        
        passwords = ["password"]
        results = check_passwords(passwords)
        
        self.assertIn("password", results)
        self.assertIsNone(results["password"])

if __name__ == "__main__":
    unittest.main()
