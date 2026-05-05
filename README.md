## Hash3r

The project was created to learn about the cryptographic algorithms used in cybersecurity and their relevance to each other in terms of speed and strength.

## Installation

```bash
source ~/venv/bin/activate
pip install .
```

## Usage

```bash
hash3r -a <algorithm> (-s <string> | -f <file> | -l <list> | -vH <hash>)
```

### Supported Algorithms

- sha256  
- sha512  
- sha3  
- md5  
- bcrypt  
- argon2  
- blake3  

---

### Examples

#### 🔹 Hash a string
```bash
hash3r -a argon2 -s "Password123"
```

#### 🔹 Hash a file
```bash
hash3r -a sha256 -f file.txt
```

#### 🔹 Hash multiple strings from a list
```bash
hash3r -a blake3 -l list.txt
```

#### 🔹 Verify a hash
```bash
hash3r -a argon2 -s "Password123" -vH <hash>
```

---

### Notes

- Use **-s** for direct string input  
- Use **-f** to hash file contents  
- Use **-l** to hash multiple inputs from a file  
- Use **-vH** to verify a hash against a string  
- Output for list hashing is saved to `Hash3s.txt`

## Contributors

- **Akhilesh Singh Choudhary** — Developer  
  GitHub: https://github.com/aki-seven

- **Ankush Bhadwar** — Developer  
  GitHub: https://github.com/anku0669
