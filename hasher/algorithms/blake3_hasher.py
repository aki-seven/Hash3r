#!/usr/bin/env python3
import os, argparse
import blake3


class Blake3:# class
    CHUNK_SIZE = 8192 # it handles the large file upto 8kb.

    def __init__(self):     # intializes the object
        self.hash_value = None

    def _validate_file_path(self, file_path: str) -> bool:

        if not os.path.exists(file_path):
            print(f"Error: The path '{file_path}' does not exist.")
            return False
        if not os.path.isfile(file_path):
            print(f"Error: The path '{file_path}' is a directory, not a file.")
            return False
        return True

    def hash_string(self, input_string: str) -> str:

        input_bytes = input_string.encode('utf-8')     # the most  common encoding value is utf 8
        self.hash_value = blake3.blake3(input_bytes).hexdigest()
        return self.hash_value

    def hash_file(self, file_path: str) -> str | None: # None is used when the function does not return any value

        if not self._validate_file_path(file_path):     # the statement return when the file path is incorrect if it is right it returns none
            return None

        try:
            hasher = blake3.blake3()
            with open(file_path, "rb") as f:
                while chunk := f.read(self.CHUNK_SIZE):
                    hasher.update(chunk)
            self.hash_value = hasher.hexdigest()
            return self.hash_value
        except IOError as e:
            print(f"Error reading file '{file_path}': {e}")
            return None


def main():

    parser = argparse.ArgumentParser(       # this is main function use for parsing the the objects
        description="A command-line tool to compute BLAKE3 hashes for strings or files.",
        epilog="Note: Requires the blake3 library. On Debian/Ubuntu, run: apt install python3-blake3"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-s", "--string", help="Input string to hash.")   # parsing for strings
    group.add_argument("-f", "--file", help="Input file path to hash.") # parsing for file

    args = parser.parse_args()

    hasher = Blake3()

    if args.string: # this return statement which give the result from text to hash which is in hexadecimal format
        digest = hasher.hash_string(args.string)
        if digest:
            print(f'blake3 hash ({args.string}) = {digest}')
    elif args.file: # it is for file
        digest = hasher.hash_file(args.file)
        if digest:
            print(f'blake3 hash ({args.file}) = {digest}')


if __name__ == "__main__":
    main()

