# update version in setup.py once then run this script
. .\sh_update_local.ps1


twine check dist/*
# twine upload dist/*

# pip install py_output_compare -U
