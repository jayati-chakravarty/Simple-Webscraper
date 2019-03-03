import bs4
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#the URL which we need to parse
#myUrl ='https://www.amazon.in/s?rh=i%3Aelectronics%2Cn%3A976419031%2Cn%3A%21976420031%2Cn%3A1388921031%2Cp_85%3A10440599031%2Cp_89%3AAnt+Audio&amp;bbn=1388921031&amp;ie=UTF8'
myUrl='file:///C:/Users/LENOVO/webscrape/Amazon.in%20%20Prime%20Eligible%20-%20Ant%20Audio%20_%20Headphones%20%20Electronics.html'

#opening the Url
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

#parsing the URL
page_soup = soup(page_html, "html.parser")

#grab each product
containers = page_soup.findAll("div", {"class":"s-item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "Product, Brand_Name, Price, Original_Price, Discount(%)\n"
f. write(headers)

#making the list
for contain in containers :
   try: 
        product = contain.a.img["alt"]

        brand_array = contain.findAll("span",{"class":"a-size-small a-color-secondary"})
        brand_name = brand_array[1].text

        price_array = contain.findAll("span",{"class":"a-size-base a-color-price s-price a-text-bold"})
        price=price_array[0].text.strip()

        disc_array = contain.findAll("span",{"class":"a-size-small a-color-price"})
        discount = disc_array[0].text.strip()
        disc_tot=disc_array[0].text.strip()
        disc_rs=disc_tot[0:-5]
        original_price  = re.sub('[^0-9]','',disc_rs)  #print only the numeral value
        disc_per=disc_tot[-4:-1]

        f.write(product + "," + brand_name + "," + price.replace(",","") + "," + original_price.replace(",","") + ","+ disc_per + "\n")
   except IndexError:
        break

f.close()