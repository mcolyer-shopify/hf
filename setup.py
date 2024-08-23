from setuptools import setup, find_packages

setup(
    name="hf",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fire",
        "huggingface_hub"
    ],
    entry_points={
        "console_scripts": [
            "hf=hf.cli:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to list discussions on a Hugging Face repo",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hf",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
