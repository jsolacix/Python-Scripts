#!/usr/bin/python
import requests
import thermometer 
import time
import datetime

if __name__ == '__main__':

    temp1up = thermometer.gettemp(thermometer.ID1)/float(1000)
    temp1down = thermometer.gettemp(thermometer.ID2)/float(1000)
    temp2up = thermometer.gettemp(thermometer.ID3)/float(1000)
    temp2down = thermometer.gettemp(thermometer.ID4)/float(1000)
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime(' %Y-%m-%d %H:%M:%S')
    data = {'Temp 1 Up': temp1up,'Temp 1 Down': temp1down,'Temp 2 Up': temp2up,'Temp 2 Down': temp2down, 'Time': timestamp}
    r = requests.post("http://httpbin.org/post", data)
    print(r.text)
