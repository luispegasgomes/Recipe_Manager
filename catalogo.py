from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox 


def combobox_option(*args):

    if selected.get() == "Título":
        f = open(receitas, "r", encoding="utf-8")
        lista1 = f.readlines()
        f.close()

        option = lista1
    elif selected.get() == "Categoria":
        f = open(categorias, "r", encoding="utf-8")
        lista2 = f.readlines()
        f.close()

        option = lista2

    cbx2.config(values=option)









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

cbx1 = ttk.Combobox(janela_catalogo, width=15, textvariable=selected, values=["Titulo","Categoria"])
cbx1.bind("<<ComboboxSelected>>",combobox_option)
cbx1.place(x=590, y=50)

cbx2 = ttk.Combobox(janela_catalogo, width=15)
cbx2.place(x=460, y=50)

# ---------BUTTON---------
search_btn = Button(janela_catalogo, text="Procurar", fg="white", width=9, height=1, relief='ridge', command = "noaction", bg="#499dc0")
search_btn.place(x=400, y=90)



# ------ORDENAR POR------

sort_lbl = LabelFrame(janela_catalogo, text="Ordenar por", bd=3, height=100, width=200)
sort_lbl.place(x=400, y=250)

radio1 = Radiobutton(sort_lbl, text="Views")
radio1.place(x=20, y=25)

radio2 = Radiobutton(sort_lbl, text="Rating")
radio2.place(x=100, y=25)
janela_catalogo.mainloop()
