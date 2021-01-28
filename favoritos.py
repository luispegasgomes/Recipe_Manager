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
#---IMAGENS DA JANELA---
imgLogo=PhotoImage(file="imagens\\logo.png", width=200, height=200)
l_logo=Label(janela_fav, image=imgLogo)
l_logo.place(x=70, y=50)
imgFav=PhotoImage(file="imagens\\favoritos.png", width=200, height=200)
l_Fav=Label(janela_fav, image=imgFav)
l_Fav.place(x=70, y=280)

# Painel Consultar
panel2 = LabelFrame(janela_fav, text = 'Consultar', width = 550, height = 550, bd = "3", relief = "sunken", bg='#aff7ff')
panel2.place(x=400, y=10)

# Text para a leitura dos dados
caixa_txt=Text(panel2, width=62, height=10)
caixa_txt.place(x=20, y=350)
    
# ---Botões---

# Botão Consultar
btn_consultar=Button(panel2, text='Consultar', fg='white', width=20, height=3, relief='ridge', command = "consult", bg="#499dc0")
btn_consultar.place(x=30, y=260)
# Botão Editar
btn_editar=Button(panel2, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "edit", bg="#499dc0")
btn_editar.place(x=190, y=260)
# Botão Remover
btn_remove=Button(panel2, text='Remover', fg='white', width=20, height=3, relief='ridge', command = "remover", bg="#499dc0")
btn_remove.place(x=350, y=260)

# Componente treeview 
tree = ttk.Treeview(panel2, columns = ("Nome da Receita", "Categoria", "Duração", "Descrição"), show = "headings")
tree.column("Nome da Receita", width = 200, anchor="c")
tree.column("Categoria", width = 100, anchor="c")
tree.column("Descrição", width = 100, anchor="c")
tree.column("Duração", width = 100, anchor="c")
tree.heading("Nome da Receita", text="Nome da Receita")
tree.heading("Categoria", text="Categoria")
tree.heading("Descrição", text="Descrição")
tree.heading("Duração", text="Duração")
tree.place(x=15, y=10)

janela_fav.mainloop()