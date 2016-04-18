#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import argparse
import paramiko
import subprocess

DEFAULT_FTP_USER = "decmetrics"
DEFAULT_FTP_PWD = "x7tBN94wSCxx"
DEFAULT_HOST = "31.3.230.106"
DEFAULT_POST_SCRIPT = "importfile.py"
DEFAULT_SRC_DIR = "readings"
DEFAULT_DST_DIR = "readings"
DEFAULT_PATTERN = "southend_airport_20\d\d-\d\d-\d\d\.csv"


ftp_user = os.environ.get("FTP_USER", DEFAULT_FTP_USER)
ftp_pwd = os.environ.get("FTP_PWD", DEFAULT_FTP_PWD)

def help_str(format_str, *vargs):
    return format_str.format(*vargs)

parser = argparse.ArgumentParser(description="Downloading and processing files from a SFTP server.")
parser.add_argument("-u", "--user",
        help=help_str("SFTP user (default: {})", ftp_user), default=ftp_user)
parser.add_argument("-p", "--pwd", 
        help="SFTP user password (default: ********)", default=ftp_pwd)
parser.add_argument("--host", 
        help=help_str("SFTP host (default: {})", DEFAULT_HOST), default=DEFAULT_HOST)
parser.add_argument("--src", 
        help=help_str("SFTP source directory (default: {})", DEFAULT_SRC_DIR), 
        default=DEFAULT_SRC_DIR)
parser.add_argument("--dst", 
        help=help_str("Destination directory (default: {})", DEFAULT_DST_DIR),
        default=DEFAULT_DST_DIR)
parser.add_argument("-s", "--script", 
        help=help_str("Post processing script (default: {})", DEFAULT_POST_SCRIPT),
        default=DEFAULT_POST_SCRIPT)
parser.add_argument("-P", "--pattern", 
        help=help_str("Source file name pattern (default: {})", DEFAULT_PATTERN),
        default=DEFAULT_PATTERN)
args = parser.parse_args()

password = args.pwd
username = args.user
host = args.host
src_dir = args.src
dst_dir = args.dst
post_script = args.script
filename_re = re.compile(args.pattern)

port = 22
transport = paramiko.Transport((host, port))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

sftp.chdir(src_dir)
for fn in sftp.listdir():
    if filename_re.match(fn):
        sftp.get(fn, os.path.join(dst_dir, fn))

sftp.close()
transport.close()

if os.path.exists(post_script):
    subprocess.Popen(post_script, shell=True)
else:
    raise Exception("Missing post processing script {}".format(post_script))

