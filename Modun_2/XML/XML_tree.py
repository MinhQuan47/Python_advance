# importing element tree
import xml.etree.ElementTree as ET
# Pass the path of the xml document
tree = ET.parse("D:\Python\Modun_2\XML\DT_XML\\items.xml")
# get the root tag
root = tree.getroot()
# print the root tag along with its memory location
print(root)
# print the text contained within first subtag of the 0th tag from the root
print(root[0][0].text)
# print the attributes of the first subtag of the 0th tag from the root
print(root[0][0].attrib)
