from xml.dom import minidom
# parse file items.xml
file = minidom.parse('D:\Python\Modun_2\XML\DT_XML\\items.xml')
# use getElementsByTagName() to get tags
items = file.getElementsByTagName('item')
# one specific item attribute
print('Value of attribute name of item #2:')
print(items[1].attributes['name'].value)
# all attributes of item tags
print('\nAll values of attribute name:')
for elem in items:
    print(elem.attributes['name'].value)
# one specific item's data
print('\nData of item:')
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)
# all items data
print('\nAll item data:')
for elem in items:
    print(elem.firstChild.data)
