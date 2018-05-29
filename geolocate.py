#from bs4 import BeautifulSoup
#import urllib
#r = urllib.urlopen('https://www.whatismyip.com/').read()
#soup = BeautifulSoup(r)
#print type(soup)

import requests
from bs4 import BeautifulSoup
import re
 
#set the user-agent to the one specified by whatismyip.com
header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0',}
 
#the url we want to grab the ip from
url = r'http://whatismyip.com'
#build the request, with the proper user-agent in the custom header
r = requests.get(url, headers=header)
 
#convert html to soup
soup = BeautifulSoup(r.content)
#find the line with the ip in it
# which is in a div, with id 'ip'
ip = soup.findAll('li', {'class': 'list-group-item'})[0]
#then, convert the HTML entities
raw_public_ip = BeautifulSoup(ip.text)
 
#match this regexp '[0-9].*?(?=N)'
# or '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
# or ([0-9]{1,3}\.){3}([0-9]{1,3})
#compile the regex pattern for re
#pattern = re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
pattern = re.compile('([0-9]{1,3}\.){3}([0-9]{1,3})')
#find the first instance of the patter in the string raw_public_ip's text attribute
public_ip = re.search(pattern, raw_public_ip.text)
 
#print it out
print 'Your Public IP is: {}'.format(public_ip.group(0))
