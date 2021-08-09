#-*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   mfyreport
# FileName:     setup
# Author:      MingFeiyang
# Datetime:    2021/8/9 14:23
#-----------------------------------------------------------------------------------

import setuptools

with open("./README.md", "r",encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mfyreport",
    version="0.0.2",
    author="MingFeiyang",
    author_email="mfy1102@163.com",
    description="打印报告的库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mfy68/mfyreport.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)