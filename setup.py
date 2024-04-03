# -*- coding: utf-8 -*-
"""
# @项目名称 :zsx_pack
# @文件名称 :setup.py
# @作者名称 :zsx
# @日期时间 :2024/4/3 17:06
# @文件介绍 :
"""
import setuptools  # 导入setuptools打包工具

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zsx_pack",  # 用自己的名替换其中的YOUR_USERNAME_
    version="0.0.1",  # 包版本号，便于维护版本
    author="zsx",  # 作者，可以写自己的姓名
    author_email="17630583910@163.com",  # 作者联系方式，可写自己的邮箱地址
    description="自用包，主要是为了不行使用logger无法屏蔽第三方包日志",  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="",  # 自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 对python的最低版本要求
)
