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

# skip first 3 ads
for container in containers[3:]:
    # getting values from html for each video card
    brand_container = container.find("div", {"class": "item-branding"})
    brand = brand_container.img["title"]
    title_container = container.find("a", {"class": "item-title"})
    product_name = title_container.text
    shipping_container = container.find("li", {"class": "price-ship"})
    shipping = shipping_container.text.strip()

    # replacing commas with semicolons to prevent parsing values
    brand = brand.replace(",", ";")
    product_name = product_name.replace(",", ";")
    shipping = shipping.replace(",", ";")
    # writing all products to csv file
    f.write(brand + "," + product_name + "," + shipping + "\n")

f.close()
