# coding: utf8

import datetime,time

with open('a.txt', 'a+') as f:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(now)

with open('a.txt', 'r') as f:
    print f.read()

print 1
time.sleep(10)
print 2
print "2018-11-05"
