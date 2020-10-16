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

# creating csv file
filename = "products.csv"
f = open(filename, "w")

# call headers
headers = "brand, product_name, shipping\n"

# writes headers then starts a new line
f.write(headers)

for container in containers:
    title = container.div.a.img["title"]
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("title: " + title)
    print("product name: " + product_name)
    print("shipping: " + shipping)

    product_name.replace(",", ";")
    f.write(brand + "," + product_name + "," + shipping + "\n")

f.close()