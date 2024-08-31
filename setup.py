from setuptools import setup, find_packages
import os


def package_files(directory):
    paths = []
    for path, directories, filenames in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


extra_files = package_files("src/static")

setup(
    name="cursor_website",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"": extra_files},
    include_package_data=True,
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
