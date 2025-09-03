from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="laam-framework",
    version="0.1.0",
    author="Ruben Lopez",
    author_email="lopezruben189@yahoo.com",
    description="Lopez Audit Anchor Model - A game-theoretic framework for fair enforcement systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/LAAM-Framework",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
    ],
)
