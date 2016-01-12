import os.path
import os
import time
import shutil

while True:
    if os.path.exists("C:/Users/Alex/Desktop/filezilla.txt"):
        print "File exists!"
        shutil.copy("C:/Users/Alex/Desktop/filezilla.txt", "C:/Users/Alex/Desktop/sample/filezilla.txt")
        os.remove("C:/Users/Alex/Desktop/filezilla.txt")
        time.sleep(5)
    else:
        print "File does not exist!"
        time.sleep(5)

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