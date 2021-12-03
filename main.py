from scapy.all import *
#รับค่าจากคีย์บอร์ด
source_ip = input("IP Addres : ")
target_ip = input("IP Addres Target : ")
i + 1

while True:
  for source_port in range(1, 65535):
    IP1 = IP_PROTOS(source_ip = source_ip , destination = Target)
    TCP1 = TCPListenPipe(srcport = source_port, dstport = 80)
    pkt = IP1/TCP1
    send(pkt, inter = .001)
    
print("Ereos sent ", i)
i = i+1