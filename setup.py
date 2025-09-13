from setuptools import setup, find_packages

setup(
    name="zakilla",
    version="1.0.0",
    description="A modern, easy to use, and fully customizable pagination system for discord.py",
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