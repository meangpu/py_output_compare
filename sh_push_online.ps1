# run update local
. .\sh_local_update.ps1


# create file name
$credentialsPath = "credential.txt"
$credentials = Get-Content $credentialsPath | ConvertFrom-StringData

twine check dist/*
twine upload -u $credentials.username -p $credentials.password dist/*


git add .
git commit -m "update script version"
git push origin main

