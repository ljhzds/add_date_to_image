# coding: utf8
import re
import ast

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def extract_version():
    with open('add_date/__init__.py', 'rb') as f_version:
        ast_tree = re.search(
            r'__version__ = (.*)',
            f_version.read().decode('utf-8')
        ).group(1)
        if ast_tree is None:
            raise RuntimeError('Cannot find version information')
        return str(ast.literal_eval(ast_tree))

with open('README.rst', 'rb') as f_readme:
    readme = f_readme.read().decode('utf-8')

packages = ['add_date']
version = extract_version()

setup(
    name='add_date',
    version=version,
    keywords=['image', 'edit', 'date'],
    description='a little program to add date to a picture.',
    long_description=readme,
    author='Zhangdesheng',
    author_email='jzhangdesheng@gmail.com',
    license='MIT',
    url='https://github.com/ljhzds/add_date',

    install_requires=[],
    packages=packages,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Pc',
        'Intended Audience :: Information Technology',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: PIL :: EDIT',
    ],

    entry_points={
        'console_scripts': [
            'add_date = add_date.add_date:main'
        ]
    }
)
