from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox 


def combobox_option(*args):

    if selected.get() == "Titulo":

        f = open(receitas, "r", encoding="utf-8")
        lista1 = f.readlines()

        f.close()

        option = lista1
        cbx2.set(option[0])
    elif selected.get() == "Categoria":

        f = open(categorias, "r", encoding="utf-8")
        lista2 = f.readlines()

        f.close()

        option = lista2
        cbx2.set(option[0])
    elif selected.get() == "Ingredientes":

        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista3 = f.readlines()
        f.close()
        for linha in lista3:
            campos = linha.split(";")
            option = campos[4]

        cbx2.set(option)


    cbx2.config(values=option)


def search():

    if selected.get() == "Procurar por...":
        messagebox.showerror("ERRO", "Não escolheu uma opção")
    else:
        lbox.delete(0, "end")

        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            print(linha)
            campos = linha.split(";")
            if cbx2.get() == campos[1] or cbx2.get() == campos[0] or campos[4]:
                lbox.insert("end", campos[0])


#def sort():







receitas = "ficheiros\\receitas.txt"
categorias = "ficheiros\\categorias.txt"

janela_catalogo = Tk()
janela_catalogo.geometry("900x500")
janela_catalogo.title("Catálogo de Receitas")


# ---------LISTBOX----------

lbox = Listbox(janela_catalogo, height=20, width=50, bd=2)
lbox.place(x=40, y=50)

f = open(receitas, "r", encoding="utf-8")
lista = f.readlines()
f.close()
for linha in lista:
    lbox.insert("end", linha)

# ------COMBOBOXES------

search_lbl = Label(janela_catalogo, text="Procurar : ")
search_lbl.place(x=400, y=50)

selected = StringVar()
selected.set("Procurar por...")

cbx1 = ttk.Combobox(janela_catalogo, width=15, textvariable=selected, values=["Titulo","Categoria","Ingredientes"])
cbx1.bind("<<ComboboxSelected>>",combobox_option)
cbx1.place(x=590, y=50)

cbx2 = ttk.Combobox(janela_catalogo, width=15)
cbx2.place(x=460, y=50)

# ---------BUTTON---------
search_btn = Button(janela_catalogo, text="Procurar", fg="white", width=9, height=2, relief='ridge', command = search, bg="#499dc0")
search_btn.place(x=400, y=90)



# ------ORDENAR POR------

sort_frame = LabelFrame(janela_catalogo, text="Ordenar por", bd=3, height=100, width=200)
sort_frame.place(x=400, y=250)

val = StringVar()
val.set("views")
radio1 = Radiobutton(sort_frame, text="Views", variable=val, value="views")
radio1.place(x=20, y=25)

radio2 = Radiobutton(sort_frame, text="Rating", variable=val, value="rating")
radio2.place(x=100, y=25)

sort_btn = Button(janela_catalogo, text="Ordenar", width=10, height=2, fg="white", bg="#499dc0")
sort_btn.place(x=640, y=280)



janela_catalogo.mainloop()