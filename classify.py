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
		
		if tempheader == 'lat' or tempheader == 'lon' or tempheader == 'locationName' or tempheader == 'obsTime':
			dataset[tempheader] = getvalue(temp) + ','
			continue
		
		elif tempheader == 'stationId':
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
			
			dataset[ele] = val + ','
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
			dataset[par] = val + ','
			if par == 'TOWN_SN':
				dataset[par] = val + '\n'
			
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
	temp = dataset['lat'] + dataset['lon'] + dataset['locationName'] + dataset['stationId'] + ',' + dataset['obsTime'] + dataset['ELEV'] + dataset['WDIR'] + dataset['WDSD'] + dataset['TEMP'] + dataset['HUMD'] + dataset['PRES'] + dataset['SUN'] + dataset['H_24R'] + dataset['H_FX'] + dataset['H_XD'] + dataset['H_FXT'] + dataset['CITY'] + dataset['CITY_SN'] + dataset['TOWN'] + dataset['TOWN_SN']
#	for k,v in dataset.items():
#		if k == 'lat' :
#			temp = temp + v
#		elif k == 'TOWN_SN':
#			temp = temp + v + '\n'
#			break
	
	f.write(temp)
	f.close()



#transData()
