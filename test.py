#! /usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'lei'


def addAllBit(num):
	"""
	add all bit num until sum less than 9
	:param num: int number
	:return:int number
	"""
	tempNum=num
	s=11
	while s>10:
		s=0
		while tempNum>0:
			curbit=tempNum%10
			s+=curbit
			tempNum/=10

		tempNum=s

	return s

def numToString(num):
	"""

	:param num:
	:return:
	"""

if __name__=="__main__":
	allsum=addAllBit(999)
	print(allsum)