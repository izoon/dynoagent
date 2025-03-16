from setuptools import setup

setup(
    name="dynoagent",
    version="0.1.0",
    packages=["dynoagent"],
    package_dir={"dynoagent": "."},
    install_requires=[
        "numpy",
        "networkx",
        # Add these as stub dependencies since they're clearly external packages
        # that will need to be installed separately or from other repositories
    ],
    description="Core agent framework for DynoFrame",
    author="izoon",
    author_email="example@example.com",
    url="https://github.com/izoon/dynoagent",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
) 