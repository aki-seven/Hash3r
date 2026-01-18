from setuptools import setup, find_packages

setup(
    name="hash3r",
    version="0.7",
    description="A multi-algorithm hashing CLI tool",
    author="Your Name",
    author_email="you@example.com",
    url="https://github.com/yourusername/hash3r",  # optional
    packages=find_packages(),  # Automatically include all packages in the project
    include_package_data=True,
    install_requires=[
        "bcrypt",
        "argon2-cffi",
        "blake3",
        "pyfiglet",
        # Add any other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "hash3r=hasher.cli:main",  # This makes `hash3r` command available globally
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
