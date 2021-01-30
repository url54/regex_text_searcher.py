# This program was designed for an assignment, where we used regular expressions
# to assist in pulling out all of the number values in a text file, regex_sum_113910.
# We were tasked with pulling out the numbers then summing them up to equal a secret value
# that we were told ends with the last three digits being "618".   I have saved the text file
# that we used with this program in this repository.  The instructions for the
# problem are listed below.

#Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
# We provide two files for this assignment. One is a sample file where we give you the
# sum for your testing and the other is the actual data you need to process for the assignment.
# regex_sum_1139130.txt (There are 96 values and the sum ends with 618). 

import re

fname = 'regex_sum_1139130.txt'
hdle = open(fname)
nmlst = list()
for lne in hdle:
    lne = lne.strip()
    for wds in lne.split():
        nms = re.findall('([0-9]+)', wds)
        nlist = [int(i) for i in nms]
        if len(nlist) == 0:
            continue
        nmlst.append(sum(nlist))
print(sum(nmlst))
