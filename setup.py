"""ezTrack setup script."""

import os
from setuptools import setup, find_packages

# Get the current version number from inside the module
with open(os.path.join('ezTrack', 'version.py')) as version_file:
    exec(version_file.read())

# Load the long description from the README
with open('README.md') as readme_file:
    long_description = readme_file.read()

# Load the required dependencies from the requirements file
with open("requirements.txt") as requirements_file:
    install_requires = requirements_file.read().splitlines()

setup(
    name = 'ezTrack',
    version = __version__,
    description = 'Module for fast tracking.',
    long_description = long_description,
    long_description_content_type = 'text/x-rst',
    python_requires = '>=3.6',
    maintainer = '',
    maintainer_email = '',
    url = 'https://github.com/denisecailab/ezTrack/',
    packages = find_packages(),
    license = 'GPL, 3.0',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GPL',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    platforms = 'any',
    project_urls = {
        'Documentation' : '',
        'Bug Reports' : 'https://github.com/denisecailab/ezTrack/issues',
        'Source' : 'https://github.com/denisecailab/ezTrack/'
    },
    download_url = 'https://github.com/denisecailab/ezTrack/releases',
    keywords = ['neuroscience', 'tracking', 'real time', 'mouse'],
    install_requires = install_requires,
    extras_require = {
        "stats" : ["statsmodels"],
    },
    tests_require = ['pytest'],
)
