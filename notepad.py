import os
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfile, asksaveasfilename
from tkinter.messagebox import showinfo

def newFile():
    global file
    root.title("untitled-Notepad")
    file=None
    textarea.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Documents",".txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ "-Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
        filetypes=[("All Files","*.*"),("Text Documents",".txt")])
        if file=="":
            file =None
        else: #save as a new file 
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ "-Notepad")
            print("file saved")
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()

    
def quitApp():
    root.destroy()

def cut():
    textarea.event_generate("<<Cut>>")
    

def copy():
    textarea.event_generate("<<Copy>>")

def paste():
    textarea.event_generate("<<Paste>>")

def about():
    showinfo("notepad","notepad by shashank")



if __name__=='__main__':
    root=Tk()
    root.geometry("700x600")
    root.title("untitled-Notepad")

    textarea=Text(root,font="lucida  14")
    file=None
    textarea.pack(expand=True,fill=BOTH)


    scroll=Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)  # to use scroll int text area 
    textarea.config(yscrollcommand=scroll.set)# to adjust scroll according to  text of the notepad


    menubar=Menu(root)



    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_command(label="new",command=newFile)
    filemenu.add_command(label="open",command=openFile)
    filemenu.add_command(label="save",command=saveFile)
    filemenu.add_command(label="exit",command=quitApp)

    menubar.add_cascade(label="file",menu=filemenu)


    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="cut",command=cut)
    editmenu.add_command(label="copy",command=copy)
    editmenu.add_command(label="paste",command=paste)


    menubar.add_cascade(label="Edit",menu=editmenu)


    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="About",command=about)
    menubar.add_cascade(label="help",menu=helpmenu)

    root.config(menu=menubar)
    root.mainloop()