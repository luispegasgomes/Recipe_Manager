from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox 

janela = Tk()
janela.geometry("1024x600")
janela.title("top most rated")
janela.configure(bg='#aff7ff')

#funçoes

def likes():
    f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for linha in lista:
        campos = linha.split(";")
        tree.insert("", "end", values = (campos[0], campos[1], campos[2]))


    '''total=len(results)
    prim=results[0]
    cont1=results.count(prim)
    for i in range total:
        if results[i]==prim:
            results[i]="0"
    for a in range total:
        if results[a]!="0":
            results[a]=sec
            cont2=results.count(sec)
    break'''


#paineis

panel1 = LabelFrame(janela, text = 'Ordenar por :', width = 300, height = 380, bd = "3", relief = "sunken")
panel1.place(x=75, y=35)

panel2 = LabelFrame(janela, text = 'Top most rated', width = 480, height = 480, bd = "3", relief = "sunken")
panel2.place(x=450, y=35)

#botoes

btn1=Button(panel1, text='Gostos', fg='white', width=20, height=3, relief='ridge', command=likes, bg="#499dc0")
btn1.place(x=70, y=70)

btn2=Button(panel1, text='Comentários', fg='white', width=20, height=3, relief='ridge', bg="#499dc0")
btn2.place(x=70, y=140)

btn3=Button(panel1, text='Favoritos',  fg='white', width=20, height=3, relief='ridge', bg="#499dc0")
btn3.place(x=70, y=210)

#treeview

tree = ttk.Treeview(panel2, columns = ("Receita", "Descrição","Gostos"), show = "headings")
tree.column("Receita", width = 150, anchor="c")
tree.column("Descrição", width = 150, anchor="c")
tree.column("Gostos", width = 150, anchor="c")
tree.heading("Receita", text="Receita")
tree.heading("Descrição", text="Descrição")
tree.heading("Gostos", text="Gostos")
tree.place(x=15, y=10)

janela.mainloop()