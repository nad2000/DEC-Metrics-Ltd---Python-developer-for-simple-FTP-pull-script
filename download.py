#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import datetime
import argparse
import paramiko
import subprocess

DEFAULT_FTP_USER = "decmetrics"
DEFAULT_FTP_PWD = "x7tBN94wSCxx"
DEFAULT_HOST = "31.3.230.106"
DEFAULT_POST_SCRIPT = "./importfile.py"
DEFAULT_SRC_DIR = "readings"
DEFAULT_DST_DIR = "readings"
DEFAULT_PREFIX = "southend_airport"


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
parser.add_argument("-P", "--prefix", 
        help=help_str("Source file name prefix (default: {})", DEFAULT_PREFIX),
        default=DEFAULT_PREFIX)
args = parser.parse_args()

password = args.pwd
username = args.user
host = args.host
src_dir = args.src
dst_dir = args.dst
post_script = args.script
prefix = args.prefix

port = 22
transport = paramiko.Transport((host, port))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

src_file_name = prefix + "_" + datetime.date.today().strftime("%Y-%m-%d") + ".csv"
dst_file_name = os.path.join(dst_dir, src_file_name)
sftp.chdir(src_dir)

if src_file_name in sftp.listdir():
    print "*** Processing: ", src_file_name
    sftp.get(src_file_name, dst_file_name)
    if os.path.exists(post_script):
        subprocess.Popen(post_script + " " + dst_file_name, shell=True)
    else:
        raise Exception("Missing post processing script {}".format(post_script))
else:
    print "*** File", src_file_name, "not found."

sftp.close()
transport.close()

