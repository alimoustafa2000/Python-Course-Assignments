# Regular Expression to match => (http://www.elzero.org:8888/link.php || https://elzero.org:8888/link.php || http://www.elzero.com/link.py || https://elzero.com/link.py)

# RegEx. => (https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+)

import re

my_string1 = "http://www.elzero.org:8888/link.php"
my_string2 = "https://elzero.org:8888/link.php"
my_string3 = "http://www.elzero.com/link.py"
my_string4 = "https://elzero.com/link.py"
my_string5 = "http://www.elzero.net"
my_string6 = "https://elzero.net"

result1 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string1)
result2 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string2)
result3 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string3)
result4 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string4)
result5 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string5)
result6 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string6)


print(result1)
# ['http://www.elzero.org:8888/link.php']
print(result2)
# ['https://elzero.org:8888/link.php']
print(result3)
# ['http://www.elzero.com/link.py]
print(result4)
# ['https://elzero.com/link.py]
print(result5)
# []
print(result6)
# []
