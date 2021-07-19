# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Lab proxy stuff
import os

proxy = '172.31.42.7:3128'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = bytearray()

while True:
    url = input('Enter - ')
    # If nothing is entered, use google
    if len(url) < 1:
        url = "https://www.google.com"
        break
    # Check if its a valid URL, if not, restart loop
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        break
    except:
        print('Invalid website, try again')
        continue

# Remove duplicaiton of html assignments through use of not
if not html:    
    html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
