import os
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHash
from hasher.utils import Utilities

class Argon2:

    DEFAULT_TIME_COST = 2 # Increased to increase computation time, more time to brute force.
    DEFAULT_MEMORY_COST = 102400 # 100 MiB. Increased to increase memory usage, more memory needed to brute force.
    DEFAULT_PARALLELISM = 8 # Number of Threads
    DEFAULT_HASH_LEN = 32 # in bytes
    DEFAULT_SALT_LEN = 16 # in bytes

    def __init__(self, time_cost=None, memory_cost=None, parallelism=None, hash_len=None, salt_len=None):
        
        self.hasher = PasswordHasher(
            time_cost=time_cost or self.DEFAULT_TIME_COST,
            memory_cost=memory_cost or self.DEFAULT_MEMORY_COST,
            parallelism=parallelism or self.DEFAULT_PARALLELISM,
            hash_len=hash_len or self.DEFAULT_HASH_LEN,
            salt_len=salt_len or self.DEFAULT_SALT_LEN
        )  

    def hash_string(self, string: str) -> str: # Type hinting
        hashed = self.hasher.hash(string)
        if self.verify_hash(hashed, string):
            print("[+] Hashing and verification successful.")
        return hashed
        
    def hash_file(self, file_path: str) -> str: # Type hinting
        print("[-] Warning: Argon2 is not intended for file hashing. Use SHA-256 or Blake3 instead.")
        if not Utilities.validate_file_path(file_path):
            return None
                
        with open(file_path, 'rb') as f:
            data = (f.read()).decode('latin1') #.decode('utf-8', errors='ignore') # Decoding data before passing it.
            return self.hasher.hash(data)
    
    def verify_hash(self, hash: str, string: str) -> bool:
        try:
            return self.hasher.verify(hash, string)
        except (VerifyMismatchError, InvalidHash) as e:
            if isinstance(e, InvalidHash):
                print("[-] Error: The provided hash is not a valid Argon2 hash.")
            return False

if __name__ == "__main__":
    Argon2_hasher = Argon2()
    test_string = "Hello, Worl!"
    print(f"String: {test_string}")
    hash_val = Argon2_hasher.hash_string(test_string)
    print(f"ARGON2 Hash: {hash_val}")
    if Argon2_hasher.verify_hash(hash_val, test_string):
        print("[+] verification ok")

