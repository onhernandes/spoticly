"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from spoticly import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.md"), encoding="utf-8") as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""

    description = "run tests"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(["py.test", "--cov=spotify", "--cov-report=term-missing"])
        raise SystemExit(errno)


setup(
    name="spoticly",
    version=__version__,
    description="A spotify cli app",
    long_description=long_description,
    url="https://github.com/onhernandees/spoticly",
    author="Hernandes",
    author_email="midia.matheus@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="cli",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=[
        "docopt",
        "pyyaml",
        "requests",
        "PyInquirer",
        "spotipy"
    ],
    extras_require={"test": ["coverage", "pytest", "pytest-cov"]},
    entry_points={"console_scripts": ["spoticly=spoticly.cli:main"]},
    cmdclass={"test": RunTests},
)
