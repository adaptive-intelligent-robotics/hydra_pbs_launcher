# FORKED FROM: Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# type: ignore
from pathlib import Path

from read_version import read_version
from setuptools import find_namespace_packages, setup

setup(
    name="hydra_pbs_launcher",
    version=read_version("hydra_plugins/hydra_pbs_launcher", "__init__.py"),
    author="Forked by Antoine Cully, Original authors: Jeremy Rapin, Jieru Hu, Omry Yadan",
    author_email="jrapin@fb.com, jieru@fb.com, omry@fb.com",
    description="PBS Submitit Launcher for Hydra apps",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/adaptive-intelligent-robotics/hydra_pbs_launcher/",
    packages=find_namespace_packages(include=["hydra_plugins.*"]),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 4 - Beta",
    ],
    install_requires=[
        "hydra-core>=1.1.0.dev7",
    ],
    include_package_data=True,
)
