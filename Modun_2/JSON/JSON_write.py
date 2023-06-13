import json
data_dict = {
    "domainname": "pythonpcap.com",
    "active": True,
    "numberposts": 360,
    "category": ["hardware", "software", "network"],
    "facebookpage": "https://www.facebook.com/pythonpcap/",
    "build": {
        "language": "php",
        "cms": "wordpress",
        "database": "mysql"
}
}
#convert dictionary to json string with sort_keys and indent
data_string = json.dumps(data_dict, sort_keys=True, indent=4)
# write json string to file
myjsonfile = open("D:\\Python\\Modun_2\\JSON\\JSON_DATA\\info.json", "w")
myjsonfile.write(data_string)
myjsonfile.close()

