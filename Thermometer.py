#!/usr/bin/python
ID1 = '28-0000069ffbec' # THIS VALUE MUST BE CONFIGURED !!! Unique number
ID2 = '28-000006a0164b'
ID3 = '28-000006a01af1'
ID4 = '28-000006a04ee0'

def gettemp(id):
    try:
        mytemp = ''
	filename = 'w1_slave'
	f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
	line = f.readline() #read first line
	crc = line.rsplit(' ',1)
	crc = crc[1].replace('\n', '')
	if crc=='YES':
	    line = f.readline() #read second line
	    mytemp = line.rsplit('t=',1)
	else:
	    mytemp = 99999
	f.close()

	return int(mytemp[1])

    except:
	return 99999

if __name__ == '__main__':

    print "Temp1 UP : " + '{:.3f}'.format(gettemp(ID1)/float(1000))
    print "Temp1 DOWN : " + '{:.3f}'.format(gettemp(ID2)/float(1000))
    print "Temp2 UP : " + '{:.3f}'.format(gettemp(ID3)/float(1000))
    print "Temp2 DOWN : " + '{:.3f}'.format(gettemp(ID4)/float(1000))
