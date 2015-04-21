import socket

daddr = '255.255.255.255'
saddr =' 0.0.0.0'
serverPort = 68
cport = 67
Op = b'\x02'
HwType = b'\x01'
HwAddrLen = b'\x06'
HopC = b'\x00'
TransactionID = b'\x39\x03\xf3\x26'
NumOfSec = b'\x00\x00'
Flags_B_Res = b'\x00\x00'
ciaddr = b'\x00\x00\x00\x00'
yiaddr = b'\xC0\xA8\x01\x64'
siaddr = b'\x00\x00\x00\x00'
giaddr = b'\x00\x00\x00\x00'
chwaddr = b'\x00\x05\x3C\x04\x8D\x59'
chwpadding = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
srchostname = b'\x00' * 64
bootfilename = b'\x00' * 128
magic_cookie = b'\x63\x82\x53\x63'
msg_type = b'\x35\x01\x02'
opt1 = b'\x01\x04\xff\xff\xff\x00'
opt2 = b'\x03\x04\xc0\xa8\x01\x01'
opt3 = b'\x33\x04\x00\x01\x51\x80'
opt4 = b'\x36\x04\xc0\xa8\x01\x01'

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')

#receive Discover + Send Offer 
get, clientAddress = serverSocket.recvfrom(2048)
print('Discover Packet : \n')
print(get)
print('\n')
print('OP : %x'%get[0])
print('HTYPE : %x'%get[1])
print('HLEN : %x'%get[2])
print('HOPs : %x'%get[3])
print('XID : 0x%x0%x%x%x'%(get[4],get[5],get[6],get[7]))
print('SECS : %x'%get[8])
print('FLAGS : %x'%get[10])
print('CIADDR : %x.%x.%x.%x'%(get[12],get[13],get[14],get[15]))
print('YIADDR : %d.%d.%d.%d'%(get[16],get[17],get[18],get[19]))
print('SIADDR : %x.%x.%x.%x'%(get[20],get[21],get[22],get[23]))
print('GIADDR : %x.%x.%x.%x'%(get[24],get[25],get[26],get[27]))
print('Magic cookie : 0x%x%x%x%x'%(get[236],get[237],get[238],get[239]))
print('DHCP option%d : DHCP Discover'%get[240])
print('DHCP option%d : %d.%d.%d.%d requested\n'%(get[243],get[245],get[246],get[247],get[248]))

pkt =Op+HwType+HwAddrLen+HopC+TransactionID+NumOfSec+Flags_B_Res+ciaddr+yiaddr+siaddr+giaddr+chwaddr+chwpadding+srchostname+bootfilename+magic_cookie+msg_type+opt1+opt2+opt3+opt4+b'\xff'
serverSocket.sendto(pkt,(daddr,cport))

#Receive Request + Send Ack
get, clientAddress = serverSocket.recvfrom(2048)
print('Request Packet : \n')
print(get)
print('OP : %x'%get[0])
print('HTYPE : %x'%get[1])
print('HLEN : %x'%get[2])
print('HOPs : %x'%get[3])
print('XID : 0x%x0%x%x%x'%(get[4],get[5],get[6],get[7]))
print('SECS : %x'%get[8])
print('FLAGS : %x'%get[10])
print('CIADDR : %x.%x.%x.%x'%(get[12],get[13],get[14],get[15]))
print('YIADDR : %d.%d.%d.%d'%(get[16],get[17],get[18],get[19]))
print('SIADDR : %x.%x.%x.%x'%(get[20],get[21],get[22],get[23]))
print('GIADDR : %x.%x.%x.%x'%(get[24],get[25],get[26],get[27]))
print('Magic cookie : 0x%x%x%x%x'%(get[236],get[237],get[238],get[239]))
print('DHCP option%d : DHCP Request'%get[240])
print('DHCP option%d : %d.%d.%d.%d requested'%(get[243],get[245],get[246],get[247],get[248]))
print('DHCP option%d : %d.%d.%d.%d DHCP server\n'%(get[249],get[251],get[252],get[253],get[254]))

print('\n')
msg_type1 = b'\x35\x01\x05'
pkt =Op+HwType+HwAddrLen+HopC+TransactionID+NumOfSec+Flags_B_Res+ciaddr+yiaddr+siaddr+giaddr+chwaddr+chwpadding+srchostname+bootfilename+magic_cookie+msg_type1+opt1+opt2+opt3+opt4+b'\xff'
serverSocket.sendto(pkt,(daddr,cport))
