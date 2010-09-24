import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(
    name = "django-pastebin",
    version = "0.1",
    packages = find_packages(),
    py_modules = ['setup', 'ez_setup'],
    author = "Agiliq and friends",
    author_email = "shabda@agiliq.com", 
    description = "A django based pastebin",
    url = "http://github.com/agiliq/django-pastebin",
    include_package_data = True
)
