#!/usr/bin/env python

###############################################################################
# EXPLANATION OF KEY COMPONENTS
###############################################################################

#   - name: The distribution name of your package. This is how your package will
#   be listed on PyPI and when installing via pip.
#   - version: The current version of your package. Follow semantic versioning
#   (SemVer) as much as possible.
#   - author and author_email: Your name (or your organization's name) and email
#   address for package maintainability.
#   - description: A short, one-sentence summary of your package.
#   - long_description: A detailed description of your package. This is often
#   the content of your README.md.
#   - long_description_content_type: Specifies the format of the long
#   description; in this case, Markdown.
#   - url: The URL to your project's main homepage, which is typically its
#   GitHub repository.
#   - packages: Tells setuptools to find packages to include.
#   find_packages(where='src') searches for packages in the src directory.
#   - package_dir: Indicates that the packages are located in the src directory.
#   - classifiers: A list of classifiers that describe your package. These are
#   used by PyPI to classify and filter packages. Make sure to adjust these to
#   match your project.
#   - python_requires: Specifies the Python versions your package is compatible
#   with.
#   - install_requires: A list of dependencies needed by your package to run.
#   Uncomment and modify the example to include any actual dependencies.
#   - entry_points: This makes your package executable from the command line.
#   It maps commands to functions. xkcd-pwd-gen will be the command to run your
#   script, mapped to main function in xkcd_pwd_gen.main.

###############################################################################
# IMPORTS
###############################################################################

from setuptools import setup, find_packages

###############################################################################
# SETUP
###############################################################################

setup(
    name='xkcd_pwd_gen',
    version='0.1.0',
    author='Greg Barbieri',
    author_email='gfbarbieir@gmail.com',
    description='A secure password generator inspired by XKCD.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gfbarbieri/xkcd_pwd_gen',
    packages=find_packages(where='xkcd_pwd_gen'),
    package_dir={'': 'xkcd_pwd_gen'},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'xkcd-pwd-gen=xkcd_pwd_gen.main:main',
        ],
    },
)
