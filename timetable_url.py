#!usr/bin/env python
import sys

def urlgen():
    default_dcu_tt = 'https://www101.dcu.ie/timetables/feed.php?prog=_&per=_&_&hour=1-28&template=student'
    
    default_dcu_tt = default_dcu_tt.split('_')
    
    sem1 = 'week1=1&week2=12'
    sem2 = 'week1=20&week2=31'
    
    prog = raw_input('Please enter your program: ')
    year = raw_input('Please enter your year: ')
    sem = raw_input('Please enter your semester: ')
    
    if sem == '1':
        sem = sem1
    else:
        sem = sem2

    url = ''
    url = default_dcu_tt[0] + prog + default_dcu_tt[1] + year + default_dcu_tt[2] + sem + default_dcu_tt[3]
    return url
    
tt_url = urlgen()
print tt_url

