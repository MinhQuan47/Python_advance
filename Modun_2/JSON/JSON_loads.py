import json
data_string = """
{
"domainname": "pythonpcap.com",
"active": true,
"numberposts": 360,
"category": ["basic", "intermediate", "advanced"],
"facebookpage": "https://www.facebook.com/pythonpcap/",
"build": {
"language": "php",
"cms": "wordpress",
"database": "mysql"
}
}
"""
#convert json string to dictionary
data = json.loads(data_string)
# access value of key-value
print(data["domainname"])
print(data["active"])
print(data["numberposts"])
print(data["category"])
print(data["facebookpage"])
print(data["build"])
category = data["category"]
build = data["build"]
print("type of category:", 
type(category))
print("type of build:", type(build))
