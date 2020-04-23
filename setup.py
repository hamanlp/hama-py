from setuptools import setup, find_packages

with open("README.md", "r") as fh:
        long_description = fh.read()

setup(name="hama",
      version="1.0.0",
      description="Korean natural language toolkit",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/hamanlp/hama-py",
      keywords=
      'korean nlp natural language processing morpheme part of speech tagging',
      author="Seongmin Park",
      author_email="llov0708@gmail.com",
      license="MIT",
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      include_package_data=True)
