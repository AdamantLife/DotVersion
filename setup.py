import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DotVersion",
    version="0.0.1",
    author="AdamantLife",
    author_email="",
    description="A container class to allow for easy comparisons between versions with dot-dilineation (i.e.- 1.2.03.40)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdamantLife/DotVersion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "al_decorators @ git+https://github.com/AdamantLife/AL_Decorators"
        ]
)
