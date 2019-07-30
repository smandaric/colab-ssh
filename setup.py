import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colabssh",
    version="0.0.1",
    author="Stefan Mandaric",
    author_email="stefan.mandaric@gmail.com",
    description="Copy SSH keys from Google Drive to Colaboratory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smandaric/colabssh",
    packages=['colabssh'],
    install_requires=['PyDrive',],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)