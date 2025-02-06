from setuptools import setup

setup(
    name='cryptoneed',
    version='1.0.0',
    author='pashkatrick',
    description='A reusable Python library module',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pashkatrick/cryptoneed',
    py_modules=['cryptoneed'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
