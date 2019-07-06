# save the bing background picture

import urllib.request
page = urllib.request.urlopen('https://cn.bing.com')
bing_web_content = page.read()

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

#parsed_html = BeautifulSoup(bing_web_content, features="html5lib")
parsed_html = BeautifulSoup(bing_web_content, features="html.parser")

image_link = parsed_html.head.link

#inputTag = parsed_html.findAll(attrs={"id":"bgLink"})
#output = inputTag[0]
#print(output)
#print(output['href'])

image_link_string = image_link['href']

image_url = image_link_string.split('&')

pic_url = 'https://cn.bing.com/' + image_url[0]

pic_name = image_url[0][11:]

urllib.request.urlretrieve(pic_url, pic_name)

print('The picture ' + pic_name + ' is saved.')
