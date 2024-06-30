python .\setup.py sdist bdist_wheel
pip install .\dist\py_output_compare-0.6-py3-none-any.whl --force-reinstall



# twine check dist/*
# twine upload dist/*
# To enter api token cannot use ctrl+v or right click, need to use Edit>paste

