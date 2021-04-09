from setuptools import setup

with open('README.md', 'r') as f:
    long_description =  f.read()

setup(
    name = 'helloworld',
    version = '0.0.1',
    description = 'add numbers wow',
    py_modules = ['helloworld'],
    package_dir = {'': 'src'},
    classifiers = [
        'Programming Language:: Python :: 3',
        'Programming Language:: Python :: 3.6',
        'Programming Language:: Python :: 3.7',
        'Operating System :: OS Independent',
    ], 
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install_requires = [
        "blessings >= 1.7",
        "numpy > 1.1",
    ],
    extras_require = [
        "dev": ["pytest == 3.7"]
    ]
)