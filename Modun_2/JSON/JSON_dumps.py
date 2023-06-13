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
print("type of data_dict:", type(data_dict))
#convert dictionary to json string
data_string = json.dumps(data_dict,indent=4)
print("type of data_string:", type(data_string))
print(data_string)
