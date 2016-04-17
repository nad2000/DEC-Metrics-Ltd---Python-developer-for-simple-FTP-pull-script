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

1. source `intall.sh`:
```
. ./install.sh
```

2. set up environment variables **FTP_USER** and **FTP_PWD** (or change the default value variable values in the script):

```
export FTP_USER=...
export FTP_PWD=...
```

3. run `download.py` to download ZIP file:

```
 ./download.py
```

4 to download XLS workbooks:

```
 ./download_xls.py
```

## Usage with MS Windows

1. set up environment variables **IEA_USER** and **IEA_PWD** (or change the default value variable values in the script):

```
set IEA_USER=...
set IEA_PWD=...
```

2. run `download.py`:

```
python3 ./download.py
```
