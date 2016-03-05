import ftplib
import os
import time

while True:
    

    f=open("bluetooth.txt","w")


    s = raw_input("Please enter the Phone's Name: ")
    f.write(s)
    f.close()

    if os.path.exists("receipt.jpg"):
        print "Client Connecting to FTP Server"
        session = ftplib.FTP('192.168.1.1','pi','raspberry')
        f=open("bluetooth.txt","r")
        session.storbinary('STOR /home/pi/Desktop/receipts/bluetooth.txt', f)
        f.close()
        file = open('receipt.jpg','rb')
        print "Sending file to the FTP Server.."
        session.storbinary('STOR Desktop/receipts/receipt.jpg', file)
        file.close()
        print "File sent. Removing unnecessary files..."
        os.remove("receipt.jpg")
        os.remove("bluetooth.txt")
        print "Done."
        session.quit()
    else:
        print "Image file is needed."


# print "Client Connecting to FTP Server"
# session = ftplib.FTP('192.168.1.1','pi','raspberry')
# print session
# if session:
#     print "not OK"
# else:
#     print "Client Connected."
# print session
# print "Test"
# while True:
#     if os.path.exists("C:/Users/Alex/Desktop/sample/receipt.jpg"):
#         f=open("C:/Users/Alex/Desktop/sample/bluetooth.txt","w")
#         s = raw_input("Please enter the Phone's Name: ")
#         f.write(s)
#         f.close()
#         f=open("C:/Users/Alex/Desktop/sample/bluetooth.txt","r")
#         session.storbinary('STOR /home/pi/Desktop/receipts/bluetooth.txt', f)
#         f.close()
#         file = open('C:/Users/Alex/Desktop/sample/receipt.jpg','rb')
#         print "Sending file to the FTP Server.."
#         session.storbinary('STOR Desktop/receipts/receipt.jpg', file)
#         file.close()
#         print "File sent. Removing unnecessary files..."
#         os.remove("C:/Users/Alex/Desktop/sample/receipt.jpg")
#         os.remove("C:/Users/Alex/Desktop/sample/bluetooth.txt")
#         print "Done."
# input()
