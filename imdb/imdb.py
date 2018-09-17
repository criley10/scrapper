from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

print(page_soup.title.text)

containers = page_soup.findAll('td',{'class':'titleColumn'})
input("press")
for container in containers :
	a, b = container.div.text.split("(")
	print(a , container.a.text + " " + container.span.text)
input('press')