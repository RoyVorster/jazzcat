from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Add easter eggs to your github for not a single good reason'

# Simplest possible setup
setup(
    name='jazzcat', 
    version=VERSION,
    author='Roy Vorster',
    author_email='royvorster@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    url='https://github.com/RoyVorster/jazzcat',
)

