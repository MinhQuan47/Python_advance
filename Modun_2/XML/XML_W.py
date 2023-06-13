from bs4 import BeautifulSoup
# create an empty xml document
soup = BeautifulSoup(features='xml')
# create data tag as root tag
data = soup.new_tag("data")
soup.append(data)
# create child tag of data tag
items = soup.new_tag("items")
data.append(items)
# create child tag of items
item1 = soup.new_tag('item')
item1.string = "book"
item1["name"] = "item1"
item1["price"] = "5"
items.append(item1)
item2 = soup.new_tag('item')
item2.string = "chair"
item2["name"] = "item2"
item2["price"] = "15"
items.append(item2)
item3 = soup.new_tag('item')
item3.string = "window"
item3["name"] = "item3"
item3["price"] = "20"
items.append(item3)
# create a new XML file
filepath = "D:\Python\Modun_2\XML\DT_XML\\items_1.xml"
myxmlfile = open(filepath, "w")
myxmlfile.write(soup.prettify())
myxmlfile.close()
