from setuptools import setup, find_packages

setup(
    name='smartbot',
    version='1',
    description='Script help you working with contacts, notes and help you sort files in folder',
    packages=find_packages(),
    install_requires=['fuzzywuzzy', 'python-Levenshtein'],
    entry_points={'console_scripts': ['smartbot = smartbot.app:main']}
)
