import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
name = 'main_module',
version = '0.0.2',
author = 'USC AUV Team',
author_email = 'hshively@usc.edu',
description = 'Logic for autonomous path following and task execution',
long_description = long_description,
long_description_content_type = 'text/markdown',
url = 'https://github.com/usc-auv-team/main.module',
packages = setuptools.find_packages(),
classifiers = [
    'Programming Language :: Python',
    'Operating System :: OS Independent',
],
)
