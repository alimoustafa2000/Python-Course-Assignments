# Regular Expression to match => (http || https) by 5 methods.

# RegEx. 1 => https?
# RegEx. 2 => http\w?
# RegEx. 3 => http.?
# RegEx. 4 => http[a-z]?
# RegEx. 5 => http\S?

import re

my_string = "http || https || abcd || abcd"

result = re.findall(r"(http\w?)", my_string)

print(result)
#['http', 'https']
