import sys
from Tkinter import *
import tkMessageBox
import ftplib
import os
import time

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('BT')
    geom = "207x220+460+206"
    root.geometry(geom)
    w = BT (root)
    # _support.init(root, w)
    root.mainloop()

w = None
def create_BT(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('BT')
    geom = "207x220+460+206"
    w.geometry(geom)
    w_win = BT (w)
    # _support.init(w, w_win, param)
    return w_win

def destroy_BT():
    global w
    w.destroy()
    w = None


class BT:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        master.configure(background="#d9d9d9")


        self.Text1 = Text(master)
        self.Text1.place(relx=0.1, rely=0.27, relheight=0.15, relwidth=0.7)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=144)
        self.Text1.configure(wrap=WORD)

        self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)

        self.Label1 = Label(master)
        self.Label1.place(relx=0.0, rely=0.09, height=21, width=144)
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Bluetooth Device Name :''')
        self.Label1.configure(width=144)

        self.Button1 = Button(master)
        self.Button1.place(relx=0.24, rely=0.55, height=34, width=87)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background=_bgcolor)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')
        self.Button1.configure(command=self.ok)
        self.Button1.configure(width=87)

    def ok(self):
        pwd = os.path.dirname(os.path.realpath(sys.executable))
        pwd = pwd.replace('\\','/')
        input = self.Text1.get("1.0",'end-1c')
        f=open(pwd+"/resc/bluetooth.txt","w")
        f.write(input)
        f.close()

        if os.path.exists(pwd+"/resc/receipt.jpg"):
            print "Client Connecting to FTP Server"
            session = ftplib.FTP('192.168.1.1','pi','raspberry')
            f=open(pwd+"/resc/bluetooth.txt","r")
            session.storbinary('STOR /home/pi/Desktop/receipts/bluetooth.txt', f)
            f.close()
            file = open(pwd+'/resc/receipt.jpg','rb')
            print "Sending file to the FTP Server.."
            session.storbinary('STOR Desktop/receipts/receipt.jpg', file)
            file.close()
            print "File sent. Removing unnecessary files..."
            os.remove(pwd+"/resc/receipt.jpg")
            os.remove(pwd+"/resc/bluetooth.txt")
            self.Text1.delete("1.0",'end-1c')
            print "Done."
            session.quit()
            root.destroy()
        else:
            self.Text1.delete("1.0",'end-1c')
            tkMessageBox.showinfo("Error", "Oops something happened.")

if __name__ == '__main__':
    vp_start_gui()

