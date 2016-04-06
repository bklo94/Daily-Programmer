#!/bin/bash
#this line is a comment
#display the day

#empties textfile
: >test.txt 

#appends date and uptime to text file
date >> test.txt
uptime -p >> test.txt

#exits scripts
exit 0
