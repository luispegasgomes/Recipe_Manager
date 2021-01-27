from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox 

#def favoritos():



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
                login_frame.withdraw()
                pag_admin()
                logado = True
        if not logado:
            messagebox.showwarning("Error", "Utilizador ou password incorretos.")
            janelalogin.destroy()
            login()

    janelalogin = Tk()
    janelalogin.geometry("900x600")
    janelalogin.configure(bg='#aff7ff')
    janelalogin.title("Iniciar Sessão")
    login_frame = janelalogin
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
        if txt_rpw.get() == txt_pw.get():
            try:
                with open('ficheiros\\utilizadores.txt', 'a', encoding="utf-8") as arquivoUtilizador_1:
                    arquivoUtilizador_1.write(txt_username.get() + '\n')
                with open('ficheiros\\senhas.txt', 'a', encoding="utf-8") as arquivoUtilizador:
                    arquivoUtilizador.write(txt_pw.get() + '\n')
                janelaregisto.destroy()
                login()
            except:
                print('Erro')
        else:
            messagebox.showerror("Error", "As passwords não coincidem!")    
    def escolhe_imagem():
    # file dialog, para selecionar ficheiro em disco
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select file",filetypes = (("gif files","*.gif"),("jpeg files","*.jpg"),("png files", "*.png"), ("all files","*.*")))
        global img 
        img = ImageTk.PhotoImage(file = filename)
    janelaregisto = Toplevel(janela_principal)
    janelaregisto.geometry("900x600")
    janelaregisto.title("Registo")
    janelaregisto.configure(bg='#aff7ff')
    original_frame.withdraw()
    lbl_username=Label(janelaregisto, text="Cria a tua conta !", font=("Helvetica",20))
    lbl_username.place(x=320, y=10)
    # Botão foto de perfil
    btn_foto=Button(janelaregisto, text="Adiciona a tua foto de perfil!", width=25, height=5, command = escolhe_imagem)
    btn_foto.place(x=600, y=180)

    # Label email
    lbl_email=Label(janelaregisto, text="Email :")
    lbl_email.place(x=350, y=70)

    # Entry email
    txt_email=Entry(janelaregisto, width=25)
    txt_email.place(x=350, y=100)


    # Label username
        
    lbl_username=Label(janelaregisto, text="Username :")
    lbl_username.place(x=350, y=130)

    # Entry username
    txt_username=Entry(janelaregisto, width=25)
    txt_username.place(x=350, y=160)

    # Label password
    lbl_pw=Label(janelaregisto, text="Password :")
    lbl_pw.place(x=350, y=190)

    # Entry password
    txt_pw=Entry(janelaregisto, width=25, show="*")
    txt_pw.place(x=350, y=220)

    # Label repeat password
    lbl_rpw=Label(janelaregisto, text="Confirmar password :")
    lbl_rpw.place(x=350, y=250)

    # Entry repeat password
    txt_rpw=Entry(janelaregisto, width=25, show="*")
    txt_rpw.place(x=350, y=280)

    # Registo button
    btnw=Button(janelaregisto, text="Regista-te", fg='white', width=30, height=2, relief='ridge', command = registar, bg="#499dc0")
    btnw.place(x=325, y=350)



    janelaregisto.mainloop()

def pag_admin():
    janela = Tk()
    janela.title('Recipe Manager')
    janela.geometry("1024x600")
    janela.configure(bg='#aff7ff')
    janela.resizable(0, 0)
    """imgLogo=PhotoImage(file="imagens\\logo12.gif", width=200, height=200)
    l_logo=Label(janela, image=imgLogo)
    l_logo.place(x=10, y=70)"""
    lbl_utilizador = Label(janela, text="Bem vindo(a), utilizador")
    lbl_utilizador.place(x=880, y=10)
    # Implementar menu
    barra_Menu = Menu(janela)

    # Constroi o menu
    simuladores_Menu = Menu(barra_Menu)
    barra_Menu.add_command(label="Home", command="noaction")
    barra_Menu.add_command(label="Todas as Receitas", command="noaction")
    barra_Menu.add_command(label="Favoritos", command=favoritos)
    barra_Menu.add_command(label="Contacte-nos", command="noaction")
    barra_Menu.add_command(label="About Us", command="noaction")

    # Botões
    btnadd = Button(janela, text='Gerir as minhas receitas', fg='white',width=35, height=3, relief='ridge', command=pag_user, bg="#499dc0")
    btnadd.place(x=380, y=1)

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

def pag_user():
    def adicionar():
        with open('ficheiros\\nome_receitas.txt', 'a', encoding="utf-8") as arquivonreceitas:
            arquivonreceitas.write(txt_nreceita.get() + '\n')
        with open('ficheiros\\categorias.txt', 'a', encoding="utf-8") as arquivoCategorias:
            arquivoCategorias.write(cb_categorias.get() + '\n')
        with open('ficheiros\\descricao_receita.txt', 'a', encoding="utf-8") as arquivoTexto:
            arquivoTexto.write(caixa_txt.get("1.0", "end") + '\n')
        janela_add.destroy()
        pag_user()
    def remover():
        lbox_gerir.delete(lbox_gerir.curselection())
    janela_add = Toplevel(janela_principal) 
    janela_add.geometry("1366x800")
    janela_add.title("Recipe Manager")
    # Painel Adicionar receita
    panel1 = LabelFrame(janela_add, text = 'Adicionar receita', width = 350, height = 500, bd = "3", relief = "sunken")
    panel1.place(x=10, y=10)
    # Painel Consultar
    panel2 = LabelFrame(janela_add, text = 'Consultar', width = 500, height = 500, bd = "3", relief = "sunken")
    panel2.place(x=800, y=10)
    # Painel Edições
    panel3 = LabelFrame(janela_add, text = 'Todas as minhas receitas', width = 300, height = 300, bd = "3", relief = "sunken")
    panel3.place(x=425, y=10)
    # Caixa de texto
    caixa_txt=Text(panel1, width=30, height=15)
    caixa_txt.place(x=20, y=15)
    # Listbox
    lbox_gerir = Listbox(panel3, width = 45, height = 16, bd = "3", relief = "sunken")
    lbox_gerir.place(x=10, y=10)

    # Entry nome da receita
    txt_nreceita=Entry(panel1, width=40)
    txt_nreceita.place(x=20, y=310)
    lbl_name=Label(panel1, text="Nome da receita :", fg="black", font=("Helvetica", 11))
    lbl_name.place(x=16, y=280)
        
    # ---Botões---
    # Botão Adicionar
    btn1=Button(panel1, text='Adicionar', fg='white', width=40, height=1, relief='ridge', command = adicionar, bg="#499dc0")
    btn1.place(x=20, y=420)
    # Botão Consultar
    btn_consultar=Button(janela_add, text='Consultar', fg='white', width=20, height=3, relief='ridge', command = "noaction", bg="#499dc0")
    btn_consultar.place(x=500, y=330)
    # Botão Editar
    btn_editar=Button(janela_add, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "noaction", bg="#499dc0")
    btn_editar.place(x=500, y=400)
    # Botão Remover
    btn_remove=Button(janela_add, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=500, y=470)


    # Componente treeview 
    tree = ttk.Treeview(panel2, columns = ("Receita", "Descrição"), show = "headings")
    tree.column("Receita", width = 100, anchor="c")
    tree.column("Descrição", width = 350, anchor="c")
    tree.heading("Receita", text="Receita")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=15, y=10)

    # Combobox para a categoria
    lbl_categorias=Label(panel1, text="Selecione a categoria a que pretende adicionar :", fg="black", font=("Helvetica", 11))
    lbl_categorias.place(x=16, y=340)
    lista = ['Sopas', 'Carne', 'Peixe', 'Massas', 'Breakfast', 'Vegetais', 'Snacks', 'Sobremesas', 'Bebidas', 'Outros']
    cb_categorias = Combobox(panel1, values = lista)
    cb_categorias.place(x=20, y=370)
    
    ficheiro = open("ficheiros\\nome_receitas.txt", "r", encoding="utf-8")
    lista_categorias = []
    for i in ficheiro:
        lista_categorias.append(i)
    for j in lista_categorias:
        lbox_gerir.insert(END, j)

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
# Define fundo da aplicação
janela_principal.configure(bg='#aff7ff')
original_frame = janela_principal
# Cria o Logo
imgLogo=PhotoImage(file="imagens\\logo.png", width=200, height=200)
l_logo=Label(janela_principal, image=imgLogo)
l_logo.place(x=400, y=70)
# Botões
btnlogin=Button(janela_principal, text='Iniciar sessão !', fg='white', width=30, height=2, relief='ridge', command = login, bg="#499dc0")
btnlogin.place(x=220, y=450)
btnregisto=Button(janela_principal, text='Ainda não criou uma conta? Registe-se', fg='white', width=30, height=2, relief='ridge', command = registo, bg="#499dc0")
btnregisto.place(x=580, y=450)
janela_principal.mainloop()

