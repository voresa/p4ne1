from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, a, b):
        IPv4Network.__init__(self, (a, b), strict=False)
    def key_value(self):
        return IPv4Network
#int(IPv4RandomNetwork())
#n1=random.randint(8, 24)
#print(n1)
i=1
while i < 5 :
    x = IPv4RandomNetwork(random.randint(0x0B000000, 0xDF000000), random.randint(8, 24))
    n = int(x())
    print(x)
    i = i+1
