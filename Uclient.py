import socket
daddr = '255.255.255.255'
saddr =' 0.0.0.0'
serverPort = 68
cport = 67
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
clientSocket.bind(('0.0.0.0',cport))
Op = b'\x01'
HwType = b'\x01'
HwAddrLen = b'\x06'
HopC = b'\x00'
TransactionID = b'\x39\x03\xf3\x26'
NumOfSec = b'\x00\x00'
Flags_B_Res = b'\x00\x00'
ciaddr = b'\x00\x00\x00\x00'
yiaddr = b'\x00\x00\x00\x00'
siaddr = b'\x00\x00\x00\x00'
giaddr = b'\x00\x00\x00\x00'
chwaddr = b'\x00\x05\x3C\x04\x8D\x59'
chwpadding = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
srchostname = b'\x00' * 64
bootfilename = b'\x00' * 128
magic_cookie = b'\x63\x82\x53\x63'
msg_type = b'\x35\x01\x01'
opt1 = b'\x32\x04\xC0\xA8\x01\x64'
opt2 = b'\x36\x04\xc0\xa8\x01\x01'

#Send Discover + Receive Offer 
pkt =Op+HwType+HwAddrLen+HopC+TransactionID+NumOfSec+Flags_B_Res+ciaddr+yiaddr+siaddr+giaddr+chwaddr+chwpadding+srchostname+bootfilename+magic_cookie+msg_type+opt1+b'\xff'
clientSocket.sendto(pkt,(daddr, serverPort))
get= clientSocket.recv(2048)
print('Offer Packet : ')
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
print('DHCP option%d : DHCP Offer'%get[240])
print('DHCP option%d : %d.%d.%d.%d subnet mask'%(get[243],get[245],get[246],get[247],get[248]))
print('DHCP option%d : %d.%d.%d.%d router'%(get[249],get[251],get[252],get[253],get[254]))
print('DHCP option%d : %ds'%(get[255],get[257]+get[258]*16*16*16*16+get[259]*16*16+get[260]))
print('DHCP option%d : %d.%d.%d.%d DHCP server\n'%(get[261],get[263],get[264],get[265],get[266]))

msg_type1 = b'\x35\x01\x03'

#Send Request + Receive Ack
pkt =Op+HwType+HwAddrLen+HopC+TransactionID+NumOfSec+Flags_B_Res+ciaddr+yiaddr+siaddr+giaddr+chwaddr+chwpadding+srchostname+bootfilename+magic_cookie+msg_type1+opt1+opt2+b'\xff'
clientSocket.sendto(pkt,(daddr, serverPort))
get= clientSocket.recv(2048)
print('Ack Packet : \n')
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
print('DHCP option%d : DHCP ACK'%get[240])
print('DHCP option%d : %d.%d.%d.%d subnet mask'%(get[243],get[245],get[246],get[247],get[248]))
print('DHCP option%d : %d.%d.%d.%d router'%(get[249],get[251],get[252],get[253],get[254]))
print('DHCP option%d : %ds'%(get[255],get[257]+get[258]*16*16*16*16+get[259]*16*16+get[260]))
print('DHCP option%d : %d.%d.%d.%d DHCP server'%(get[261],get[263],get[264],get[265],get[266]))

