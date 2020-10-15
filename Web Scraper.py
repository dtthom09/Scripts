from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as Soup

# website to scrape data from
my_url = 'https://www.newegg.com/p/pl?d=video+cards'

# opening up connection, grabbing the page
uClient = Ureq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = Soup(page_html, 'html.parser')

# testing to see that page_soup is getting html from url
page_soup.h1
page_soup.p

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})
len(containers)

for container in containers:
    title = container.div.div.a["title"]
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    