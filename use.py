import requests
import time
import os
import classify


def getData(lastfile):
	weatherfile = requests.get("http://opendata.cwb.gov.tw/opendataapi?dataid=O-A0001-001&authorizationkey=CWB-A7A69CF2-28D1-4E1E-B5C4-32548E120BAC")
	filename = time.strftime("%F %H-%M-%S")+'.txt'
	data = open(filename,'w',encoding = 'UTF8')
	data.write(weatherfile.text)
	data.close()
	
	if compare(lastfile, filename):
		classify.classified(filename)
		os.remove(lastfile)
		return filename
	
	else:
		os.remove(filename)
		return lastfile

def timer(n):
	lastfile = '2018-01-25 12-34-11.txt'
	while True
		lastfile = getData(lastfile)
		
		time.sleep(n)

def compare(old,new):
	olddata = open(old,'r',encoding='UTF-8')
	oldline = olddata.readlines()
	newdata = open(new,'r',encoding='UTF-8')
	newline = newdata.readlines()
	temp = 0
	for i in range(0,200):
		#print (oldline[i])
		if oldline[i] != newline[i]:
			#print ('in')
			temp = temp+1
			
	olddata.close()
	newdata.close()
	#print (temp)
	if temp>5:
		return True
	else:
		return False




timer(1200)




