import unittest
from utils.hash_util import hash_password

class TestHashUtil(unittest.TestCase):
    def test_hash_password(self):
        expected_hash = "5BAA61E4D5A9F3E6"
        self.assertEqual(hash_password("password"), expected_hash)

if __name__ == "__main__":
    unittest.main()
