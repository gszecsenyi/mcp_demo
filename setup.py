"""Setup configuration for MCP Demo."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mcp_demo",
    version="0.1.0",
    author="MCP Demo Team",
    description="A simple Model Context Protocol demonstration with agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gszecsenyi/mcp_demo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
        ],
    },
)
