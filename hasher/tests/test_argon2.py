import unittest
from hasher.algorithms.argon2 import Argon2Hasher

class TestArgon2Hasher(unittest.TestCase):

    def setUp(self):
        self.hasher = Argon2Hasher()

    def test_hash_output(self):
        password = "secure_password"
        hashed = self.hasher.hash(password)
        self.assertIsInstance(hashed, str)
        self.assertNotEqual(password, hashed)

    def test_verify(self):
        password = "secure_password"
        hashed = self.hasher.hash(password)
        self.assertTrue(self.hasher.verify(password, hashed))
        self.assertFalse(self.hasher.verify("wrong_password", hashed))

if __name__ == '__main__':
    unittest.main()
