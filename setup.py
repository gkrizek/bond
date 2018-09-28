from setuptools import setup
from beam import __version__


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="bonder",
    version=__version__,
    description="Atom Auto-Bonding for a Cosmos Validator",
    long_description=readme(),
    author="Graham Krizek",
    author_email="gkrizek@krizek.io",
    url="https://github.com/gkrizek/bonder",
    packages=["bonder"],
    py_modules=['bonder'],
    install_requires=[
        "click"
    ],
    entry_points={
        "console_scripts": ['bonder = bonder.index:main']
    }
)
