import ftplib
import os
import time

print "Client Connecting to FTP Server"
session = ftplib.FTP('192.168.1.1','pi','raspberry')
print "Client Connected."
while True:
    if os.path.exists("C:/Users/Alex/Desktop/sample/receipt.jpg"):
        f=open("C:/Users/Alex/Desktop/sample/bluetooth.txt","w")
        s = raw_input("Please enter the Phone's Name: ")
        f.write(s)
        f.close()
        f=open("C:/Users/Alex/Desktop/sample/bluetooth.txt","r")
        session.storbinary('STOR /home/pi/Desktop/receipts/bluetooth.txt', f)
        f.close()
# session.quit()
#         print "A receipt exist. Opening connection to FTP server.."
        file = open('C:/Users/Alex/Desktop/sample/receipt.jpg','rb')
        print "Sending file to the FTP Server.."
        session.storbinary('STOR Desktop/receipts/receipt.jpg', file)
        file.close()
        print "File sent. Removing unnecessary files..."
        os.remove("C:/Users/Alex/Desktop/sample/receipt.jpg")
        os.remove("C:/Users/Alex/Desktop/sample/bluetooth.txt")
        print "Done."
    # else:
        # print "File does not exist!"
        # time.sleep(5)

# To find out the current directory, use FTP.pwd():
#
# FTP.pwd(): Return the pathname of the current directory on the server.
# To change the directory, use FTP.cwd(pathname):
#
# FTP.cwd(pathname): Set the current directory on the server.

# import socket
# import sys
#
# s = socket.socket()
# s.connect(("localhost",9999))
# f=open ("libroR.pdf", "rb")
# l = f.read(1024)
# while (l):
#     s.send(l)
#     l = f.read(1024)
# s.close()