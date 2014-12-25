#!/usr/bin/env python

from setuptools import setup, find_packages
from UCloud import version

url="https://github.com/jeffkit/UCloud"

long_description="UCloud(UCloud.cn) Python SDK"

setup(name="ucloud-py",
      version=version,
      description=long_description,
      maintainer="jeff kit",
      maintainer_email="bbmyth@gmail.com",
      url = url,
      long_description=long_description,
      packages=find_packages('.'),
     )


