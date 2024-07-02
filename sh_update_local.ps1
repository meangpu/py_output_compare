# update version in setup.py once then run this script

# remove old  file
$folderPath = "./dist"
$files = Get-ChildItem -Path $folderPath -File
foreach ($file in $files) {
    Remove-Item -Path $file.FullName
}

# update version
python .\update_version.py

# build new file version
python .\setup.py sdist bdist_wheel

$filePattern = "py_output_compare-*.whl"
$targetFile = Get-ChildItem -Path $folderPath -Filter $filePattern
Write-Host installing $targetFile

# install
pip install .\dist\$targetFile --force-reinstall