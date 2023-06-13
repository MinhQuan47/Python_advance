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
#convert dictionary to json string with sort_keys
data_string = json.dumps(data_dict, sort_keys=True,indent=4)
print(data_string)
