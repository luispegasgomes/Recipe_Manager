from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
janela_add = Tk()
janela_add.geometry("1366x800")
janela_add.title("Recipe Manager")

# Painel Adicionar receita
panel1 = LabelFrame(janela_add, text='Adicionar receita', width=350, height=500, bd="3", relief="sunken")
panel1.place(x=10, y=10)

# Painel Consultar
panel2 = LabelFrame(janela_add, text='Consultar', width=500, height=500, bd="3", relief="sunken")
panel2.place(x=800, y=10)

# Painel Edições
panel3 = LabelFrame(janela_add, text='Todas as minhas receitas', width=300, height=300, bd="3", relief="sunken")
panel3.place(x=425, y=10)

# Caixa de texto
caixa_txt = Text(panel1, width=30, height=15)
caixa_txt.place(x=20, y=15)

# Listbox
lbox_gerir = Listbox(panel3, width=45, height=16, bd="3", relief="sunken")
lbox_gerir.place(x=10, y=10)

# Entry nome da receita
txt_nreceita = Entry(panel1, width=40)
txt_nreceita.place(x=20, y=310)
lbl_name = Label(panel1, text="Nome da receita :", fg="black", font=("Helvetica", 11))
lbl_name.place(x=16, y=280)

# ---Botões---
# Botão Adicionar
btn1 = Button(panel1, text='Adicionar', fg='white', width=40, height=1, relief='ridge', command="adicionar", bg="#499dc0")
btn1.place(x=20, y=420)

# Botão Consultar
btn_consultar = Button(janela_add, text='Consultar', fg='white', width=20, height=3, relief='ridge', command="consultar", bg="#499dc0")
btn_consultar.place(x=500, y=330)

# Botão Editar
btn_editar = Button(janela_add, text='Editar', fg='white', width=20, height=3, relief='ridge', command="verificar_admin", bg="#499dc0")
btn_editar.place(x=500, y=400)

# Botão Remover
btn_remove = Button(janela_add, text='Remover', fg='white', width=20, height=3, relief='ridge', command="remover", bg="#499dc0")
btn_remove.place(x=500, y=470)

# Componente treeview
tree = ttk.Treeview(panel2, columns=("Receita", "Descrição"), show="headings")
tree.column("Receita", width=100, anchor="c")
tree.column("Descrição", width=350, anchor="c")
tree.heading("Receita", text="Receita")
tree.heading("Descrição", text="Descrição")
tree.place(x=15, y=10)

# Combobox para a categoria
lbl_categorias = Label(panel1, text="Selecione a categoria a que pretende adicionar :", fg="black", font=("Helvetica", 11))
lbl_categorias.place(x=16, y=340)
lista = ['Sopas', 'Carne', 'Peixe', 'Massas', 'Breakfast', 'Vegetais', 'Snacks', 'Sobremesas', 'Bebidas', 'Outros']
cb_categorias = Combobox(panel1, values=lista)
cb_categorias.place(x=20, y=370)

ficheiro = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
lista_categorias = []
for linha in ficheiro:
    campos = linha.split(";")
    lista_categorias.append(campos[0])
for j in lista_categorias:
    lbox_gerir.insert(END, j)

janela_add.mainloop()
