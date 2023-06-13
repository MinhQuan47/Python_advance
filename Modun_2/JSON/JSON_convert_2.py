import json
import xmltodict
# read file xml
with open("D:\Python\Modun_2\XML\DT_XML\\items.xml") as file:
    data_xml = file.read()
# convert xml string to dictionary
data_dict = xmltodict.parse(data_xml)
# convert dictionary to json string
data_json = json.dumps(data_dict, indent=4)
# print xml string, dictionary, json string
print("type of data_xml:", type(data_xml))
print("type of data_dict:", type(data_dict))
print("type of data_json:", type(data_json))
print(data_json)