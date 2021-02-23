from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="hama",
    version="1.0.1",
    description="Korean natural language toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.hamanlp.org",
    keywords="korean nlp natural language processing morpheme part of speech tagging",
    author="Seongmin Park",
    author_email="llov0708@gmail.com",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["mmh3"],
)
