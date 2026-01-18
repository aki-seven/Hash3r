from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Hash3r",
    version="1.0.0",
    description="An educational multi-algorithm hashing CLI tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Akhilesh Singh Choudhary",
    author_email="akhileshbadyal@gmail.com",  # optional, can remove if you want
    url="https://github.com/aki-seven/Hash3r",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "bcrypt",
        "argon2-cffi",
        "blake3",
        "pyfiglet",
    ],
    entry_points={
        "console_scripts": [
            "hash3r=hasher.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
    ],
    python_requires=">=3.8",
)
