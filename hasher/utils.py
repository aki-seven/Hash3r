import sys

class Utilities:

    @staticmethod
    def validate_file_path(file_path: str) -> bool: # Type hinting
        try:
            with open(file_path, 'rb'):
                return True
        except FileNotFoundError:
            return False
        
    @staticmethod    
    def read_password_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            sys.exit(1)

    @staticmethod    
    def verify_hash(hash_str: str, string: str, hasher) -> bool:
        return hash_str == hasher.hash_string(string)
    
    @staticmethod
    def hash_list(file_path, hasher):
        if not Utilities.validate_file_path(file_path):
            print("[-] File not found")
            return False
        # printing to a file
        try:
            with open(file_path, "r") as f, open("Hash3s.txt", "w") as n:
                for line in f:
                    line = line.strip()
                    digest = hasher.hash_string(line)
                    n.write(f"{hasher.__class__.__name__.upper()}(\"{line}\") = {digest}\n")
            return True
        except Exception as e: 
           print(f"[-] Error writing to Hash3s.txt: {e}. Maybe the file already exists?")
           return False
                

                




