import random
from string import ascii_letters
from string import digits

def password(length):
    characters = ascii_letters + digits + "@$&|?=!~"
    pw = str()
    for i in range(length):
         pw = pw + random.choice(characters)
    return pw

pw = password(8)
print(pw)


