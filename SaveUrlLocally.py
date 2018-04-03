from xml.dom import minidom
import urllib2, Constants

file_name = "export.xml"

xml = urllib2.urlopen(Constants.URL)
contents = xml.read()
file = open("LOCALHOST/" + file_name, 'w')
file.write(contents)
file.close()