from setuptools import setup, find_packages

def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        README = f.read()
    return README

setup(
    name="zakilla",
    version="1.0.2",
    description="A modern, easy to use, and fully customizable pagination system for discord.py",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="ZaaakW",
    license="Apache-2.0",
    url="https://github.com/ZaaakW/zakilla",
    packages=find_packages(include=["zakilla", "zakilla.*"]),
    install_requires=[
        "discord.py",
        "disnake",
        "pillow",
        "python-dotenv"
    ],
)