from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in security/__init__.py
from security import __version__ as version

setup(
	name="security",
	version=version,
	description="security app is contain of every sigle move in/out the company ",
	author="yahia gamal",
	author_email="security@alshaheen.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
