import requests
import time
import os

def transData():
	classified(dataname)


def classified(datasheet):
	f = open(datasheet,'r',encoding = 'UTF-8')
	
	dataset = {}
	for i in open(datasheet,'r',encoding = 'UTF-8'):
	#for i in range(0,34794):
		temp = f.readline()
		
		tempheader = getheader(temp)
		
		if tempheader == 'lat' or tempheader == 'lon' or tempheader == 'locationName' or tempheader == 'stationId' or tempheader == 'obsTime':
			dataset[tempheader] = getvalue(temp)
			continue
		
		elif tempheader == 'weatherElement':
			ele = ''
			val = ''
			while ele != 'elementName':
				temp = f.readline()
				ele = getheader(temp)
			ele = getvalue(temp)
			
			while val != 'value':
				temp = f.readline()
				val = getheader(temp)
			val = getvalue(temp)
			
			dataset[ele] = val
			continue
			
		elif tempheader == 'parameter':
			par = ''
			val = ''
			while par != 'parameterName':
				temp = f.readline()
				par = getheader(temp)
			par = getvalue(temp)
			
			while val != 'parameterValue':
				temp = f.readline()
				val = getheader(temp)
			val = getvalue(temp)
			dataset[par] = val
			
			continue
			
		elif tempheader == '/location':
			save(dataset)
			dataset.clear()
			continue
	
	f.close()




def getheader(line):
	temp = ''
	for i in range(len(line)):
		if line[i] != '<':
			continue
		i += 1
		while line[i] != '>':
			temp += line[i]
			i += 1
		break
	
	return temp
			
	
def getvalue(line):
	temp = ''
	for i in range(len(line)):
		if line[i] != '>':
			continue
		i += 1
		while line[i] != '<':
			temp += line[i]
			i += 1
		break
	
	return temp


def save(dataset):
	file = time.strftime('%Y-%m')
	if not os.path.isdir(file):
		os.mkdir(file)
	
	filename = file + '/' + dataset['stationId'] + time.strftime('-%Y-%m') + '.txt'
	f = open(filename,'a',encoding = 'UTF-8')
	temp = ''
	for k,v in dataset.items():
		if k != 'TOWN_SN' :
			temp = temp + v + ',' 
		elif k == 'TOWN_SN':
			temp = temp + v + '\n'
			break
	
	f.write(temp)
	f.close()



#transData()
