# Import modules
import Constants

from xml.dom import minidom
import urllib2

dom = minidom.parse(urllib2.urlopen(Constants.URL))
date = dom.getElementsByTagName(Constants.LAST_UPDATED_DATE)
time = dom.getElementsByTagName(Constants.BORDER_WAIT_TIME)

print("Date :" + str(date))
print("Time :" + str(time))
ports = dom.getElementsByTagName(Constants.PORT)

i = 1
for port in ports:
    print("\t" + str(i) + "-PORTNUMBER-" + str(port.getElementsByTagName(Constants.PORT_NUMBER)))
    i += 1


#TODO MYSQL LOGIC