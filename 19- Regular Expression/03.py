# Regular Expression to match => (+(0100) 600-1234 || +(0100) 60-1234 || (0100) 6000-1234)

# RegEx. => (\+?)(\(0100\))\s(\d{,4})-(\d{4})

import re

my_string1 = "+(0100) 600-1234"
my_string2 = "+(0100) 60-1234"
my_string3 = "(0100) 6000-1234"
my_string4 = "01006001234"
my_string5 = "0100 600 1234"
my_string6 = "(0100) 600-1"
my_string7 = "(0100) 600-12"


result1 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string1)
result2 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string2)
result3 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string3)
result4 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string4)
result5 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string5)
result6 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string6)
result7 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string7)



print(result1)
# ['+(0100) 600-1234']
print(result2)
# ['+(0100) 60-1234']
print(result3)
# ['(0100) 6000-1234']
print(result4)
# []
print(result5)
# []
print(result6)
# []
print(result7)
# []
