# py_output_compare

a python package that create to help compare output of 2 python script, I apply this to help grading student code compare to teacher

# note to myself

## to make it auto login to twine

1. create `pip.ini` at `%APPDATA%\pip\pip.ini`, then add following content

> content of `pip.ini`

```ini
[global]
index = https://$username:$password@pypi.example.com/pypi
index-url = https://$username:$password@pypi.example.com/simple
cert = /etc/ssl/certs/ca-certificates.crt
```

`pip config list`

2. then create `.env` file with this content

```
export username=meangpu
export password=password("the long token pypi-xxxxx)
```
