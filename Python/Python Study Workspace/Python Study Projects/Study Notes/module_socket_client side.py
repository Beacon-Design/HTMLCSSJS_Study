# coding=utf-8
print('''------client side------------------------------------------------''')

# print('''------V1------''') 
# import socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('localhost', 8001))
# import time
# time.sleep(2)
# sock.send('1')
# print (sock.recv(1024))
# sock.close()
# 
# 
# print('''------V2------''') 
# import socket
# # Address
# HOST = '127.0.0.1'
# PORT = 8000
# 
# request = 'can you hear me?'
# # configure socket
# s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# # send message
# s.sendall(request)# receive message
# reply   = s.recv(1024)
# print ('reply is: ',reply)# close connection
# s.close()


# print('''------V3------''')
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
# #服务器的主机名和端口
# host="localhost"
# port=1235
# s.connect((host,port))
# s.send(b"i am client")
# data=s.recv(1024)
# print ("Reply from server-----%s"  %data)




# print('''------V4---bytes_to_string------''')
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 
# host="localhost"
# port=1235
# input_1=input("client input: ")
# 
# s.connect((host,port))
# s.send(input_1.encode(encoding="utf-8"))
# 
# data=s.recv(1024)
# print("sever reply {}".format(data.decode()))





# print('''------V5---tcp_socket_client------''')
# import socket
# 
# host="localhost"
# port=1235
# 
# clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# clientSocket.connect((host,port))
# 
# while True:
#     data = input()
#     if not data:
#         break
#     clientSocket.send(data.encode(encoding="utf-8"))
#     recvdata = clientSocket.recv(1024)
#     if not recvdata:
#         break
#     print("sever reply {}".format(recvdata.decode()))
#     
# clientSocket.close()





# print('''------V6---***------''')
# import socket
#  
# host="68.194.67.140"
# port=38243
#  
# clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# clientSocket.connect((host,port))
#  
# while True:
#     data = input()
#     if not data:
#         break
#     clientSocket.send(data.encode(encoding="utf-8"))
#     recvdata = clientSocket.recv(1024)
#     if not recvdata:
#         break
#     print("sever reply {}".format(recvdata.decode()))
#      
# clientSocket.close()


print('''------V7 A Minimal Client------''')
import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
print (s.recv(1024))















