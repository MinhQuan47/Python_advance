import re


# fuc findall
str = "Xin chào Bạn! Bạn đang học bài Regex trong Python."
matches = re.findall("Bạn", str)

matches_1 = re.findall("Ban", str)
print(matches)
print(matches_1)


# fuc search
str = "Xin chào Bạn! Bạn đang học bài Regex trong Python."
matches = re.search("Bạn", str)
print(type(matches))
print(matches)


