from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/GPUs-Video-Graphics-Devices/Category/ID-38'

# opening up connection with html site
uClient = uReq(my_url)

# offloads content into var
# page_html = uClient.read()

uClient.close()

# parseHtml
page_soup = soup(page_html, "html.parser")
# getting the items by class @minute 15
containers = page_soup.findAll("div", {"class": "item-cell"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
    print(container.div.div.a)
    print('br')
    if container.div.div.a.img:
        brand = container.div.div.a.img["title"] if container.div.div.a.img["title"] else ''
        # print(brand)
        title_container = container.findAll("a", {"class", "item-title"})
        product_name = title_container[0].text

        shipping_container = container.findAll("li", {"class":"price-ship"})
        shipping = container.findAll("li", {"class":"price-ship"})
        shipping = shipping[0].text

        # print("brand: " + brand)
        # print("product_name: " + product_name)
        # print("shipping: " + shipping)

        f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")

f.close()