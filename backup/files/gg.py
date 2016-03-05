from Tkinter import *
import sys
import ttk
import tkMessageBox
import ftplib
import os
import time
import ttk


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('Digital_Receipt_Printer')
    geom = "365x278+464+209"
    root.geometry(geom)
    w = Digital_Receipt_Printer (root)
    root.mainloop()

w = None
def create_Digital_Receipt_Printer(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('Digital_Receipt_Printer')
    geom = "365x278+464+209"
    w.geometry(geom)
    w_win = Digital_Receipt_Printer (w)
    return w_win

def destroy_Digital_Receipt_Printer():
    global w
    w.destroy()
    w = None


class Digital_Receipt_Printer:
    # host = '192.168.1.1'
    # user = 'pi'
    # password = 'raspberry'
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(background="#d9d9d9")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")


        self.menubar = Menu(master,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)



        self.Label5 = Label(master)
        self.Label5.place(relx=0.05, rely=0.65, height=21, width=6)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background=_bgcolor)
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(master)
        self.TNotebook1.place(relx=0.08, rely=0.04, relheight=0.81
                , relwidth=0.83)
        self.TNotebook1.configure(width=300)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_pg0 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg0, padding=3)
        self.TNotebook1.tab(0, text="Bluetooth",underline="-1",)
        self.TNotebook1_pg1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg1, padding=3)
        self.TNotebook1.tab(1, text="FTP Settings",underline="-1",)

        self.Label1 = Label(self.TNotebook1_pg0)
        self.Label1.place(relx=0.03, rely=0.1, height=21, width=137)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Bluetooth Device Name :''')

        self.tNo37_pg0_cpd39 = Text(self.TNotebook1_pg0)
        self.tNo37_pg0_cpd39.place(relx=0.0, rely=0.0, relheight=0.01
                , relwidth=0.0)
        self.tNo37_pg0_cpd39.configure(background="white")
        self.tNo37_pg0_cpd39.configure(font="TkTextFont")
        self.tNo37_pg0_cpd39.configure(foreground="black")
        self.tNo37_pg0_cpd39.configure(highlightbackground="#d9d9d9")
        self.tNo37_pg0_cpd39.configure(highlightcolor="black")
        self.tNo37_pg0_cpd39.configure(insertbackground="black")
        self.tNo37_pg0_cpd39.configure(selectbackground="#c4c4c4")
        self.tNo37_pg0_cpd39.configure(selectforeground="black")
        self.tNo37_pg0_cpd39.configure(width=164)
        self.tNo37_pg0_cpd39.configure(wrap=WORD)

        self.Text1 = Text(self.TNotebook1_pg0)
        self.Text1.place(relx=0.17, rely=0.26, relheight=0.12, relwidth=0.68)
        self.Text1.configure(background="white")
        self.Text1.bind("<Return>", self.ok())
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=204)
        self.Text1.configure(wrap=WORD)

        self.Button1 = Button(self.TNotebook1_pg0)
        self.Button1.place(relx=0.2, rely=0.48, height=34, width=69)
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

        self.Button3 = Button(self.TNotebook1_pg0)
        self.Button3.place(relx=0.57, rely=0.48, height=34, width=69)
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

        self.tNo37_pg1_cpd44 = Text(self.TNotebook1_pg1)
        self.tNo37_pg1_cpd44.place(relx=0.0, rely=0.0, relheight=0.0
                , relwidth=0.0)
        self.tNo37_pg1_cpd44.configure(background="white")
        self.tNo37_pg1_cpd44.configure(font="TkTextFont")
        self.tNo37_pg1_cpd44.configure(foreground="black")
        self.tNo37_pg1_cpd44.configure(highlightbackground="#d9d9d9")
        self.tNo37_pg1_cpd44.configure(highlightcolor="black")
        self.tNo37_pg1_cpd44.configure(insertbackground="black")
        self.tNo37_pg1_cpd44.configure(selectbackground="#c4c4c4")
        self.tNo37_pg1_cpd44.configure(selectforeground="black")
        self.tNo37_pg1_cpd44.configure(width=154)
        self.tNo37_pg1_cpd44.configure(wrap=WORD)

        self.Button2 = Button(self.TNotebook1_pg1)
        self.Button2.place(relx=0.39, rely=0.53, height=34, width=65)
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

        self.Text2 = Text(self.TNotebook1_pg1)
        self.Text2.place(relx=0.23, rely=0.09, relheight=0.11, relwidth=0.57)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=174)
        self.Text2.configure(wrap=WORD)

        self.Text3 = Text(self.TNotebook1_pg1)
        self.Text3.place(relx=0.23, rely=0.22, relheight=0.11, relwidth=0.57)
        self.Text3.configure(background="white")
        self.Text3.configure(font="TkTextFont")
        self.Text3.configure(foreground="black")
        self.Text3.configure(highlightbackground="#d9d9d9")
        self.Text3.configure(highlightcolor="black")
        self.Text3.configure(insertbackground="black")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(selectforeground="black")
        self.Text3.configure(width=174)
        self.Text3.configure(wrap=WORD)

        self.Text4 = Text(self.TNotebook1_pg1)
        self.Text4.place(relx=0.23, rely=0.35, relheight=0.11, relwidth=0.57)
        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(foreground="black")
        self.Text4.configure(highlightbackground="#d9d9d9")
        self.Text4.configure(highlightcolor="black")
        self.Text4.configure(insertbackground="black")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(selectforeground="black")
        self.Text4.configure(width=174)
        self.Text4.configure(wrap=WORD)

        self.Label2 = Label(self.TNotebook1_pg1)
        self.Label2.place(relx=0.1, rely=0.09, height=21, width=31)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background=_bgcolor)
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Host''')

        self.Label3 = Label(self.TNotebook1_pg1)
        self.Label3.place(relx=0.02, rely=0.23, height=21, width=59)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background=_bgcolor)
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Username''')

        self.Label4 = Label(self.TNotebook1_pg1)
        self.Label4.place(relx=0.03, rely=0.35, height=21, width=56)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background=_bgcolor)
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Password''')

    def initial(self):
        # pwd = os.path.dirname(os.path.realpath(sys.executable))
        pwd = os.getcwd()
        f=open(pwd+"/config/config.txt","r")
        s=f.readlines()
        f.close()
        self.host = s[1].strip('\n')
        self.user = s[3].strip('\n')
        self.password = s[5].strip('\n')

    def ok(self):
        self.initial()
        pwd = os.path.dirname(os.path.realpath(sys.executable))
        # pwd = os.getcwd()
        pwd = pwd.replace('\\','/')
        if self.Text1.get("1.0",'end-1c') == "":
            tkMessageBox.showerror("Error", "Bluetooth name is required!")
        else:
            input = self.Text1.get("1.0",'end-1c')
            f=open(pwd+"/resc/bluetooth.txt","w")
            f.write(input)
            f.close()

            if os.path.exists(pwd+"/resc/receipt.jpg"):
                try:
                    session = ftplib.FTP(self.host,self.user,self.password)
                    f=open(pwd+"/resc/bluetooth.txt","r")
                    session.storbinary('STOR /home/pi/Desktop/receipts/bluetooth.txt', f)
                    f.close()
                    file = open(pwd+'/resc/receipt.jpg','rb')
                    session.storbinary('STOR Desktop/receipts/receipt.jpg', file)
                    file.close()
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
            # self.host = self.Text2.get("1.0",'end-1c')
            # self.user = self.Text3.get("1.0",'end-1c')
            # self.password = self.Text4.get("1.0",'end-1c')
            pwd = os.path.dirname(os.path.realpath(sys.executable))
            # pwd = os.getcwd()
            f=open(pwd+"/config/config.txt","r")
            s=f.readlines()
            f.close()
            s[1] = self.Text2.get("1.0",'end-1c')+'\n'
            s[3] = self.Text3.get("1.0",'end-1c')+'\n'
            s[5] = self.Text4.get("1.0",'end-1c')+'\n'
            f=open(pwd+"/config/config.txt","w")
            f.writelines(s)
            f.close()
            self.Text2.delete("1.0",'end-1c')
            self.Text3.delete("1.0",'end-1c')
            self.Text4.delete("1.0",'end-1c')
            tkMessageBox.showinfo("Success", "Settings are saved.")




if __name__ == '__main__':
    vp_start_gui()


