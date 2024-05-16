import socket
from struct import *
from ctypes import *
import os
import sys
import threading
import time

class IPV4(Structure):
    _fields_=[
            ("ttl", c_ubyte),
            ("protocol_num", c_ubyte),
            ("sum", c_ushort),
            ("src", c_uint32),
            ("dst", c_uint32)
            ]
    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        
        self.sadd = socket.inet_ntoa(pack("@I",self.src))
        self.dadd = socket.inet_ntoa(pack("@I",self.dst))
        
class TCP_UDP(Structure):
    _fields_=[
            ("s_port", c_ushort),
            ("d_port", c_ushort)
            ]
    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        self.sport = socket.ntohs(self.s_port)
        self.dport = socket.ntohs(self.d_port)

def send(packet,dadd):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)    
    sock.sendto(packet,(dadd,0))

def chack(sip,dip,sport,dport,proto):
    for line in reversed(open("rules.conf").readlines()):
            line = line.split()
            if (line[0] == sip or line[0] == 'any') and (line[1] == dip or line[1] == 'any') and (line[2] == sport or line[2] == 'any') and (line[3] == dport or line[3] == 'any') and (line[4] == proto or line[4] == 'any') and (line[5] == "A" or line[5] == 'a'):
                return True
            elif (line[0] == sip or line[0] == 'any') and (line[1] == dip or line[1] == 'any') and (line[2] == sport or line[2] == 'any') and (line[3] == dport or line[3] == 'any') and (line[4] == proto or line[4] == 'any') and (line[5] == "D" or line[5] == 'd'):
                return False
    return False

def show(filename):
    c = 1
    print(f"\n----- Firewall {filename[:5]} -----\n")
    for line in reversed(open(filename).readlines()):
        print(f'{c} {line}',end="")
        c = c + 1 
    print()

def write(filename,line):
    with open(filename,"a") as f:
        f.write(line)
        f.write("\n")

def delete(filename,line):
    c = 1 
    l = reversed(open(filename).readlines())
    with open ("tmp",'w') as f:
        for nl in l:
            if c != line:
                f.write(nl)
            c = c + 1
    l = reversed(open('tmp').readlines())
    with open (filename,'w') as f:
        for nl in l:
            f.write(nl)

def bind(interface):
    time.sleep(2)
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface,0))
    while True:
        data = sock.recvfrom(65565)[0]
        ip = IPV4(data[22:])
        ip_header = pack('!BBHHHBBH4s4s', (4<<4)+5,0,0,0,0,ip.ttl,ip.protocol_num,0,socket.inet_aton(ip.sadd),socket.inet_aton(ip.dadd))
        packet = ip_header + data[34:]
        if ip.protocol_num == 6 or ip.protocol_num == 17:
            tcp_udp=TCP_UDP(data[34:])
            if chack(ip.sadd,ip.dadd,tcp_udp.sport,tcp_udp.dport,ip.protocol_num):
                send(packet,ip.dadd)
        else:
            if chack(ip.sadd,ip.dadd,'0','0',str(ip.protocol_num)):
                send(packet,ip.dadd)

os.system('clear')
text = "\033[1;31mWELCOME TO BASIC FIREWALL\033[0m"
width = 100
print("+" + "_" * (width - 2) + "+")
print( text.center(width - 2) )
print("+" + "_" * (width - 2) + "+")
if os.path.isfile('rules.conf'):
    print("\n\033[1;36mrules.conf\033[0m \033[1;92mFound\033[0m")
else:
    print('\033[1;36mrules.conf\033[0m \033[1;91mNot Found\033[0m')
    with open("rules.conf",'w') as f:
        f.write("any any any any any D\n")
    print('\033[1;36mrules.conf\033[0m \033[1;93mCreated\033[0m')
if os.path.isfile('routs.conf'):
    print("\033[1;36mrouts.conf\033[0m \033[1;92mFound\033[0m")
else:
    print('\033[1;36mrouts.conf\033[0m \033[1;91mNot Found\033[0m')
    with open("routs.conf",'w') as f:
        f.write("")
    print('\033[1;36mrouts.conf\033[0m \033[1;93mCreated\033[0m')
interface = os.listdir('/sys/class/net/')
for i in interface:
    if i != "lo":
        t = threading.Thread(target=bind, args=(i,))
        t.daemon=True
        t.start()
print(f'{threading.active_count()-1} \033[1;36mInterface\033[0m \033[1;92mFound\033[0m')
for c in range(40):
    print("\033[1;33m-\033[0m",end="")
    sys.stdout.flush()
    time.sleep(0.1)
print("\n\033[1;36mEnter help For Help\033[0m\n")

consol = "Firewall :"
while True:
    try:
        x = input(consol)
    except KeyboardInterrupt:
        print("\nExiting.....")
        exit()
    if consol == "Firewall :":
        if x == "help":
            print("\nconf rules \t:   \033[1;36m-----Add Or Remove Firewall Rules-----\033[0m\nconf routes \t:   \033[1;36m-----Add Or Remove Firewall Routes-----\033[0m\nshow rules \t:   \033[1;36m-----Show List Of Firewall Rules-----\033[0m\nshow routes \t:   \033[1;36m-----Show List Of Firewall Routes-----\033[0m\nexit \t\t:   \033[1;36m-----Exit Firewall-----\033[0m\n")
        elif x == "conf rules":
            consol = "Firewall : "
            show("rules.conf")
        elif x == "conf route":
            consol = "Firewall :"
            show("routs.conf")
        elif x == "show routes":
            show("routs.conf")
        elif x == "show rules":
            show("rules.conf")
        elif x == "exit":
            print("Exiting.....")
            exit()
        else:
            print(f'"{x}" Command Not Found')
    elif consol == "Firewall : ":
        y = x.split()
        if x == "help":
            print("\nadd \t-   \033[1;36mAdd Firewall Rules\t<Sours IP> <Destination IP> <Sours Port> <Destination Port> <Protocal Number> <A or D>\033[0m\ndel \t-   \033[1;36mRemove Firewall Rules\t<Rules Number>\033[0m\nexit \t-   \033[1;36mBack\033[0m\n")
        elif y[0] == 'add':
            if len(y) < 6:
                print("Command Incomplete")
                continue
            try:
                if(y[1] != "any"):
                    socket.inet_aton(y[1])
            except:
                print(f'"{y[1]}" Is Not A Valid IP address')
                continue
            try:
                if(y[2] != "any"):
                    socket.inet_aton(y[2])
            except:
                print(f'"{y[2]}" Is Not A Valid IP address')
                continue
            try:
                if y[3] != 'any':
                    if int(y[3]) > 65565 or int(y[3]) < 0:
                        print(f'"{y[3]}" Is Not A Valid Port Number')
                        continue
            except:
                print(f'"{y[3]}" Is Not A Valid Port Number')
                continue
            try:
                if y[4] != 'any':
                    if int(y[4]) > 65565 or int(y[4]) < 0:
                        print(f'"{y[4]}" Is Not A Valid Port Number')
                        continue
            except:
                print(f'"{y[4]}" Is Not A Valid Port Number')
                continue
            try:
                if y[5] != 'any':
                    if int(y[5]) > 255 or int(y[5]) < 0:
                        print(f'"{y[5]}" Is Not A Valid Protocol Number')
                        continue
            except:
                print(f'"{y[5]}" Is Not A Valid Protocol Number')
                continue
            if y[6] != 'A' and y[6] != 'a' and y[6] != 'D' and y[6] != 'd':
                print(f'"{y[6]}" Command Not Found')
                continue
            write("rules.conf",x[4:])
        elif y[0] == 'del':
            if len(y) < 2:
                print("Comand Incomplete")
                continue
            try:
                delete("rules.conf",int(y[1]))
            except:
                print(f'"{y[1]}" Is Not A Number')
                continue
        elif x == "exit":
            consol = "Firewall :"
        else:
            print(f'"{x}" Command Not Found')

