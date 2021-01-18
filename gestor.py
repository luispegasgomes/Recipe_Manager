from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
janela = Tk()
janela.title('Recipe Manager')
janela.geometry("1024x600")
janela.configure(bg='#aff7ff')
janela.resizable(0,0)
imgLogo=PhotoImage(file="imagens\\logo.png", width=200, height=200)
l_logo=Label(janela, image=imgLogo)
l_logo.place(x=10, y=10)
# Implementar menu
barra_Menu = Menu(janela)

# Constroi o menu
simuladores_Menu = Menu(barra_Menu)
barra_Menu.add_command(label = "Home", command = "noaction")
barra_Menu.add_command(label = "Todas as Receitas", command = "noaction")
barra_Menu.add_command(label = "Favoritos", command = "noaction")
barra_Menu.add_command(label = "Contacte-nos", command = "noaction")
barra_Menu.add_command(label = "About Us", command = "noaction")

# Botões
btnadd=Button(janela, text='Adicione uma nova Receita!', fg='white', width=35, height=3, relief='ridge', command = "add_receita", bg="#499dc0")
btnadd.pack(side=TOP)



btn2=Button(janela, text='Sopas', fg='black', width=7, height=3, relief='ridge', command = "sopas")
btn2.place(x=280, y=80)
btn3=Button(janela, text='Breakfast', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn3.place(x=380, y=80)
btn4=Button(janela, text='Frango', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn4.place(x=480, y=80)
btn5=Button(janela, text='Peixe', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn5.place(x=580, y=80)
btn6=Button(janela, text='Carne Vermelha', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn6.place(x=680, y=80)

btn10=Button(janela, text='Acompanhamentos', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn10.place(x=280, y=160)
btn11=Button(janela, text='Massa', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn11.place(x=380, y=160)
btn12=Button(janela, text='Cassarolas', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn12.place(x=480, y=160)
btn13=Button(janela, text='Vegetais', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn13.place(x=580, y=160)
btn14=Button(janela, text='Snacks', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn14.place(x=680, y=160)

btn18=Button(janela, text='Geleias', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn18.place(x=280, y=240)
btn19=Button(janela, text='Bebidas', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn19.place(x=380, y=240)
btn20=Button(janela, text='Marisco', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn20.place(x=480, y=240)
btn21=Button(janela, text='Bolos', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn21.place(x=580, y=240)
btn22=Button(janela, text='Biscoitos', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn22.place(x=680, y=240)

btn23=Button(janela, text='Vegetais', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn23.place(x=280, y=320)
btn24=Button(janela, text='Molhos', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn24.place(x=380, y=320)
btn25=Button(janela, text='Aperitivos', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn25.place(x=480, y=320)
btn26=Button(janela, text='Outros', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn26.place(x=580, y=320)
btn27=Button(janela, text='+', fg='black', width=7, height=3, relief='ridge', command = "noaction")
btn27.place(x=680, y=320)

# Constroi menu Sair, com comando quit 
barra_Menu.add_command(label = "Sair", command = janela.quit)
janela.configure(menu=barra_Menu)

janela.mainloop()