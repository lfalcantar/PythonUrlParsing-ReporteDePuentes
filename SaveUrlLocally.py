from xml.dom import minidom
import urllib2, Constants

dom = minidom.parse(urllib2.urlopen(Constants.URL))


#TODO logic to get file locally
