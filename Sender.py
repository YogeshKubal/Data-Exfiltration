import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

IPAddr = sys.argv[1]
Interface = sys.argv[2]
Type = sys.argv[3]
Message = sys.argv[4]

if(len(sys.argv)>5):
    for x in range (5, len(sys.argv)):
        Message = Message +" "+sys.argv[x]

#print (IPAddr)
#print (Interface)
#print (Type)
#print (Message)

#for l in list(Message):
#    a = hex(ord(l))
#    a = int(a,16)
#    b = int('0x41',16)
#    c = a*256 + b
#    print(a)
#    print(b)
#    print(c)
#    ls(IP(dst=IPAddr, id=c)/ICMP())

    #print(hex(ord(l))+0x41)

b = int('0x41',16)
frag_no = 0

#ls(IP(dst=IPAddr, id=c/ICMP())
#send(IP(dst=IPAddr)/ICMP()/Message)

if Type == "0":
#    print ("Inside 0")
    for l in list(Message):
        a = hex(ord(l))
        a = int(a,16)
        c = a*256 + b
        send((IP(dst=IPAddr, id=c, frag = frag_no)/ICMP()), iface=Interface)
        frag_no += 1
#        print(hex(ord(l)))
    send((IP(dst=IPAddr, id=b, frag = (1*16*16*16+frag_no))/ICMP()), iface=Interface)

elif Type == "1":
#    print ("Inside 1")
    for l in list(Message):
        a = hex(ord(l))
        a = int(a,16)
        c = a*256 + b
        send((IP(dst=IPAddr, id=c, frag = frag_no)/TCP()), iface=Interface)
        frag_no += 1
#        print(hex(ord(l)))
    send((IP(dst=IPAddr, id=b, frag = (1*16*16*16+frag_no))/TCP()), iface=Interface)


elif Type == "2":
#    print ("Inside 2")
    for l in list(Message):
        a = hex(ord(l))
        a = int(a,16)
        c = a*256 + b
        send((IP(dst=IPAddr, id=c, frag = frag_no)/UDP()), iface=Interface)
        frag_no += 1
#        print(hex(ord(l)))
    send((IP(dst=IPAddr, id=b, frag = (1*16*16*16+frag_no))/UDP()), iface=Interface)

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
#s.connect(IPAddr, Port)
#s.send()
#s.close()