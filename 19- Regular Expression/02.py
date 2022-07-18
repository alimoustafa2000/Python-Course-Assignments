# Regular Expression to match => (LElzero) in this strint => "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"

# RegEx. => (L[A-z]+)

import re

my_string = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"

result = re.findall(r"(L[A-z]+)", my_string)

print(result)
# ['LElzero']
