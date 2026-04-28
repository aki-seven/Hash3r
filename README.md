<h1 align="center">🔐 Hash3r</h1>
<h3 align="center">Advanced Password Hashing & Verification Toolkit</h3>

<p align="center">
  A lightweight Python CLI utility for generating, managing, and verifying secure cryptographic hashes.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-CLI-black?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Security-Cryptography-black?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Open%20Source-Utility-black?style=for-the-badge"/>
</p>

---

## ⚡ Overview

**Hash3r** is a command-line based cryptographic hashing utility built for:

- secure password hashing
- integrity verification
- educational cryptography experiments
- quick generation of industry-standard digests

It provides a clean and modular hashing engine useful for developers, security learners, and authentication projects.

---

## 🔥 Supported Hash Algorithms

- MD5
- SHA1
- SHA224
- SHA256
- SHA384
- SHA512
- Bcrypt
- Argon2 *(if enabled in package)*

---

## 🚀 Key Features

✅ Generate secure hashes instantly  
✅ Verify plaintext against existing hashes  
✅ Simple command-line interface  
✅ Modular Python package structure  
✅ Easy integration with authentication systems  
✅ Security-focused utility for learning and experimentation

---

## 🖥 Usage

```bash
python -m hasher.cli --help
```

### Example: Generate Hash

```bash
python -m hasher.cli hash "mypassword" --algo sha256
```

### Example: Verify Hash

```bash
python -m hasher.cli verify "mypassword" "<stored_hash>"
```

---

## 📂 Project Structure

```bash
Hash3r/
│
├── hasher/
│   ├── cli.py
│   ├── core.py
│   ├── algorithms.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

## 🎯 Use Cases

- Authentication system development
- Password storage testing
- Cryptography demonstrations
- Security education
- Data integrity verification

---

## 🛠 Tech Stack

- Python 3
- Cryptographic Hash Libraries
- CLI Argument Parsing

---

## 👨‍💻 Contributors

- **Akhilesh Singh Choudhary** — Developer  
  GitHub: https://github.com/aki-seven

- **Ankush Bhadwar** — Developer  
  GitHub: https://github.com/anku0669

---

## 📌 Future Improvements

- File hashing support
- Batch verification
- Hash cracking benchmark mode
- Colored terminal interface
- Docker packaging

---

<p align="center"><b>Built with security in mind. Designed for cryptographic experimentation.</b></p>
