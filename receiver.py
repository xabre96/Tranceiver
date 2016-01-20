import os
import time
import shutil
import bluetooth
import lightblue

while True:
  if os.path.exists("/home/pi/Desktop/receipts/receipt.jpg"):
    f = open('/home/pi/Desktop/receipts/bluetooth.txt')
    lines = f.read()
    target_name = lines.rstrip('\n')
    f.close()
        
    obex_port = None                 
    target_address = None  
    dummy = None
        
    print "searching for nearby devices..."  
    nearby_devices = bluetooth.discover_devices()  
        
    for bdaddr in nearby_devices:
      if target_name == bluetooth.lookup_name(bdaddr):
        target_address = bdaddr
        break  
        
    print "searching for the object push service..."
    # print target_address
    services = lightblue.findservices(dummy)  
    for service in services:
      if service[2] == "OBEX Object Push":
        obex_port = service[1]       
        print "OK, service '", service[2], "' is in port", service[1], "!"  
        break  
        
    print "sending a file..."
    if target_address is not None:
      os.system("obexftp --nopath --noconn --uuid none --bluetooth "+target_address+" --channel {} -p /home/pi/Desktop/receipts/receipt.jpg".format(obex_port))
      os.remove("/home/pi/Desktop/receipts/receipt.jpg")
      os.remove("/home/pi/Desktop/receipts/bluetooth.txt")
    else:
      print "an error occurred while sending file\n"

else:
  print "File does not exist!"
  time.sleep(5)

# f = open('/home/pi/Desktop/receipts/bluetooth.txt')
# lines = f.read()
# target_name = lines.rstrip('\n')
# f.close()

# target_address = None
# channel = None

# nearby_devices = bluetooth.discover_devices()
# for bdaddr in nearby_devices:
#   if target_name == bluetooth.lookup_name(bdaddr):
#     target_address = bdaddr
#     break

# add = ''.join(target_address)
# add = str(target_address)
# print add
# if svc["name"]=='OBEX Object Push' or svc["name"] == 'OPP':
# services = bluetooth.find_service(address=str(target_address))
# print target_address
# services = lightblue.findservices('00:1A:13:4C:C2:DE')
# for service in services:
  # print 'No'
 # if service[2] == "OBEX Object Push":
  # obex_port = service[1]       
  # print "OK, service '", service[2], "' is in port", service[1], "!"  
  # break
# print services
# for svc in services:
#   if svc["name"]=='OBEX Object Push':
#     channel = str(svc["port"])
#     print channel
#     print("Service Name: %s" % svc["name"])
#     print("    channel/PSM: %s" % svc["port"])
#     print("")

# if target_address is not None:
#   print "found target bluetooth device with address ", target_address
#   os.system("obexftp --nopath --noconn --uuid none --bluetooth "+target_address+" --channel 23 -p /home/pi/Desktop/receipts/receipt.jpg")
# else:
#   print "could not find target bluetooth device nearby"



#subprocess.call(["obexftp --nopath --noconn --uuid none --bluetooth B0:C5:DD:5C:72 --channel 9 -p /home/pi/Desktop/receipts/receipt.jpg"])
#subprocess.check_output(['obexftp', '--nopath', '--noconn', '--uuid none', '--bluetooth B0:C5:DD:5C:72', '--channel 9', '-p /home/pi/Desktop/receipts/receipt.jpg'])

#         # print lines
# f = open('/home/pi/Desktop/receipts/bluetooth.txt', 'w')
# for line in lines:
#     if line != "\n":
#         f.write(line)
# f.close()
# try:
#   os.system('obexftp --nopath --noconn --uuid none --bluetooth B0:C5:DD:5C:72 --channel 9 -p /home/pi/Desktop/receipts/receipt.jpg')
# except:
#   print 'error'
# f = open('/home/pi/Desktop/receipts/bluetooth.txt')
# target_name = f.read()
# target_name = str.rstrip('\n')
# f.close()
  
# for svc in services:
#   if svc["name"]=='OBEX Object Push':
#     channel = str(svc["port"])
#     print channel
#     print("Service Name: %s" % svc["name"])
#     print("    channel/PSM: %s" % svc["port"])
#     print("")
    

  # os.system('obexftp --nopath --noconn --uuid none --bluetooth B0:C5:DD:5C:72 --channel 5 -p /home/pi/Desktop/receipts/receipt.jpg')
      #os.remove("/home/pi/Desktop/receipts/receipt.jpg")
            #os.remove("/home/pi/Desktop/receipts/bluetooth.txt")
            # time.sleep(5)
  # print channel
  # print target_address
# nearby_devices = bluetooth.discover_devices()
# for bdaddr in nearby_devices:
#     if str(target_name) == bluetooth.lookup_name( bdaddr ):
#         target_address = bdaddr
#         break
# while True:
#     if os.path.exists("/home/pi/Desktop/receipts/receipt.jpg"):
            
#         print "File exists!"
#         f = open('/home/pi/Desktop/receipts/bluetooth.txt')
#         lines = f.readlines()
#         f.close()
#         # print lines
#         f = open('/home/pi/Desktop/receipts/bluetooth.txt', 'w')

#         for line in lines:
#          if line != "\n":
#           f.write(line)

#         f.close()
#         f = open('/home/pi/Desktop/receipts/bluetooth.txt', 'r')
#         target_name = f.read()
#         f.close()
#         # print string
#         #target_name = "Pldt_home_fibr"
#         target_address = None

#         nearby_devices = bluetooth.discover_devices()

#         for bdaddr in nearby_devices:
#             if str(target_name) == bluetooth.lookup_name( bdaddr ):
#                 target_address = bdaddr
#                 break

#         nearby_devices = bluetooth.discover_devices()
#         add = ''.join(target_address)
#         services = bluetooth.find_service(address=target_address)
        
#         for svc in services:
#             if svc["name"]=='OBEX FileTransfer':
#               print("Service Name: %s"    % svc["name"])
#               print("    Host:        %s" % svc["host"])
#               print("    Description: %s" % svc["description"])
#               print("    Provided By: %s" % svc["provider"])
#               print("    Protocol:    %s" % svc["protocol"])
#               print("    channel/PSM: %s" % svc["port"])
#       channel = svc["port"]
#               print("    svc classes: %s "% svc["service-classes"])
#               print("    profiles:    %s "% svc["profiles"])
#               print("    service id:  %s "% svc["service-id"])
#               print("")


#         if target_address is not None:
#       print channel
#       print target_address
#             print "found target bluetooth device with address ", target_address
# #            os.system("obexftp --nopath --noconn --uuid none --bluetooth "+str(target_address)+" --channel "+str(channel)+" -p /home/pi/Desktop/fuck/receipt.jpg")
#             os.system('obexftp --nopath --noconn --uuid none --bluetooth B0:C5:DD:5C:72 --channel 5 -p /home/pi/Desktop/receipts/receipt.jpg')
#       #os.remove("/home/pi/Desktop/receipts/receipt.jpg")
#             #os.remove("/home/pi/Desktop/receipts/bluetooth.txt")
#             time.sleep(5)
#         else:
#             print "could not find target bluetooth device nearby"

# else:
#     print "File does not exist!"
#     time.sleep(5)

# target_name = "My Phone"
# target_address = None

# nearby_devices = bluetooth.discover_devices()
# print nearby_devices

# import socket  
# address, services = socket.bt_obex_discover()  
# print "Chosen device:", address, services  


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
