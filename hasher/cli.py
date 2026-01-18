
import sys, argparse
import pyfiglet
from pyfiglet import FigletFont
from hasher.utils import Utilities
from argparse import ArgumentParser

def parse_arguments():
    usage = "%(prog)s -a <algorithm> (-s <string> | -f <file> | -l <list> | -v <verify>)"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-a", "--algorithm", dest="algorithm",
                        help="algorithm to use for hashing", metavar ="")
    parser.add_argument("-s", "--string", dest="string", 
                        help="string to hash", metavar ="")
    parser.add_argument("-f", "--file", dest="file", 
                        help="file to hash", metavar ="")
    parser.add_argument("-l", "--list", dest="list", 
                        help="file with strings to hash", metavar ="")
    parser.add_argument("-vH", "--verify", dest="verify", 
                        help="hash string to verify", metavar ="")
    # parser.add_argument("-H", "--hash-value", dest="hash_value",
    #                     help="hash to verify", metavar ="")
    
    options = parser.parse_args() # command line for option parser

    if not (options.string or options.file or options.list or options.verify or options.algorithm): # if user input in not correct then it shows the help parser.
        parser.print_help()
        # print("[-] Error: Type -h for help.")
        print("[-] Example: python hasher.py -a argon2 -s 'Password123'")
        print("[-] Example: python hasher.py --algo blake3 --string 'Hello world'")
        print("[-] Example: python hasher.py -a argon2 -s 'Hello world' -h hashvalue -v")
        sys.exit(1)


    return options

def select_hasher(algorithm):
    if algorithm.lower() == "sha256":
        from .algorithms.sha256_hasher import Sha256
        return Sha256()
    elif algorithm.lower() == "sha512":
        from .algorithms.sha512_hasher import Sha512
        return Sha512()
    elif algorithm.lower() == "sha3":
        from .algorithms.sha3_hasher import Sha3
        return Sha3()
    elif algorithm.lower() == "bcrypt":
        from .algorithms.bcrypt_hasher import Bcrypt
        return Bcrypt()
    elif algorithm.lower() == "md5":
        from .algorithms.md5_hasher import Md5
        return Md5()
    elif algorithm.lower() == "argon2":
        from .algorithms.argon2_hasher import Argon2
        return Argon2()
    elif algorithm.lower() == "blake3":
        from .algorithms.blake3_hasher import Blake3
        return Blake3()
    
    else:
        supported = ["sha3", "sha512", "sha256", "md5", "bcrypt" "argon2", "blake3"]
        print(f"[-] Error: Unsupported algorithm. Supported algorithms are: {', '.join(supported)}.")
        sys.exit(1)


def run_cli(options):
    hasher = select_hasher(options.algorithm)

    if options.verify and options.string:  # Verification block
        if hasattr(hasher, "verify_hash"): # Change when get a chance to do so 
            # Has built-in verify (Argon2)
            result = hasher.verify_hash(options.verify, options.string)
        else:
            # Deterministic hashes (SHA256, Blake3)
            result = Utilities.verify_hash(options.verify, options.string, hasher)

        if result:
            print("[+] Verification successful")
        else:
            print("[-] Verification failed")

    elif options.list:
        digest_list = Utilities.hash_list(options.list, hasher)
        if digest_list:
            print("[+] Hashes written to Hash3s.txt")
        else:
            print(f"[-] An error occurred. Please check the file for correct format.")
            print(f"Correct Syntax for file: Each line should contain a single string to hash.")
            sys.exit(1)

    elif options.file:
        digest = hasher.hash_file(options.file)
        print(f"(\"{options.file}\") = {digest}")
    else:
        digest = hasher.hash_string(options.string)  
        print(f"{options.algorithm.upper()}(\"{options.string}\") = {digest}")

        
 # Entry Point
def main():

    figlet =pyfiglet.Figlet(font='doh') # Works differently when bundled
    banner = figlet.renderText("Hash3R")
    print(banner)

    options = parse_arguments()
    run_cli(options)

if __name__ == "__main__":
    main()
