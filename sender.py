
from Tkinter import *
import sys
import ttk
import tkMessageBox
import ftplib
import os
import time



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('Digital Receipt Printer')
    geom = "500x220+490+187"
    root.geometry(geom)
    w = BT (root)
    root.mainloop()

w = None
def create_BT(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('BT')
    geom = "500x220+490+187"
    w.geometry(geom)
    w_win = BT (w)
    return w_win

def destroy_BT():
    global w
    w.destroy()
    w = None


class BT:
    host = '192.168.1.1'
    user = 'pi'
    password = 'raspberry'
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        master.configure(background="#d9d9d9")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")


        self.Text1 = Text(master)
        self.Text1.place(relx=0.04, rely=0.25, relheight=0.15, relwidth=0.33)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=164)
        self.Text1.configure(wrap=WORD)

        self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)



        self.Label1 = Label(master)
        self.Label1.place(relx=0.0, rely=0.09, height=21, width=144)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Bluetooth Device Name :''')

        self.Button1 = Button(master)
        self.Button1.place(relx=0.04, rely=0.45, height=34, width=67)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background=_bgcolor)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(command=self.ok)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')

        self.Button3 = Button(master)
        self.Button3.place(relx=0.22, rely=0.45, height=34, width=67)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background=_bgcolor)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(command=self.cancel)
        self.Button3.configure(text='''Cancel''')

        self.Label2 = Label(master)
        self.Label2.place(relx=0.57, rely=0.09, height=21, width=31)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background=_bgcolor)
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Host''')

        self.Label3 = Label(master)
        self.Label3.place(relx=0.51, rely=0.23, height=21, width=59)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background=_bgcolor)
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Username''')

        self.Label4 = Label(master)
        self.Label4.place(relx=0.52, rely=0.36, height=21, width=56)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background=_bgcolor)
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Password''')

        self.Button2 = Button(master)
        self.Button2.place(relx=0.73, rely=0.51, height=34, width=55)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background=_bgcolor)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(command=self.save)
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Save''')

        self.Label6 = Label(master)
        self.Label6.place(relx=0.04, rely=0.77, height=41, width=164)
        self.Label6.configure(background=_bgcolor)
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        # self.Label6.configure(text='''Label''')
        self.Label6.configure(width=164)

        self.Text2 = Text(master)
        self.Text2.place(relx=0.64, rely=0.09, relheight=0.11, relwidth=0.31)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=154)
        self.Text2.configure(wrap=WORD)

        self.Text3 = Text(master)
        self.Text3.place(relx=0.64, rely=0.22, relheight=0.11, relwidth=0.31)
        self.Text3.configure(background="white")
        self.Text3.configure(font="TkTextFont")
        self.Text3.configure(foreground="black")
        self.Text3.configure(highlightbackground="#d9d9d9")
        self.Text3.configure(highlightcolor="black")
        self.Text3.configure(insertbackground="black")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(selectforeground="black")
        self.Text3.configure(width=154)
        self.Text3.configure(wrap=WORD)

        self.Text4 = Text(master)
        self.Text4.place(relx=0.64, rely=0.36, relheight=0.11, relwidth=0.31)
        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(foreground="black")
        self.Text4.configure(highlightbackground="#d9d9d9")
        self.Text4.configure(highlightcolor="black")
        self.Text4.configure(insertbackground="black")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(selectforeground="black")
        self.Text4.configure(width=154)
        self.Text4.configure(wrap=WORD)

    def ok(self):
        # pwd = os.path.dirname(os.path.realpath(sys.executable))
        pwd = os.getcwd()
        pwd = pwd.replace('\\','/')
        if self.Text1.get("1.0",'end-1c') == "":
            tkMessageBox.showerror("Error", "Bluetooth name is required!")
        else:
            input = self.Text1.get("1.0",'end-1c')
            f=open(pwd+"/resc/bluetooth.txt","w")
            f.write(input)
            f.close()

            if os.path.exists(pwd+"/resc/receipt.jpg"):
                # print "Client Connecting to FTP Server"
                try:
                    session = ftplib.FTP(self.host,self.user,self.password)
                    f=open(pwd+"/resc/bluetooth.txt","r")
                    session.storbinary('STOR /home/pi/Desktop/receipts/bluetooth.txt', f)
                    f.close()
                    file = open(pwd+'/resc/receipt.jpg','rb')
                    # print "Sending file to the FTP Server.."
                    session.storbinary('STOR Desktop/receipts/receipt.jpg', file)
                    file.close()
                    # print "File sent. Removing unnecessary files..."
                    os.remove(pwd+"/resc/receipt.jpg")
                    os.remove(pwd+"/resc/bluetooth.txt")
                    self.Text1.delete("1.0",'end-1c')
                    session.quit()
                except IOError:
                    tkMessageBox.showerror("Error", "Cannot find the FTP Server!")
                else:
                    tkMessageBox.showinfo("Success", "Image sent!")
                    root.destroy()
            else:
                self.Text1.delete("1.0",'end-1c')
                tkMessageBox.showerror("Error", "Image does not exist!")

    def cancel(self):
        root.destroy()

    def save(self):
        if self.Text2.get("1.0",'end-1c') == "" or self.Text3.get("1.0",'end-1c')=="" or self.Text4.get("1.0",'end-1c') == "":
            self.Text2.delete("1.0",'end-1c')
            self.Text3.delete("1.0",'end-1c')
            self.Text4.delete("1.0",'end-1c')
            tkMessageBox.showerror("...", "Fields are required to be filled.")
        else:
            self.host = self.Text2.get("1.0",'end-1c')
            self.user = self.Text3.get("1.0",'end-1c')
            self.password = self.Text4.get("1.0",'end-1c')
            self.Text2.delete("1.0",'end-1c')
            self.Text3.delete("1.0",'end-1c')
            self.Text4.delete("1.0",'end-1c')
            # self.Label6.configure(text='''Settings are set.''')
            tkMessageBox.showinfo("Success", "Settings are saved.")

if __name__ == '__main__':
    vp_start_gui()


