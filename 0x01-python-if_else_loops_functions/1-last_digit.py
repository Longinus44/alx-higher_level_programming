#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

lastnumber = abs(number) % 10
comment = f"Last digit of {number} is"

if number < 0:
    lastnumber = -lastnumber
if lastnumber > 5:
    print(f"{comment} {lastnumber} and is greater than 5")
elif lastnumber < 6:
    print(f"{comment} {lastnumber} and is less than 6 and not 0")
elif lastnumber < 0:
    print(f"{comment} {lastnumber} and is less than 6 and not 0")
else:
    print(f"{comment} {lastnumber} and is 0")
