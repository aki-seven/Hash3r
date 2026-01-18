import unittest
from hasher.algorithms.blake3_hasher import Blake3

class TestBlake3Hasher(unittest.TestCase):

    def setUp(self):
        self.hasher = Blake3()

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
