
import hashlib
from hasher.utils import Utilities # COMMENT this if u wanna run only this file else it will throw an error.

class Sha256:
    chunk_size = 8192 # 8KB chunk size for reading files

    def __init__(self):
        pass

    def hash_string(self, string: str) -> str: # Type hinting
        hasher = hashlib.sha256()
        hasher.update(string.encode('utf-8'))
        return hasher.hexdigest()

    def hash_file(self, file_path: str) -> str: # Type hinting
        if Utilities.validate_file_path(file_path):
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                while chunk := f.read(self.chunk_size):
                    hasher.update(chunk)
            return hasher.hexdigest()
        else:
            return None



# FOR STANDALONE TESTING

# if __name__ == "__main__":
#     sha256_hasher = Sha256()
#     test_string = "Hello, World!"
#     print(f"String: {test_string}")
#     print(f"SHA-256 Hash: {sha256_hasher.hash_string(test_string)}")
#     if sha256_hasher.verify_hash(sha256_hasher.hash_string(test_string), test_string):
#         print("[+] verfication ok!")
