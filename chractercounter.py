import pprint

print ('Hello, I am a chracter counter. I count the number of chracters in a string')
print ('Tell me the string you want me to count')
string = input()
count = {}

for char in string.upper():
    count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)
