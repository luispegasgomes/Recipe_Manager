from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox 

janela_fav = Tk()
janela_fav.geometry("1024x600")
janela_fav.title("Favoritos")
janela_fav.configure(bg='#aff7ff')


def consult():
    try:
        itemSelecionado = tree.selection()[0]
        valors = tree.item(itemSelecionado,"values")
        descriçao_receita = str(valors[2])
        favoritos.insert("end", descriçao_receita)
        print(descriçao_receita)
            
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
def edit():
    f = open("ficheiros\\favoritos.txt", "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for linha in lista:
        campos = linha.split(";")
        if (campos[1] == 'Outros'):
            tree.insert("", "end", values = (campos[0], campos[1], campos[2]))

def remover2():
    try:
        itemSelecionado = tree.selection()[0]
        valors = tree.item(itemSelecionado,"values")
        print(valors)
        nome1 = str(valors[0])
        tree.delete(itemSelecionado)
        with open("ficheiros\\favoritos.txt", "r") as f_fav:
            lines = f_fav.readlines()
        with open("ficheiros\\favoritos.txt", "w") as f_fav:
            for line in lines:
                campos = line.split(";")
                if campos[0] != nome1:
                    f_fav.write(line)
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  



# Painel Consultar
panel2 = LabelFrame(janela_fav, text = 'Consultar', width = 500, height = 500, bd = "3", relief = "sunken")
panel2.place(x=450, y=35)

# Painel Edições
panel3 = LabelFrame(janela_fav, text = 'Receitas favoritas', width = 300, height = 300, bd = "3", relief = "sunken")
panel3.place(x=75, y=35)

# Listbox
lbox_fav = Listbox(panel3, width = 45, height = 16, bd = "3", relief = "sunken")
lbox_fav.place(x=10, y=10)
    
# ---Botões---

# Botão Consultar
btn_consultar=Button(janela_fav, text='Consultar', fg='white', width=20, height=3, relief='ridge', command = consult, bg="#499dc0")
btn_consultar.place(x=145, y=350)
# Botão Editar
btn_editar=Button(janela_fav, text='Editar', fg='white', width=20, height=3, relief='ridge', command = edit, bg="#499dc0")
btn_editar.place(x=145, y=420)
# Botão Remover
btn_remove=Button(janela_fav, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover2, bg="#499dc0")
btn_remove.place(x=145, y=490)

ficheiro_tree = open("ficheiros\\favo ritos.txt", "r", encoding="utf-8")
lista = ficheiro_tree.readlines()
ficheiro_tree.close()
for linha in lista:
    lista = linha.split(";")
    tree.insert("", "end", values = (lista[0],lista[1],lista[2],lista[3],lista[4]))

# Componente treeview 
tree = ttk.Treeview(panel2, columns = ("Receita", "Descrição","Duração","Categorias"), show = "headings")
tree.column("Receita", width = 115, anchor="c")
tree.column("Descrição", width = 115, anchor="c")
tree.column("Duração", width=115, anchor="c")
tree.column("Categorias", width=105, anchor="c")
tree.heading("Receita", text="Receita")
tree.heading("Descrição", text="Descrição")
tree.heading("Duração", text="Duração")
tree.heading("Categorias", text="Categorias")
tree.place(x=15, y=10)





janela_fav.mainloop()