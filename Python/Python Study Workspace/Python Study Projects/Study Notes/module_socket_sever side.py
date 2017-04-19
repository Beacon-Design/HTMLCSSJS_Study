# coding=utf-8
print('''------sever side---------------------------------------------------''')


# print('''------V1------''')
# import socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('localhost', 8001))
# sock.listen(5)
# while True:
#     connection,address = sock.accept()
#     try:
#         connection.settimeout(5)
#         buf = connection.recv(1024)
#         if buf == '1':
#             connection.send('welcome to server!')
#         else:
#             connection.send('please go out!')
#     except socket.timeout:
#         print ('time out')
# connection.close()
# 
# 
#  
# print('''------V2------''')
# import socket
# # Address
# HOST = ''
# PORT = 8000
# 
# reply = 'Yes'# Configure socket
# s     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# # passively wait, 3: maximum number of connections in the queue
# s.listen(3)# accept and establish connection
# conn, addr = s.accept()# receive message
# request    = conn.recv(1024)
# print ('request is: ',request)
# print ('Connected by', addr)# send message
# conn.sendall(reply)# close connection
# conn.close()

# print('''------V3------''')
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
# #也可以使用s=socket.socket()来通过默认参数来生成TCP的流套接字
# #host=''   host可以为空，表示bind()函数可以绑定在所有有效地地址上
# host="localhost"
# port=1235
# s.bind((host,port))   #注意，bind函数的参数只有一个，是（host,port）的元组
# s.listen(3)
# while True:
#     client,ipaddr=s.accept()
#     print ("Got a connect from %s"  %str(ipaddr))
#     data=client.recv(1024)
#     print ("receive data:%s" %data)
#     client.send("echo:%s"%data)
#     client.close()


# print('''------V4---bytes_to_string------''')
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
# #也可以使用s=socket.socket()来通过默认参数来生成TCP的流套接字
# #host=''   host可以为空，表示bind()函数可以绑定在所有有效地地址上
# host="localhost"
# port=1235
# send_1="echo:"
# 
# s.bind((host,port))   #注意，bind函数的参数只有一个，是（host,port）的元组
# s.listen(3)
# while True:
#     client,ipaddr=s.accept()
#     print ("Got a connect from {}".format(ipaddr))
#     data=client.recv(1024)
#     datatostring = data.decode()
#     print (datatostring)
# #     print ("receive data:{}".format(datatostring))
#     client.send(data)
#     client.close()



# print('''------V5---tcp_socket_sever------''')
# import socket
# import time
# severSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
# #也可以使用s=socket.socket()来通过默认参数来生成TCP的流套接字
# #host=''   host可以为空，表示bind()函数可以绑定在所有有效地地址上
# host=""
# port=1235
# timeN=time.ctime()
# 
# severSocket.bind((host,port))   #注意，bind函数的参数只有一个，是（host,port）的元组
# severSocket.listen(3)
# 
# while True:
#     clientSocket,ipaddr=severSocket.accept()
#     print ("Got a connect from {}".format(ipaddr))
#     
#     while True:       
#         data=clientSocket.recv(1024)
#         if not data:
#             break
#         datatostring = data.decode()
#         print(timeN)
#         print("client message: ",datatostring)
#         clientSocket.send(data)
# clientSocket.close()
# severSocket.close()


# print('''------ V6 tcp sever ------''')
# import socket
# 
# host = ''
# port = 80
# 
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.bind((host, port))
# print("waiting for connections...")
# s.listen(1)
# 
# while 1:
#     clientsock,clientaddr = s.accept()
#     print("Got connection from",clientsock.getpeername(),clientaddr)
#     clientsock.close()
    

print('''------ V7 A Minimal Server ------''')
import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print ('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()



























