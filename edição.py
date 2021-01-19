from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

janela = Tk()
janela.title('Recipe Manager')
janela.geometry("1024x600")
janela.configure(bg='#aff7ff')
janela.resizable(0, 0)
"""imgLogo=PhotoImage(file="imagens\\logo.png", width=200, height=200)
    l_logo=Label(janela, image=imgLogo)
    l_logo.place(x=10, y=10)"""
lbl_utilizador = Label(janela, text="Bem vindo(a), utilizador")
lbl_utilizador.place(x=880, y=10)
# Implementar menu
barra_Menu = Menu(janela)

# Constroi o menu
simuladores_Menu = Menu(barra_Menu)
barra_Menu.add_command(label="Home", command="noaction")
barra_Menu.add_command(label="Todas as Receitas", command="noaction")
barra_Menu.add_command(label="Favoritos", command="noaction")
barra_Menu.add_command(label="Contacte-nos", command="noaction")
barra_Menu.add_command(label="About Us", command="noaction")

# Botões
btnadd = Button(janela, text='Gerir as minhas receitas', fg='white',width=35, height=3, relief='ridge', command="pag_user", bg="#499dc0")
btnadd.pack(side=TOP)

btn2 = Button(janela, text='Sopas', fg='black', width=7,height=3, relief='ridge', command="sopas")
btn2.place(x=280, y=80)
btn3 = Button(janela, text='Carne', fg='black', width=7,height=3, relief='ridge', command="noaction")
btn3.place(x=380, y=80)
btn11 = Button(janela, text='Peixe', fg='black', width=7,height=3, relief='ridge', command="noaction")
btn11.place(x=480, y=80)
btn5 = Button(janela, text='Massas', fg='black', width=7,height=3, relief='ridge', command="noaction")
btn5.place(x=580, y=80)
btn6 = Button(janela, text='Breakfast', fg='black', width=7,height=3, relief='ridge', command="noaction")
btn6.place(x=680, y=80)


btn13 = Button(janela, text='Vegetais', fg='black', width=7,height=3, relief='ridge', command="noaction")
btn13.place(x=280, y=160)
btn14 = Button(janela, text='Snacks', fg='black', width=7,height=3, relief='ridge', command="noaction")
btn14.place(x=380, y=160)

btn18 = Button(janela, text='Sobremesas', fg='black', width=7,height=3, relief='ridge', command="noaction")
btn18.place(x=480, y=160)
btn19 = Button(janela, text='Bebidas', fg='black', width=7,height=3, relief='ridge', command="noaction")
btn19.place(x=580, y=160)

btn26 = Button(janela, text='Outros', fg='black', width=7,height=3, relief='ridge', command="noaction")
btn26.place(x=680, y=160)

# Constroi menu Sair, com comando quit
barra_Menu.add_command(label="Sair", command=janela.quit)
janela.configure(menu=barra_Menu)

janela.mainloop()
