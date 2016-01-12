import ftplib
session = ftplib.FTP('server.address.com','pi','raspberry')
file = open('kitten.jpg','rb')                  # file to send
session.storbinary('STOR kitten.jpg', file)     # send the file
file.close()                                    # close file and FTP
session.quit()

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