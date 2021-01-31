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


# Painel Consultar
panel2 = LabelFrame(janela_fav, text = 'Consultar', width = 500, height = 500, bd = "3", relief = "sunken")
panel2.place(x=450, y=35)

# Painel Edições
panel3 = LabelFrame(janela_fav, text = 'Receitas favoritas', width = 300, height = 300, bd = "3", relief = "sunken")
panel3.place(x=75, y=35)

# Listbox
lbox_gerir = Listbox(panel3, width = 45, height = 16, bd = "3", relief = "sunken")
lbox_gerir.place(x=10, y=10)
    
# ---Botões---

# Botão Consultar
btn_consultar=Button(janela_fav, text='Consultar', fg='white', width=20, height=3, relief='ridge', command = "noaction", bg="#499dc0")
btn_consultar.place(x=145, y=350)
# Botão Editar
btn_editar=Button(janela_fav, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "noaction", bg="#499dc0")
btn_editar.place(x=145, y=420)
# Botão Remover
btn_remove=Button(janela_fav, text='Remover', fg='white', width=20, height=3, relief='ridge', command = "noaction", bg="#499dc0")
btn_remove.place(x=145, y=490)


# Componente treeview 
tree = ttk.Treeview(panel2, columns = ("Receita", "Descrição"), show = "headings")
tree.column("Receita", width = 100, anchor="c")
tree.column("Descrição", width = 350, anchor="c")
tree.heading("Receita", text="Receita")
tree.heading("Descrição", text="Descrição")
tree.place(x=15, y=10)


janela_fav.mainloop()