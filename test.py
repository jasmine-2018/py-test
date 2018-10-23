# coding: utf8

import datetime,time,os

with open('a.txt', 'a+') as f:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(now)

with open('a.txt', 'r') as f:
    print f.read()

print 1
time.sleep(10)
print 2
print 3

print(os.environ.get("USER", "USER_MOCK"))
print(os.environ.get("TRAVIS_BRANCH", "TRAVIS_BRANCH_MOCK"))
