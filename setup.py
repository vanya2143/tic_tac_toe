from setuptools import setup, find_packages
from os.path import join, dirname

with open(join(dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tic_tac_toe',
    version='1.0',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts':
            ['ticapp = tic_tac_toe.app']
    }
)
