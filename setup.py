import os
from setuptools import setup, find_packages

setup(
    name='processing-pipeline',
    version=__import__('pipeline').__version__,
    author='John Leith',
    author_email='leith.john@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/freakypie/python-pipline',
    zip_safe=False,
)
