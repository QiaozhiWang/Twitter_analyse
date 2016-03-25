import re

text = "RT @Qiaozhi: @Betty @Wang is super #clever! 📚 📚  http://complicated.solve"
print(text)

#text = re.sub(r'RT\s@\w+:', "", text)
text = re.sub(r'RT\s@\w+:|@\w+|#|http://.*$|http://.*\s', "", text)

print("new: ",text)

"""
if text.startswith("RT"):
	text = text[3:]
if "@" in text:
	atpos = text.find('@')
	print(atpos)
	depos = text.find(':',atpos)
if text.index('#'):
	tagpos = text.find('#')
	text = text[0:tagpos-1]+' '+text[tagpos+1:]
	print(text)
"""