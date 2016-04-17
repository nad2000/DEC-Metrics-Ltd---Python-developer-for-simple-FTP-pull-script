#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import paramiko

default_ftp_user = ""
default_ftp_pwd = ""

ftp_user = os.environ.get("FTP_USER", default_ftp_user)
ftp_pwd = os.environ.get("FTP_PWD", default_ftp_pwd)

parser = argparse.ArgumentParser(description="Retrieving a file from a sFTP server.")
parser.add_argument('u', "user", help="FTP user", default=ftp_user)
parser.add_argument('p', "pwd", help="FTP user password", default=ftp_pwd)
args = parser.parse_args()

host = "THEHOST.com"                    #hard-coded
port = 22
transport = paramiko.Transport((host, port))

password = "THEPASSWORD"                #hard-coded
username = "THEUSERNAME"                #hard-coded
transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport(transport)

import sys
path = './THETARGETDIRECTORY/' + sys.argv[1]    #hard-coded
localpath = sys.argv[1]
sftp.put(localpath, path)

sftp.close()
transport.close()
print 'Upload done.'

source_url = "http://mods.iea.org/sdbs/supply.zip"
destination_filename = source_url.split('/')[-1]

req = requests.get(source_url, auth=(ftp_user, ftp_pwd), stream=True)
if req.status_code != 200:
    print("*** Failed to connect. Status code: {}".format(req.status_code))
    exit(-1)

with open(destination_filename, "wb") as f:
    for chunk in req.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

print("*** {} downloaded into {}".format(source_url, destination_filename))


