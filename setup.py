from setuptools import setup, find_packages

setup(
    name="py_output_compare",
    description="a script that help compare output of 2 python script, I apply this to help grading student code compare to teacher",
    version=0.1,
    packages=find_packages(),
    author="meangpu",
    license="MIT",
    url="https://github.com/meangpu/py_output_compare",
    install_requires=["pytest"],
)
