import unittest
from hasher.algorithms.sha256_hasher import sha256

class TestSHA256Hasher(unittest.TestCase):

    def setUp(self):
        self.hasher = sha256()

    def test_hash_string(self):
        password = "secure_password"
        hashed = self.hasher.hash_string(password)
        self.assertIsInstance(hashed, str)
        self.assertNotEqual(password, hashed)
        # Consistency check: same string should produce same hash
        self.assertEqual(hashed, self.hasher.hash_string(password))

    def test_hash_file(self):
        import tempfile
        with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
            tmp.write("test content")
            tmp_path = tmp.name
        hashed = self.hasher.hash_file(tmp_path)
        self.assertIsInstance(hashed, str)
        expected_hash = self.hasher.hash_string("test content")
        self.assertEqual(hashed, expected_hash)

if __name__ == '__main__':
    unittest.main()
