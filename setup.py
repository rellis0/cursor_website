from setuptools import setup, find_packages

setup(
    name="cursor_website",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit",
    ],
    extras_require={
        "dev": [
            "pre-commit",
            "black",
            "mypy",
        ],
        "test": [
            "unittest",
        ],
    },
)
