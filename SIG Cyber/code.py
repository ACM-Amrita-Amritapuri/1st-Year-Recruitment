# test = ####REDACTED####
#What a wonderful welcome message to the CTF to test
#flag = ###REDACTED#####

import base64
from itertools import cycle


key = ####REDACTED######   

def xor(a,b) :
    return ''.join(chr(ord(i)^ord(j)) for i,j in zip(a,cycle(b)))

c1 = base64.b16encode(xor(test,key).encode())
c2 = base64.b16encode(xor(flag,key).encode())

print(c1,c2,key)
#Hint : Would it matter if my welcome message and flag share a word?who cares..I've used a strong key

c1 = "0e0a193c0802117f0007452b0300591a0714330b0a1a38111b"
c2 = "382c3824050e076e375d3a6f2d3a21491d2a6e2930372d2d38526f16"

#flag format = ACM{....}