from setuptools import setup, find_packages

setup(
    name="zakila",
    version="0.0.1",
    description="A modern, easy to use, and fully customizable pagination system for discord.py",
    author="ZaaakW",
    license="Apache-2.0",
    url="https://github.com/ZaaakW/zakila",
    packages=find_packages(include=["zakila", "zakila.*"]),
    install_requires=[
        "discord.py",
        "disnake",
        "pillow",
        "python-dotenv"
    ],
)