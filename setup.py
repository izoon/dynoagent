"""
DynoAgent setup configuration.
"""

from setuptools import find_packages, setup

# Read the contents of README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dynoagent",
    version="0.1.0",
    author="izoon",
    author_email="example@example.com",
    description="A dynamic role-based agent framework for complex task execution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/izoon/dynoagent",
    project_urls={
        "Bug Tracker": "https://github.com/izoon/dynoagent/issues",
        "Documentation": "https://dynoagent.readthedocs.io/",
        "Source Code": "https://github.com/izoon/dynoagent",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "networkx>=2.6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0",
            "pytest-cov>=6.0",
            "pytest-asyncio>=0.26.0",
            "flake8>=7.0.0",
            "black>=24.0",
            "isort>=5.13.0",
        ],
        "docs": [
            "sphinx>=7.0",
            "sphinx-rtd-theme>=2.0",
            "myst-parser>=2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dynoagent=dynoagent.cli:main",
        ],
    },
)
