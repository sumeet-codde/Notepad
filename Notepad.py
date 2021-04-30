from tkinter import *
from tkinter.filedialog import  askopenfilename,asksaveasfilename
import os

from datetime import datetime
def NEW():
    global file
    root.title("Notepad")
    file=None
    Add_text.delete(1.0,END) #this means delete the text present from line one and character 0th

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        Add_text.delete(1.0, END)
        f = open(file, "r")
        Add_text.insert(1.0, f.read())
        f.close()
def Save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
        if file== "":
            file=None
        else:
            # Save as a new file
            f = open(file, "w")
            f.write(Add_text.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            # print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(Add_text.get(1.0, END))
        f.close()


def Close_Window():
    root.destroy()
def COPY():
    Add_text.event_generate("<<Copy>>")
def Paste():
    Add_text.event_generate("<<Paste>>")

def TIME():
    import tkinter.messagebox as tmsg
    from datetime import date
    import time
    t=time.localtime()      #The function time.localtime () accepts an optional argument of Epoch seconds, without the argument it takes
                        # the current time (probably from time.time ()). The function then calculates what time this corresponds
                             #to in your timezone (i.e. your local time) and then returns the results in object of type time.struct_time.
    current_time = time.strftime("%H:%M:%S", t)
    today = date.today()
    # print("Today's date:", today)
    tmsg.showinfo("Date",f"Today's date is {today} and current tiime is {current_time}")
def about():
    import  tkinter.messagebox as tmsg
    tmsg.showinfo("About","This Notepad is made by Sumeet")
root=Tk()
root.geometry("455x255")
root.title("Notepad By Sumeet")
root.wm_iconbitmap("Notepad.ico")

filemenu=Menu(root) #horizontal menubar is made
#make a variable m1
m1=Menu(filemenu,tearoff=0)
m1.add_command(label="New",command=NEW)
m1.add_command(label="OPEN FILE",command=openFile)
m1.add_command(label="Save",command=Save)
m1.add_separator()
m1.add_command(label="Exit",command=Close_Window)

root.config(menu=filemenu)

filemenu.add_cascade(label="File",menu=m1)
# -----------------------
m2=Menu(filemenu,tearoff=0)
m2.add_command(label="Copy",command=COPY)
m2.add_command(label="Paste",command=Paste)
m2.add_separator()
m2.add_command(label="Time and Date",command=TIME)

root.config(menu=filemenu)
filemenu.add_cascade(label="Edit",menu=m2)
#-----------------------------------------

m3=Menu(filemenu,tearoff=0)
m3.add_command(label="About",command=about)
root.config(menu=filemenu)
filemenu.add_cascade(label="Help",menu=m3)

#----------------------------------------------

# add text area
Add_text=Text(root,font="lucidal 13" )
file=None
Add_text.pack(expand=True,fill=BOTH)

#------------------------------
#making scrollbar

scrollbar=Scrollbar(Add_text)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=Add_text.yview)  #sets the scrollbar command to the yview method of the widget using "config"
Add_text.config(yscrollcommand=scrollbar.set)



root.mainloop()