import tkinter as tk
from tkinter import messagebox

class gui:
    def start(self):
        self.encrypt()
        self.filer()

    def sh(self):
        self.char='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.str_in=self.retrieve()
        self.str_out=''
        self.str_len=len(self.str_in)
        self.i=0       
        self.start()
    
    def encrypt(self):
        for self.i in range(self.str_len):
            a=self.str_in[self.i]
            if a=='\n' or a==' ' or a=='.' or a==',' or a=='\t' or a=="\"" or a=="\'" or a==':' or a==';' or a=='!' or a=='&' or a=='%' or a=='$' or a=='@' or a=='#':
                self.str_out+=a
                continue
            loc=self.char.find(a.upper())
            new_loc=(loc+13)%26 #We're using modulus so that the range stays between 26
            self.str_out+=self.char[new_loc]

    def filer(self):
        f=open("Output.txt",'w+')
        f.writelines(self.str_out.lower())
        f.close()
        messagebox.showinfo(title="Prompt",message="Encrypted Text Is Written To Output.txt")
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("800x400")
        self.root.title("ROT13 ENCRYPTION")
        self.label=tk.Label(self.root,text="Welcome to ROT13 Encryption",font=("Arial",20))

        self.label.pack(padx='0',pady='10')
        self.textbox=tk.Text(self.root,height=10,font=('Arial',16))
        self.textbox.pack()
        
        self.button=tk.Button(self.root,text="Encrypt",font=('Arial',18),command=lambda : self.sh())
        
        self.button.pack(padx=10,pady=10)

    def retrieve(self):
        self.inputvalue=self.textbox.get("1.0","end-1c")
        return self.inputvalue





gui()

