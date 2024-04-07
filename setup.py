# -*- coding: utf-8 -*-
"""
# @项目名称 :zsx_pack
# @文件名称 :setup.py
# @作者名称 :zsx
# @日期时间 :2024/4/3 17:06
# @文件介绍 :
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # 在 PyPI 上搜索的项目名称。
    name="zsx_pack",
    # 项目版本号，一般由三部分组成：MAJOR, MINOR, MAINTENANCE
    version="1.0.0",
    # 作者信息
    author="zsx",
    author_email="17630583910@163.com",
    # 维护者信息
    maintainer="zsx",
    maintainer_email="17630583910@163.com",
    # 项目许可证
    license="MIT",
    # 项目的简短描述，一般一句话就好，会显示在 PyPI 上名字下端。
    description="自用包，主要是为了logger无法屏蔽第三方包日志而开发的",
    # 对项目的完整描述，使用 long_description。如果此字符串是 rst 格式的，PyPI 会自动渲染成 HTML 显示。
    long_description=long_description,
    # 不设置格式，默认是rst格式文档解读
    long_description_content_type="text/markdown",
    # project home page 通常为 GitHub上 的链接或者 readthedocs 的链接。
    url="https://github.com/ziyueguyi/zsx_pack",
    # 项目相关额外连接，如代码仓库，文档地址等
    project_urls={
        "Bug Tracker": "https://github.com/ziyueguyi/zsx_pack",
    },
    # 提供给pypi的分类依据，参考：https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python :: 3",
    ],
    install_requires=['colorama>=0.4.6'],
    package_dir={"logger": "logger"},
    python_requires=">=3.6",
    platforms=["Windows", "Linux"],

)

# from setuptools import setup
# from setuptools import find_packages
#
# # distutils核心关键词
# setup_keywords = ('distclass', 'script_name', 'script_args', 'options',
#                   'name', 'version', 'author', 'author_email',
#                   'maintainer', 'maintainer_email', 'url', 'license',
#                   'description', 'long_description', 'long_description_content_type', 'keywords',
#                   'platforms', 'classifiers', 'download_url',
#                   'requires', 'provides', 'obsoletes')
#
# # distutils核心拓展关键词
# extension_keywords = ('sources', 'include_dirs',
#                       'define_macros', 'undef_macros',
#                       'library_dirs', 'libraries', 'runtime_library_dirs',
#                       'extra_objects', 'extra_compile_args', 'extra_link_args',
#                       'swig_opts', 'export_symbols', 'depends', 'language')
#
# # setuptools拓展关键词
# setuptools_keywords = ('include_package_data', 'exclude_package_data', 'package_data',
#                        'zip_safe', 'install_requires', 'entry_points', 'extras_require',
#                        'python_requires', 'setup_requires', 'dependency_links', 'namespace_packages',
#                        'test_suite', 'tests_require', 'test_loader''eager_resources', 'use_2to3',
#                        'convert_2to3_doctests', 'use_2to3_fixers', 'project_urls', 'package_dir', 'packages',
#                        'data_files', 'scripts', 'ext_modules', 'py_modules', 'license_file', 'license_files',
#                        'use_2to3_exclude_fixers')
# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
# setup(
#     # 在 PyPI 上搜索的项目名称。
#     name="zsx_pack",
#
#     # 项目版本号，一般由三部分组成：MAJOR, MINOR, MAINTENANCE
#     version="1.0.1",
#
#     # 作者信息
#     author="zsx",
#
#     author_email="17630583910@163.com",
#
#     # 维护者信息
#     maintainer="zsx",
#
#     maintainer_email="17630583910@163.com",
#
#     # project home page 通常为 GitHub上 的链接或者 readthedocs 的链接。
#     url="https://github.com/ziyueguyi/zsx_pack",
#
#     # 项目许可证
#     license="MIT",
#
#     # 项目的简短描述，一般一句话就好，会显示在 PyPI 上名字下端。
#     description="自用包，主要是为了logger无法屏蔽第三方包日志而开发的",
#
#     # 对项目的完整描述，使用 long_description。如果此字符串是 rst 格式的，PyPI 会自动渲染成 HTML 显示。
#     long_description=long_description,
#
#     # 不设置格式，默认是rst格式文档解读
#     long_description_content_type='text/markdown',
#
#     # 项目关键词列表
#     keywords=[
#         "tornado", "web", "http_server", "mt", "Mad_tornado", "madtornado",
#         "Tornado project template", "python3", "sea", "generate the Tornado project",
#         "tornado cli", "tornado脚手架", "生成tornado项目"
#     ],
#
#     platforms=["Windows", "Linux"],
#
#     # 提供给pypi的分类依据，参考：https://pypi.org/classifiers/
#     classifiers=[
#         "Development Status :: 3 - Alpha",
#         "Intended Audience :: Developers",
#         "Topic :: Software Development :: Build Tools",
#         "License :: OSI Approved :: MIT License",
#         "Natural Language :: Chinese (Simplified)",
#         "Programming Language :: Python :: 3",
#     ],
#
#     # 发型包下载链接
#     download_url="https://github.com/ziyueguyi/zsx_pack",
#
#     # 接受MANIFEST.in匹配的所有数据文件和目录，启用后加入MANIFEST.in文件
#     include_package_data=True,
#
#     # 项目依赖数据文件，数据文件必须放在项目目录内且使用相对路径。
#     # 如果不指定作为目录的键为空串，则代表对所有模块操作
#     package_data={
#         # If any package contains *.txt or *.rst files, include them:
#         '': ['*.txt', '*.rst'],
#         # And include any *.msg files found in the 'hello' package, too:
#         # 'hello': ['*.msg'],
#     },
#
#     # Project uses reStructuredText, so ensure that the docutils get
#     # installed or upgraded on the target machine
#     # 项目依赖的 Python 库，使用 pip 安装本项目时会自动检查和安装依赖。
#     install_requires=['colorama>=0.4.6'],
#
#     # 让你的包可以作为一个工具使用
#     # 如安装pip install madtornado
#     # 运行sea --init_project ./project ，即可让发行包工具为你创建一个tornado项目模板
#     # 实现命令行直接调用的效果需要配置该选项
#     # entry_points={
#     #     'console_scripts': [
#     #         'sea = sea:main'
#     #     ]
#     # },
#
#     extras_require={},
#
#     # 指定项目依赖的 Python 版本
#     python_requires='>=3',
#
#     # setup_requires=['cython'],
#
#     dependency_links=[],
#
#     tests_require=[],
#
#     # 项目相关额外连接，如代码仓库，文档地址等
#     project_urls={
#         "Bug Tracker": "https://github.com/ziyueguyi/zsx_pack",
#     },
#
#     package_dir={"logger": "logger"},
#
#     # 列出项目内需要被打包的所有 package。一般使用 setuptools.find_packages() 自动发现
#     # exclude 用于排除不打包的 package
#     # packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
#     packages=[],
#
#     # 如果数据文件存在于项目外，则可以使用 data_files 参数或者 MANIFEST.in 文件进行管理。
#     # 如果用于源码包，则使用 MANIFEST.in；如果用于 wheel，则使用 data_files。
#     # 上述设置将在打包 wheel 时，将 data/conf.yml 文件添加至 mydata 目录。
#     data_files=[
#         ('mydata', ['data/conf.yml'])
#     ],
#
#     # 让你的包可以作为一个工具使用，与entry_points不同，entry_points是强化了这个配置
#     # 如果你只配置了这个选项，你需要sea.py --init_project ./project调用，也就是说命令行会带一个很丑的.py后缀
#     # 想要去掉.py后缀需要再配置entry_points选项，让其作为一个命令行工具，而不是一个全局的py文件来运行
#     # scripts=["logger.py"],
#
#     # 针对的是使用 C/C++ 底层语言所写的模块
#     # ext_modules=[],
#
#     # 发行包里面包含的单个模块文件，切记不要加.py后缀，直接写模块路径就行
#     py_modules=["logger"],
# )
