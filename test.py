# coding: utf8

import datetime,time,os

with open('a.txt', 'a+') as f:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(now)

with open('a.txt', 'r') as f:
    print f.read()

print 1
time.sleep(2)
print 2

envo = os.getenv('ENVO', None)
print "ENVO is {}".format(envo)
print "ENVO == test-11 : {}".format(envo == 'test-11')
print "TRAVIS_BUILD_NUMBER is {}".format(os.getenv('TRAVIS_BUILD_NUMBER', None))

