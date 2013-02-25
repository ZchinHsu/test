#!/usr/bin/python
#coding=utf-8

import time, datetime, sys

#input: 2013-2-23

dateStr = sys.argv[1]

dateArray = dateStr.split('-')
for i in range(3):
	dateArray.append(0)

date = datetime.datetime(int(dateArray[0]), int(dateArray[1]), int(dateArray[2]), int(dateArray[3]), int(dateArray[4]), int(dateArray[5]))
timeKey = time.mktime(date.timetuple())

print int(timeKey)
