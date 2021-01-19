from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog 



def escolhe_imagem():
    # file dialog, para selecionar ficheiro em disco
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file",filetypes = (("gif files","*.gif"),("jpeg files","*.jpg"),("png files", "*.png"), ("all files","*.*")))
    global img 
    img = ImageTk.PhotoImage(file = filename)
janelaregisto = Tk()
janelaregisto.geometry("900x600")
janelaregisto.title("Registo")
janelaregisto.configure(bg='#aff7ff')
#original_frame.withdraw()
lbl_username=Label(janelaregisto, text="Cria a tua conta !", font=("Helvetica",20))
lbl_username.place(x=320, y=10)
# Botão foto de perfil
btn_foto=Button(janelaregisto, text="Adiciona a tua foto de perfil!", width=25, height=5, command = escolhe_imagem)
btn_foto.place(x=600, y=180)

# Label email
lbl_email=Label(janelaregisto, text="Email :")
lbl_email.place(x=350, y=70)

# Entry email
txt_email=Entry(janelaregisto, width=25)
txt_email.place(x=350, y=100)


# Label username
    
lbl_username=Label(janelaregisto, text="Username :")
lbl_username.place(x=350, y=130)

# Entry username
txt_username=Entry(janelaregisto, width=25)
txt_username.place(x=350, y=160)

# Label password
lbl_pw=Label(janelaregisto, text="Password :")
lbl_pw.place(x=350, y=190)

# Entry password
txt_pw=Entry(janelaregisto, width=25, show="*")
txt_pw.place(x=350, y=220)

# Label repeat password
lbl_rpw=Label(janelaregisto, text="Confirmar password :")
lbl_rpw.place(x=350, y=250)

# Entry repeat password
txt_rpw=Entry(janelaregisto, width=25, show="*")
txt_rpw.place(x=350, y=280)

# Registo button
btnw=Button(janelaregisto, text="Regista-te", fg='white', width=30, height=2, relief='ridge', command = 'registar', bg="#499dc0")
btnw.place(x=325, y=350)



janelaregisto.mainloop()