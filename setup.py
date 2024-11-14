from setuptools import setup, find_packages

setup(
    name="GeneralChordType",  # Replace with your package name
    version="0.1.0",   # Version of your package
    description="Functions to compute the General Chord Type from numpy chords or MusicXML files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/mypackage",  # Link to the repository
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
