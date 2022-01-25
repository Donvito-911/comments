from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Social Media miner comments'
LONG_DESCRIPTION = 'A package that allows to recolect in databases the comments of users in facebook, instagram and twitter posts'

# Setting up
setup(
    name="comments",
    version=VERSION,
    author="Donvito (Daniel Aguirre)",
    author_email="<danielaguirre722@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'pandas'],
    keywords=['python', 'comments', 'social media', 'twitter', 'facebook', 'instagram'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)