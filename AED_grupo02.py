from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox

def login():
    def loginBe():
        with open('ficheiros\\utilizadores.txt', 'r', encoding="utf-8") as arquivoUtilizador:
            utilizadores = arquivoUtilizador.readlines()
        with open('ficheiros\\senhas.txt', 'r', encoding="utf-8") as arquivoUtilizador:
            senhas = arquivoUtilizador.readlines()
        
        utilizadores = list(map(lambda x: x.replace('\n',''), utilizadores))
        senhas = list(map(lambda x: x.replace('\n',''), senhas))

        utilizador = txt_username.get()
        senha = txt_pw1.get()

        logado = False

        for i in range(len(utilizadores)):
            if utilizador == utilizadores[i] and senha == senhas[i]:
                print('Utilizador logado.')
                pag_inicial()
                janelalogin.destroy()
                logado = True
        if not logado:
            messagebox.showwarning("Error", "Utilizador ou password incorretos.")
            janelalogin.destroy()

    janelalogin = Tk()
    janelalogin.geometry("900x600")
    janelalogin.configure(bg='#aff7ff')
    janelalogin.title("Iniciar Sessão")
    """imgLogo2=PhotoImage(file="imagens\\logo.png", width=200, height=200)
    l_logo2=Label(janelalogin, image=imgLogo2)
    l_logo2.place(x=10, y=10)"""
    original_frame.withdraw()
        
    # Label Faça o seu login
    lbl_username=Label(janelalogin, text="Iniciar sessão", font=("Helvetica",20))
    lbl_username.place(x=390, y=10)

    # Label username
    lbl_username=Label(janelalogin, text="Username :")
    lbl_username.place(x=400, y=70)

    # Entry username
    txt_username=Entry(janelalogin, width=25)
    txt_username.place(x=400, y=100)

    # Label password
            
    lbl_pw=Label(janelalogin, text="Password :")
    lbl_pw.place(x=400, y=140)

    # Entry password
    txt_pw1=Entry(janelalogin, width=25, show="*")
    txt_pw1.place(x=400, y=170)

    # Login button
    btn=Button(janelalogin, text="Iniciar Sessão", command = loginBe, width=40)
    btn.place(x=335, y=300)

    janelalogin.mainloop()

def registo():
    def registar():
        try:
            with open('ficheiros\\utilizadores.txt', 'a', encoding="utf-8") as arquivoUtilizador_1:
                arquivoUtilizador_1.write(txt_username.get() + '\n')
            with open('ficheiros\\senhas.txt', 'a', encoding="utf-8") as arquivoUtilizador:
                arquivoUtilizador.write(txt_pw.get() + '\n')
            janelaregisto.destroy()
            login()
        except:
            print('Houve um erro')
    janelaregisto = Toplevel(janela_principal)
    janelaregisto.geometry("1024x600")
    janelaregisto.title("Registo")
    janelaregisto.configure(bg='#aff7ff')
    original_frame.withdraw()

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
    
    lbl_pw=Label(janelaregisto, text="Password :")
    lbl_pw.place(x=20, y=150)

    #label repeat password
    
    lbl_rpw=Label(janelaregisto, text="Confirmar pw :")
    lbl_rpw.place(x=20, y=200)

    # Entry email
    txt_email=Entry(janelaregisto, width=25)
    txt_email.place(x=100, y=50)

    # Entry username
    txt_username=Entry(janelaregisto, width=25)
    txt_username.place(x=100, y=100)

    # Entry password
    txt_pw=Entry(janelaregisto, width=25, show="*")
    txt_pw.place(x=100, y=150)

    #entry repeat password
    cpw = StringVar()
    txt_rpw=Entry(janelaregisto, width=25, show="*", textvariable = cpw)
    txt_rpw.place(x=100, y=200)
    #registo button
    btnw=Button(janelaregisto, text="Registe-se", command = registar)
    btnw.place(x=100, y=350)
    """def mensagem():
        if cpw.get() != pw.get():
            messagebox.showerror("Error", "As passwords não coincidem!")"""
    

    janelaregisto.mainloop()

def pag_inicial():
    janela = Tk()
    janela.title('Recipe Manager')
    janela.geometry("1024x600")
    janela.configure(bg='#aff7ff')
    janela.resizable(0,0)
    """imgLogo3=PhotoImage(file="imagens\\logo.png", width=200, height=200)
    l_logo3=Label(janela, image=imgLogo3)
    l_logo3.place(x=10, y=10)"""
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

def add_receita():
    janela_add = Toplevel(janela_principal)
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
    janela_sopas = Toplevel(janela_principal)
    janela_sopas.geometry("600x500")
    janela_sopas.title("Todas as receitas de Sopas")
    painel2 = PanedWindow(janela_sopas, width = 200, height = 200, bd = "3", relief = "sunken")
    painel2.place(x=300, y=20)
    tree = ttk.Treeview(painel2, columns = ("Número", "Data", "Hora", "Movimento"), show = "headings")
    tree.column("Número", width = 100, anchor = 'c')
    tree.place(x=5, y=5)
    janela_sopas.mainloop()

# ---- PÁGINA INICIAL ----

janela_principal = Tk()
janela_principal.title('Recipe Manager')
janela_principal.geometry("1024x600")
janela_principal.configure(bg='#aff7ff')
original_frame = janela_principal
# Cria o Logo
imgLogo=PhotoImage(file="imagens\\logo.png", width=200, height=200)
l_logo=Label(janela_principal, image=imgLogo)
l_logo.place(x=10, y=10)
btnlogin=Button(janela_principal, text='Faça LOGIN!', fg='white', width=30, height=2, relief='ridge', command = login, bg="#499dc0")
btnlogin.place(x=220, y=450)
btnregisto=Button(janela_principal, text='Ainda não criou uma conta? Registe-se', fg='white', width=30, height=2, relief='ridge', command = registo, bg="#499dc0")
btnregisto.place(x=580, y=450)
janela_principal.mainloop()

