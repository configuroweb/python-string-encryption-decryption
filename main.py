from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    screen2=Toplevel(screen)
    screen2.title("DECRYPTION")
    screen2.geometry("400x200")
    screen2.configure(bg="#00bd56")

    message=text1.get(1.0,END)
    decode_message=message.encode("ascii")
    base64_bytes=base64.b64decode(decode_message)
    decrypt=base64_bytes.decode("ascii")

    Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
    text2=Text(screen2,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=150)
    text2.insert(END,decrypt)


def encrypt():
    
    screen1=Toplevel(screen)
    screen1.title("ENCRYPTION")
    screen1.geometry("400x200")
    screen1.configure(bg="#ed3833")
        
    message=text1.get(1.0,END)
    encode_message=message.encode("ascii")
    base64_bytes=base64.b64encode(encode_message)
    encrypt=base64_bytes.decode("ascii")

    Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
    text2=Text(screen1,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=150)

    text2.insert(END,encrypt)


def main_screen():

    global screen
    global code
    global text1
     
    screen = Tk()
    screen.geometry("375x320")
    screen.title("Encrypt & Decrypt a String Program")

    def reset():
        code.set("")
        text1.delete(1.0,END)
   
    Label(text="Enter string here",fg="black",font=("ARIAL",12)).place(x=10,y=10)
    text1 = Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
   

    Button(text="ENCRYPT",height="2",width="23",bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=200)
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=200)
    Button(text="RESET",height="2",width="50",bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=250)

    screen.mainloop()

main_screen()
