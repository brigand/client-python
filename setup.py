from setuptools import setup
import os

version_file = open(os.path.join(os.path.dirname(__file__), 'VERSION'))
VERSION = version_file.read().strip()

setup(
  name = 'sightengine',
  packages = ['sightengine'],
  version = VERSION,
  description = 'Sightengine Python client',
  author = 'Sightengine',
  author_email='support@sightengine.com',
  url = 'https://github.com/Sightengine/client-python'
)