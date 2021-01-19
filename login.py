from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox

janelalogin = Tk()
janelalogin.geometry("900x600")
janelalogin.configure(bg='#aff7ff')
janelalogin.title("Iniciar Sessão")
imgLogo=PhotoImage(file="imagens\\logo.png", width=200, height=200)
l_logo=Label(janelalogin, image=imgLogo)
l_logo.place(x=10, y=10)
#original_frame.withdraw()
    
# Label Faça o seu login
lbl_username=Label(janelalogin, text="Iniciar sessão", font=("Helvetica",20))
lbl_username.place(x=390, y=10)

# Label username
lbl_username=Label(janelalogin, text="Username :")
lbl_username.place(x=400, y=70)

# Entry username
txt_username=Entry(janelalogin, width=25)
txt_username.place(x=400, y=100)

# Label password
        
lbl_pw=Label(janelalogin, text="Password :")
lbl_pw.place(x=400, y=140)

# Entry password
txt_pw1=Entry(janelalogin, width=25, show="*")
txt_pw1.place(x=400, y=170)

# Login button
btn=Button(janelalogin, text="Iniciar Sessão", command = "loginBe", width=40)
btn.place(x=335, y=300)

janelalogin.mainloop()