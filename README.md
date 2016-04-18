# Python developer for simple FTP pull script

Table of Contents
=================

...


## Original Descripions

### Task: Python developer for simple FTP pull script

> Details
> =======
> 
> Python developer wanted to write a script for retrieving a file from a sFTP server.
> Here's a step-by-step:
> 
> 1.  Connect to SFTP repository (Secure FTP)
> 2.  Identify files based on filename criteria
> 3.  Download these files to local folder
> 4.  Run an existing python script

## Installation and usage

1. source `install.sh`:
```
. ./install.sh
```
2. set up environment variables **FTP_USER** and **FTP_PWD** (or change the default value variable values in the script):
```
export FTP_USER=...
export FTP_PWD=...
```
3. run `download.py` to download files and run a post processing script:
```
. ./env/bin/activate
 ./download.py
```

## Getting Help

```
./download.py -h
```

>    usage: download.py [-h] [-u USER] [-p PWD] [--host HOST] [--src SRC]
>                       [--dst DST] [-s SCRIPT]
>    
>    Downloading and processing files from a SFTP server.
>    
>    optional arguments:
>      -h, --help            show this help message and exit
>      -u USER, --user USER  SFTP user (default: decmetrics)
>      -p PWD, --pwd PWD     SFTP user password (default: *********)
>      --host HOST           SFTP host (default: 31.3.230.106)
>      --src SRC             SFTP source directory (default: readings)
>      --dst DST             Destination directory (default: readings)
>      -s SCRIPT, --script SCRIPT
>                            Post processing script (default: importfile.py)


