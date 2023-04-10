import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    log_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'cnnClassifire'
AUTHOR_USER_NAME = 'deasadiqbal'
SRC_REPO = 'cnnClassifire'

setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description= ' small python package for CNN app',
    package_dir= {'': 'src'},
    packages= setuptools.find_packages(where='src')
)
