from setuptools import setup
from setuptools import find_packages

setup(
    name='testPackage',
    version='1.0.0',
    description='Basic package layout',
    author='Steve Ryan',
    author_email='steve.ryan@qstatebio.com',
    url='https://github.com/q-state-biosciences/Analysis',
    install_requires=[], # How would these be formatted?
#    packages=find_packages(exclude=('tests*','myPackage')), # useful to exclude support code, like tests
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello-world-cli = hello_world.main:main',
        ],
    },
)
