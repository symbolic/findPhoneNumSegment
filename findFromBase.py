#-*- coding: utf-8 -*-
from phone import Phone


def test():
	p  = Phone()
	print p.find(1888888)
	print p.find(1888888)['province'].decode('utf-8')
	print p.find(1888888)['city'].decode('utf-8')
	print p.find(1888888)['phone_type'].decode('utf-8')

def find(cardSeg):
	userDefine = 90
	current = cardSeg * 10000 + userDefine
	p = Phone()
	fp = open('result.txt', 'a')

	while (current <= (cardSeg * 10000+9990)):
		print current
		
		if (p.find(current) != None):
			'''
			print p.find(current)
			print p.find(current)['province'].decode('utf-8')
			print p.find(current)['city'].decode('utf-8')
			print p.find(current)['phone_type'].decode('utf-8')
			'''
			fp.write(str(current)+' \t')
			fp.write(p.find(current)['province']+' \t')
			fp.write(p.find(current)['city']+' \t')
			fp.write(p.find(current)['phone_type']+'\n')
			
		current += 100
	
	fp.close()
	print 'finished'

def main():
	find(130)
	find(131)
	find(132)
	
	find(155)
	find(156)
	
	find(176)
	
	find(185)
	find(186)
	
if __name__ == '__main__':
	main()