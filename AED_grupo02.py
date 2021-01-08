from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox

janela = Tk()
pastaApp=os.path.dirname(__file__)
janela.title('Recipe Manager')
# Largura * Altura
janela.geometry("1024x600")
janela.configure(bg='#aff7ff')
janela.resizable(0,0)
imgLogo=PhotoImage(file=pastaApp+"\\Logo.png", width=200, height=200)
l_logo=Label(janela, image=imgLogo)
l_logo.place(x=10, y=10)
# Funções para a execução do programa
def login():
    janelalogin = Toplevel()
    janelalogin.geometry("300x300")
    janelalogin.title("Login")

    #label username
    lbl_username=Label(janelalogin, text="Username :")
    lbl_username.place(x=20, y=50)

    #label password
    
    lbl_pw=Label(janelalogin, text="Password :", textvariable="pw")
    lbl_pw.place(x=20, y=100)

    #entry username
    txt_username=Entry(janelalogin, width=25)
    txt_username.place(x=100, y=50)

    #entry password
    txt_pw1=Entry(janelalogin, width=25, show="*")
    txt_pw1.place(x=100, y=100)

    #login button
    btn=Button(janelalogin, text="Log in")
    btn.place(x=100, y=150)

    #menu do login
    login_menu = Menu(janelalogin)
    login_menu.add_command(label="Criar conta nova", command=registo)
    janelalogin.configure(menu=login_menu)


    janelalogin.mainloop()

def registo():
    janelaregisto = Toplevel(janela)
    janelaregisto.geometry("500x400")
    janelaregisto.title("Registo")
    janelaregisto.configure(bg='#aff7ff')

    # Botão foto de perfil
    lbl_email=Label(janelaregisto, text="Clique aqui para adicionar a sua foto de perfil")
    lbl_email.place(x=20, y=250)

    #label email
    lbl_email=Label(janelaregisto, text="Email :")
    lbl_email.place(x=20, y=50)

    #label username
    lbl_username=Label(janelaregisto, text="Username :")
    lbl_username.place(x=20, y=100)

    #label password
    pw = StringVar()
    lbl_pw=Label(janelaregisto, text="Password :")
    lbl_pw.place(x=20, y=150)

    #label repeat password
    
    lbl_rpw=Label(janelaregisto, text="Confirmar pw :")
    lbl_rpw.place(x=20, y=200)


    #entry email
    txt_email=Entry(janelaregisto, width=25)
    txt_email.place(x=100, y=50)

    #entry username
    txt_username=Entry(janelaregisto, width=25)
    txt_username.place(x=100, y=100)

    #entry password
    pw = StringVar()
    txt_pw=Entry(janelaregisto, width=25, show="*", textvariable = pw)
    txt_pw.place(x=100, y=150)

    #entry repeat password
    cpw = StringVar()
    txt_rpw=Entry(janelaregisto, width=25, show="*", textvariable = cpw)
    txt_rpw.place(x=100, y=200)
    def mensagem():
        if cpw.get() != pw.get():
            messagebox.showerror("Error", "As passwords não coincidem!")

    #registo button
    btn=Button(janelaregisto, text="Registe-se", command = mensagem)
    btn.place(x=100, y=350)

    janelaregisto.mainloop()

def add_receita():
    janela_add = Toplevel(janela)
    janela_add.geometry("300x500")
    janela_add.title("Nova Receita")
    # Caixa de texto
    texto_intro = StringVar()
    texto_intro.set('Clique aqui para inserir um texto')
    caixa_txt=Text(janela_add, width=30, height=15)
    caixa_txt.place(x=27, y=25)
    # Entry nome da receita
    txt_nreceita=Entry(janela_add, width=40)
    txt_nreceita.place(x=27, y=300)
    # Entry categoria
    txt_categoria=Entry(janela_add, width=40)
    txt_categoria.place(x=27, y=340)
    
    # Botões
    btn1=Button(janela_add, text='Guardar', fg='white', width=34, height=1, relief='ridge', command = "noaction", bg="#499dc0")
    btn1.place(x=27, y=380)
    janela_add.mainloop()

def sopas():
    janela_sopas = Toplevel(janela)
    janela_sopas.geometry("600x500")
    janela_sopas.title("Todas as receitas de Sopas")
    painel2 = PanedWindow(janela_sopas, width = 200, height = 200, bd = "3", relief = "sunken")
    painel2.place(x=300, y=20)
    #self.tree = ttk.Treeview(painel2, collums = ("Número", "Data", "Hora", "Movimento"), show = "headings")
    #self.tree.collum("Número", width = 100, anchor = 'c')
    #self.tree.place(x=5, y=5)
    janela_sopas.mainloop()

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
btnadd=Button(janela, text='Adicione uma nova Receita!', fg='white', width=35, height=3, relief='ridge', command = add_receita, bg="#499dc0")
btnadd.pack(side=TOP)
btnlogin=Button(janela, text='Faça LOGIN!', fg='white', width=30, height=2, relief='ridge', command = login, bg="#499dc0")
btnlogin.place(x=220, y=450)
btnregisto=Button(janela, text='Ainda não criou uma conta? Registe-se', fg='white', width=30, height=2, relief='ridge', command = registo, bg="#499dc0")
btnregisto.place(x=580, y=450)



btn2=Button(janela, text='Sopas', fg='black', width=7, height=3, relief='ridge', command = sopas)
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
