import bcrypt
from hasher.utils import Utilities

class Bcrypt:

    def __init__(self):
        pass

    def hash_string(self, string: str) -> str: 
        salt=bcrypt.gensalt() # Default rounds is 12
        return bcrypt.hashpw(string.encode(), salt).decode() #and salt
        
    def hash_file(self, file_path: str) -> str: # Type hinting
        print("[-] Warning: Bcrypt is not intended for file hashing. Use SHA-256, SHA-512 or Blake3 instead.")
        if not Utilities.validate_file_path(file_path):
            return None  
        else:
            with open(file_path, 'rb') as f:
                data = f.read()
                hashed = bcrypt.hashpw(data, bcrypt.gensalt()).decode()
                return hashed 
    
    def verify_hash(self, hash_str: str, string: str) -> bool:
        try:
            if bcrypt.checkpw(string.encode(), hash_str.encode()):
                print("[+] verification ok")
                return True
            else:
                print("[-] verification failed")
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False


# STANDALONE TESTING
if __name__ == "__main__":
    bcrypt_hasher = Bcrypt()
    test_string = "Hello, World!"
    hash_val=bcrypt_hasher.hash_string(test_string)

    print(f"String: {test_string}")
    print(f"BCRYPT Hash: {hash_val}")
    bcrypt_hasher.verify_hash(hash_val, test_string)
    
