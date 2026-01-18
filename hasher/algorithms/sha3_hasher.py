#! /usr/bin/env python3

import hashlib
from hasher.utils import Utilities  # COMMENT this if you want to run only this file

class Sha3:
    chunk_size = 8192  # 8KB chunk size for reading files

    def __init__(self):
        pass

    def hash_string(self, string: str) -> str:
        """Generate SHA3-256 hash for a string."""
        hasher = hashlib.sha3_256()
        hasher.update(string.encode('utf-8'))
        return hasher.hexdigest()

    def hash_file(self, file_path: str) -> str:
        """Generate SHA3-256 hash for a file."""
        if Utilities.validate_file_path(file_path):
            hasher = hashlib.sha3_256()
            with open(file_path, 'rb') as f:
                while chunk := f.read(self.chunk_size):
                    hasher.update(chunk)
            return hasher.hexdigest()
        else:
            return None


# FOR STANDALONE TESTING
# if __name__ == "__main__":
#     sha3_hasher = Sha3()
#     test_string = "Hello, World!"
#     print(f"String: {test_string}")
#     print(f"SHA3-256 Hash: {sha3_hasher.hash_string(test_string)}")
