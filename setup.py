#-*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   mfyreport
# FileName:     setup
# Author:      MingFeiyang
# Datetime:    2021/8/9 14:23
#-----------------------------------------------------------------------------------

from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name='mfyreport',
    version='1.1.3',
    author='MingFeiyang',
    author_email='mfy1102@163.com',
    url='https://pypi.org/project/mfyreport',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["Jinja2==2.10.1", "PyYAML==5.3.1","requests==2.24.0"],
    packages=find_packages(),
    package_data={
        "": ["*.html",'*.md'],
    },
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)