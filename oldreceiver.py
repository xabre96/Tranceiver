import os.path
import os
import time
import shutil
import bluetooth
import socket
# f=open("test.txt","w")
# s = raw_input("Name: ")
# f.write(str(s))
# f.close()
# f=open("test.txt","r")
# string = f.read()
# print string
# f.close()

# target_name = "My Phone"
# target_address = None

# nearby_devices = bluetooth.discover_devices()
# print nearby_devices

# while True:
#     if os.path.exists("/home/pi/Desktop/receipts/receipt.jpg"):
#         print "File exists!"
#         os.system("obexftp --nopath --noconn --uuid none --bluetooth B0:C5:59:DD:5C:72 --channel 9 -p /home/pi/Desktop/receipts/receipt.jpg")
#         os.remove("/home/pi/Desktop/receipts/receipt.jpg")
#         time.sleep(5)
#     else:
#         print "File does not exist!"
#         time.sleep(5)

# import socket  
# address, services = socket.bt_discover()  
# print "Chosen device:", address, services  


# for bdaddr in nearby_devices:
#     if target_name == bluetooth.lookup_name( bdaddr ):
#         target_address = bdaddr
#         break
#
# if target_address is not None:
#     print "found target bluetooth device with address ", target_address
# else:
#     print "could not find target bluetooth device nearby"

# while True:
#     if os.path.exists("C:/Users/Alex/Desktop/filezilla.txt"):
#         print "File exists!"
#         shutil.copy("C:/Users/Alex/Desktop/filezilla.txt", "C:/Users/Alex/Desktop/sample/filezilla.txt")
#         yt
#         time.sleep(5)
#     else:
#         print "File does not exist!"
#         time.sleep(5)

# os.remove() will remove a file.
#
# os.rmdir() will remove an empty directory.
#
# shutil.rmtree() will delete a directory and all its contents.
# import socket
# import sys
# s = socket.socket()
# s.bind(("localhost",9999))
# s.listen(10) # Acepta hasta 10 conexiones entrantes.
#
# while True:
#     sc, address = s.accept()
#
#     print address
#     i=1
#     f = open('file_'+ str(i)+".pdf",'wb') #open in binary
#     i=i+1
#     while (True):
#     # recibimos y escribimos en el fichero
#         l = sc.recv(1024)
#         while (l):
#                 f.write(l)
#                 l = sc.recv(1024)
#     f.close()
#
#
#     sc.close()
#
# s.close()