from setuptools import setup, find_packages 

with open("./README.md", "r") as file:
    desc = file.read()

setup(
    long_description = desc,
    long_description_content_type = "text/markdown",
    packages = find_packages()
)
