from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description_readme = f.read()

setup(
    name="py_output_compare",
    description="a script that help compare output of 2 python script, I apply this to help grading student code compare to teacher",
    long_description=description_readme,
    long_description_content_type="text/markdown",
    version=0.5,
    package_dir={"": "py_output_compare"},
    packages=find_packages(where="py_output_compare"),
    author="meangpu",
    license="MIT",
    url="https://github.com/meangpu/py_output_compare",
    entry_points={"console_scripts": ["me_py = py_output_compare:hello"]},
)
