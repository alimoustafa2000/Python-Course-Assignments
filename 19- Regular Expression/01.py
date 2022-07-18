
# Regular Expression to match => (E-l-z-e-r-o) in this strint => "eeeeE llllLl lllzzZzzzz eroe operationr pollo"

# RegEx. => (\w )

import re

my_string = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "

result = re.findall(r"(\w )", my_string)

print(result)
# ['E ', 'l ', 'z ', 'e ', 'r ', 'o ']
