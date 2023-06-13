import json
filepath = "D:\\Python\\Modun_2\\JSON\\JSON_DATA\\info.json"
with open(filepath, 'r') as f:
    data = json.load(f)
# access value of key-value
print(data["domainname"])
print(data["active"])
print(data["numberposts"])
print(data["category"])
print(data["facebookpage"])
print(data["build"])
category = data["category"]
build = data["build"]
print("type of category:", type(category))
print("type of build:", type(build))
