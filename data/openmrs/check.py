#!/usr/bin/env python
"""
Author: Chang Liu

Comment: This file is to check whether the file in the .xlsx are all in the
         database. We want to make sure the .xlsx file are not missing
"""
# open file list that is only in .xlsx files
checkfile = open("select_file.txt", "r+")

# open file list that is in database package
file = open("filelist.txt", "r+")

# file list for all these file
xls_files = checkfile.readlines()
db_files = file.readlines()

# check
for xls_file in xls_files:
    marker = False
    for db_file in db_files:
        if xls_file == db_file:
            print "Yes: %s" % str(xls_file)[:-1]
            marker = True
            break
    if marker == False:
        print "NO: %s" % str(xls_file)[:-1]

checkfile.close()
file.close()
