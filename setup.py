#!/usr/bin/env python
from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt") as f:
        install_requires = []
        for line in f.readlines():
            req = line.strip()
            if not req or req.startswith("#") or "://" in req:
                continue
            install_requires.append(req)
    return install_requires


setup(
    name="eyeloop",
    description="EyeLoop is a Python 3-based eye-tracker tailored specifically to dynamic, "
    "closed-loop experiments on consumer-grade hardware.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/simonarvin/eyeloop",
    license="GPL",
    license_files=["LICENSE"],
    platforms="any",
    python_requires=">=3.10",
    version="0.36-dev",
    entry_points={"console_scripts": ["eyeloop=eyeloop.run_eyeloop:main"]},
    packages=find_packages(include=["eyeloop*"]),
    include_package_data=True,
    install_requires=read_requirements(),
    project_urls={
        "Documentation": "https://github.com/simonarvin/eyeloop",
        "Source": "https://github.com/simonarvin/eyeloop",
        "Tracker": "https://github.com/simonarvin/eyeloop/issues",
    },
)
