from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox

janelaregisto = Tk()
janelaregisto.geometry("1024x600")
janelaregisto.title("Registo")
janelaregisto.configure(bg='#aff7ff')
#original_frame.withdraw()

# Botão foto de perfil
btn_foto=Button(janelaregisto, text="Clica aqui para adicionares a tua foto de perfil!")
btn_foto.place(x=400, y=250)

#label email
lbl_email=Label(janelaregisto, text="Email :")
lbl_email.place(x=400, y=50)

#label username
    
lbl_username=Label(janelaregisto, text="Username :")
lbl_username.place(x=400, y=80)

#label password
    
lbl_pw=Label(janelaregisto, text="Password :")
lbl_pw.place(x=400, y=150)

#label repeat password
    
lbl_rpw=Label(janelaregisto, text="Confirmar password")
lbl_rpw.place(x=400, y=200)

# Entry email
txt_email=Entry(janelaregisto, width=25)
txt_email.place(x=100, y=50)

# Entry username
txt_username=Entry(janelaregisto, width=25)
txt_username.place(x=100, y=100)

# Entry password
txt_pw=Entry(janelaregisto, width=25, show="*")
txt_pw.place(x=100, y=150)

# Entry repeat password
cpw = StringVar()
txt_rpw=Entry(janelaregisto, width=25, show="*", textvariable = cpw)
txt_rpw.place(x=100, y=200)

# Registo button
btnw=Button(janelaregisto, text="Regista-te", command = "registar", width=20)
btnw.place(x=400, y=350)
"""def mensagem():
    if cpw.get() != pw.get():
        messagebox.showerror("Error", "As passwords não coincidem!")"""
    

janelaregisto.mainloop()