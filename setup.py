from setuptools import setup
from configparser import ConfigParser
from typing import List

# TO FILL OUT LIB INFO AND REQUIREMENTS: edit the [metadata] and [options] sections
# of setup.cfg


# --- SETUP SCRIPT ---
if __name__ == "__main__":

    config = ConfigParser()
    config.read("./setup.cfg")

    lib_name = config.get("metadata", "name")
    version = config.get("version", "release")

    # filter packages to ones with the lib name in them
    packages: List[str] = ["service"]

    # run setup
    setup(version=version, packages=packages)
