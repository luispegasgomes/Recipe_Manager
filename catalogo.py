from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox 




def combobox_option(*args):

    

    if selected.get() == "Titulo":


        f1 = open("ficheiros\\titulos.txt", "r", encoding="utf-8")
        lista1 = f1.readlines()
        f1.close()

        option = lista1
        cbx2.set(option[0])

        
    elif selected.get() == "Categoria":

        f = open("ficheiros\\categorias.txt", "r", encoding="utf-8")
        lista2 = f.readlines()
        f.close()

        option = lista2
        cbx2.set(option[0])
    
    cbx2.config(values=option)


def search():

    if selected.get() == "Procurar por...":
        messagebox.showerror("ERRO", "Não escolheu uma opção")
    else:
        linhas = tree.get_children()
        for item in linhas:
            tree.delete(item)

        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        
        lista = f.readlines()
        f.close()

        for linha in lista:
            campos = linha.split(";")
            if cbx2.get() in linha:
                tree.insert("","end", values=(campos[1], campos[2], campos[3], campos[5], campos[4]))


#def sort():





janela_catalogo = Tk()
janela_catalogo.geometry("900x400")
janela_catalogo.title("Catálogo de Receitas")


# ---------LISTBOX----------

# Componente treeview 
tree = ttk.Treeview(janela_catalogo, columns = ("Nome da Receita", "Categoria", "Duração", "Descrição", "Ingredientes"), show = "headings")
tree.column("Nome da Receita", width = 100, anchor="c")
tree.column("Categoria", width = 100, anchor="c")
tree.column("Descrição", width = 100, anchor="c")
tree.column("Duração", width = 100, anchor="c")
tree.column("Ingredientes", width = 100, anchor="c")
tree.heading("Nome da Receita", text="Nome da Receita")
tree.heading("Categoria", text="Categoria")
tree.heading("Descrição", text="Descrição")
tree.heading("Duração", text="Duração")
tree.heading("Ingredientes", text="Ingredientes")
tree.place(x=15, y=50)

f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
lista = f.readlines()
f.close()
for linha in lista:
    campos = linha.split(";")
    #if (campos[0] == utilizador):
    tree.insert("", "end", values = (campos[1], campos[2], campos[3], campos[5], campos[4]))

# ------COMBOBOXES------

search_lbl = Label(janela_catalogo, text="Procurar : ")
search_lbl.place(x=540, y=50)

selected = StringVar()
selected.set("Procurar por...")

cbx1 = ttk.Combobox(janela_catalogo, width=15, textvariable=selected, values=["Titulo","Categoria"])
cbx1.bind("<<ComboboxSelected>>",combobox_option)
cbx1.place(x=730, y=50)

cbx2 = ttk.Combobox(janela_catalogo, width=15)
cbx2.place(x=600, y=50)

# ---------BUTTON---------
search_btn = Button(janela_catalogo, text="Procurar", fg="white", width=9, height=2, relief='ridge', command = search, bg="#499dc0")
search_btn.place(x=540, y=90)



# ------ORDENAR POR------

sort_frame = LabelFrame(janela_catalogo, text="Ordenar por", bd=3, height=100, width=200)
sort_frame.place(x=550, y=180)

val = StringVar()
val.set("views")
radio1 = Radiobutton(sort_frame, text="Views", variable=val, value="views")
radio1.place(x=20, y=25)

radio2 = Radiobutton(sort_frame, text="Rating", variable=val, value="rating")
radio2.place(x=100, y=25)

sort_btn = Button(janela_catalogo, text="Ordenar", width=10, height=2, fg="white", bg="#499dc0")
sort_btn.place(x=780, y=200)

f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
lista = f.readlines()
f.close()
for linha in lista:
    campos = linha.split(";")
    f1 = open("ficheiros\\titulos.txt", "a", encoding="utf-8")
    f1.write(campos[1] + "\n")
f1.close()

janela_catalogo.mainloop()