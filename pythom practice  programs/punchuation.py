import re
string = input("enter the string")

final_string = re.sub(r'[^\w\s]','',string)

print('String with Punctuation: ', string)
print('String without Punctuation: ', final_string)
