from setuptools import setup, find_packages
from io import open
from os import path

import pathlib
HERE = pathlib.Path(__file__).parent

with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
    
install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]
                    
setup (
 name = 'simple_encryption',
 description = 'CLI for simple encryption',
 version = '1.0.0',
 packages = find_packages(),
 install_requires = install_requires,
 python_requires='>=3.6',
 entry_points='''
        [console_scripts]
        simple_encryption=simple_encryption.__main__:main
    ''',
 author="Soutrik Neogi"
)