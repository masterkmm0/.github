from setuptools import setup, find_packages

setup(
    name="github-project",
    version="0.1.0",
    description="A Python project template for GitHub",
    author="masterkmm0",
    author_email="your.email@example.com",
    url="https://github.com/your-org/your-repo",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        # Add your dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    long_description="",
    long_description_content_type="text/markdown",
)
