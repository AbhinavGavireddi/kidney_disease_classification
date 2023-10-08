import setuptools


with open('README.md','r',encoding='utf-8') as f:
    description = f.read()

__version__ = '0.0.0'

REPO_NAME = "KIDNEY_DISEASE_CLASSIFICATION"
AUTHOR_NAME = "AbhinavGavireddi"
SRC_REPO = "CNN_clasifier"
AUTHOR_EMAIL = "abhinavgavireddi@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    description="A python package for CNN app",
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    long_description=description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)