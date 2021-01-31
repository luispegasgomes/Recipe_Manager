from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
janela_sopas = Tk()
janela_sopas.title('Gestão de Sopas')
janela_sopas.geometry("800x600")
janela_sopas.configure(bg='#aff7ff')
janela_sopas.resizable(0, 0)
# Container Canvas
ctn_canvas = Canvas(janela_sopas, width = 200, height = 200, bd = 0, relief = "sunken")
ctn_canvas.place(x=100, y=20)
# Cria a imagem
img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
ctn_canvas.create_image(100,100, image = img_sopas)

# Listbox
lbox_sopas = Listbox(janela_sopas, width = 40, height = 12, bd = "3", relief = "sunken")
lbox_sopas.place(x=450, y=20)

# Componente treeview 
tree = ttk.Treeview(janela_sopas, columns = ("Receita", "Descrição"), show = "headings")
tree.column("Receita", width = 100, anchor="c")
tree.column("Descrição", width = 350, anchor="c")
tree.heading("Receita", text="Receita")
tree.heading("Descrição", text="Descrição")
tree.place(x=170, y=300)
janela_sopas.mainloop()