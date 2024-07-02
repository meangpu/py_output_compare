# run update local
. .\sh_update_local.ps1


# create file name
$credentialsPath = "credential.txt"
$credentials = Get-Content $credentialsPath | ConvertFrom-StringData

twine check dist/*
twine upload -u $credentials.username -p $credentials.password dist/*