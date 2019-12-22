from setuptools import setup

with open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="World of Warcraft API",
    version="1.0.0",
    description="Blizzard's World of Warcraft API.",
    long_description=readme,
    license=license,

    author="Mislav Jaksic",
    author_email="jaksicmislav@gmail.com",
    maintainer="Mislav Jaksic",
    maintainer_email="jaksicmislav@gmail.com",

    url="https://github.com/MislavJaksic/World-of-Warcraft-API",

    entry_points={"console_scripts": ["Project-Name = src.wowapi.runner:run"]}
)
