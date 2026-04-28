from pathlib import Path
import re
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# read version without importing package
version_file = Path(__file__).parent / "erpnext_arabic_layout" / "__init__.py"
version_match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', version_file.read_text(), re.M)
if not version_match:
	raise RuntimeError("Unable to find version string in erpnext_arabic_layout/__init__.py")
version = version_match.group(1)

setup(
	name="erpnext_arabic_layout",
	version=version,
	description="Arabic Layout",
	author="ZamilTec",
	author_email="hello@zamiltec.com",
	packages=find_packages(
		include=["erpnext_arabic_layout", "erpnext_arabic_layout.*"],
		exclude=["erpnext_arabic_layout.erpnext_arabic_layout*"],
	),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
	classifiers=[
		"Framework :: Frappe",
		"Framework :: Frappe :: 15",
	],
)
