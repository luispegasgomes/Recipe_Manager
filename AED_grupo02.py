from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox 

global utilizador

def login():
    def loginBe():
        with open('ficheiros\\utilizadores.txt', 'r', encoding="utf-8") as arquivoUtilizador:
            utilizadores = arquivoUtilizador.readlines()
        with open('ficheiros\\senhas.txt', 'r', encoding="utf-8") as arquivoUtilizador:
            senhas = arquivoUtilizador.readlines()
        with open('ficheiros\\tipo_user.txt', 'r', encoding="utf-8") as arquivoUtilizador:
            tipo_utilizador = arquivoUtilizador.readlines()
        
        utilizadores = list(map(lambda x: x.replace('\n',''), utilizadores))
        senhas = list(map(lambda x: x.replace('\n',''), senhas))
        global utilizador
        utilizador = txt_username.get()
        senha = txt_pw1.get()

        logado = False

        for i in range(len(utilizadores)):
            if utilizador == utilizadores[i] and senha == senhas[i] and 'admin' != 'tipo_user[i]':
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
    imgLogo=ImageTk.PhotoImage(master=janelalogin, file="imagens\\logo.png")
    janelalogin.imgLogo = imgLogo
    l_logo=Label(janelalogin, image = imgLogo, width=200, height=200)
    l_logo.place(x=20, y=20)
    original_frame.withdraw()
        
    # Label Faça o seu login
    lbl_username=Label(janelalogin, text="Iniciar sessão", font=("Helvetica",20))
    lbl_username.place(x=390, y=10)

    # Label username
    lbl_username=Label(janelalogin, text="Username :")
    lbl_username.place(x=400, y=70)

    # Entry username
    nome = StringVar()
    txt_username=Entry(janelalogin, width=25, textvariable = nome )
    txt_username.place(x=400, y=100)

    # Label password
            
    lbl_pw=Label(janelalogin, text="Password :")
    lbl_pw.place(x=400, y=140)

    # Entry password
    txt_pw1=Entry(janelalogin, width=25, show="*")
    txt_pw1.place(x=400, y=170)

    # Login button
    btn=Button(janelalogin, text="Iniciar Sessão", command = loginBe, width=40, height=2, bg="#499dc0", fg='white')
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
                with open('ficheiros\\tipo_user.txt', 'a', encoding="utf-8") as arquivoType:
                    arquivoType.write('user' + '\n')
                janelaregisto.destroy()
                login()
            except:
                print('Erro')
        else:
            messagebox.showerror("Error", "As passwords não coincidem!")    
    
    # File dialog, para selecionar ficheiro em disco
    def escolhe_imagem():
        global img_perfil
        global filename
        global image_perfil_id
        # file dialog, para selecionar ficheiro em disco
        filename = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files", "*.png"), ("all files","*.*")))
        img_perfil = ImageTk.PhotoImage(file = filename)

    janelaregisto = Toplevel(janela_principal)
    janelaregisto.geometry("900x600")
    janelaregisto.title("Registo")
    janelaregisto.configure(bg='#aff7ff')
    original_frame.withdraw()
    lbl_username=Label(janelaregisto, text="Cria a tua conta !", font=("Helvetica",20))
    lbl_username.place(x=320, y=10)
    imgLogo=ImageTk.PhotoImage(master=janelaregisto, file="imagens\\logo.png")
    janelaregisto.imgLogo = imgLogo
    l_logo=Label(janelaregisto, image = imgLogo, width=200, height=200)
    l_logo.place(x=20, y=20)
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
    #---IMAGEM LOGO DA APLICAÇÃO---
    imgLogo=ImageTk.PhotoImage(master=janela, file="imagens\\logo.png")
    janela.imgLogo = imgLogo
    l_logo=Label(janela, image = imgLogo, width=200, height=200)
    l_logo.place(x=20, y=20)
    #---IMAGEM PERFIL DE UTILIZADOR---
    imgPerfil=ImageTk.PhotoImage(master=janela, file="imagens\\logo.png")
    janela.imgPerfil = imgPerfil
    l_perfil=Label(janela, image = imgPerfil, width=200, height=200)
    l_perfil.place(x=30, y=500)
    global utilizador
    global filename
    global image_perfil_id
    #canvas_perfil = Canvas(pag_admin, width = 110, height = 120, bd = 4, relief = "sunken")
    #canvas_perfil.place(x=220, y=20)
    #img_perfil = ImageTk.PhotoImage(file = filename)
    #image_perfil_id = canvas_perfil.create_image(0, 0, anchor='nw', image=img_perfil)


    lbl_utilizador = Label(janela, text = "Seja bem-vindo, " + utilizador, font=("Helvetica", 11))
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
    btnadd = Button(janela, text='Gerir as minhas receitas', fg='white',width=35, height=3, relief='ridge', command=pag_user, bg="#499dc0")
    btnadd.place(x=380, y=1)

    btn2 = Button(janela, text='Sopas', fg='black', width=7,height=3, relief='ridge', command=sopas)
    btn2.place(x=280, y=80)
    btn3 = Button(janela, text='Carne', fg='black', width=7,height=3, relief='ridge', command=carne)
    btn3.place(x=380, y=80)
    btn11 = Button(janela, text='Peixe', fg='black', width=7,height=3, relief='ridge', command=peixe)
    btn11.place(x=480, y=80)
    btn5 = Button(janela, text='Massas', fg='black', width=7,height=3, relief='ridge', command=massas)
    btn5.place(x=580, y=80)
    btn6 = Button(janela, text='Breakfast', fg='black', width=7,height=3, relief='ridge', command=breakfast)
    btn6.place(x=680, y=80)


    btn13 = Button(janela, text='Vegetais', fg='black', width=7,height=3, relief='ridge', command=vegetais)
    btn13.place(x=280, y=160)
    btn14 = Button(janela, text='Snacks', fg='black', width=7,height=3, relief='ridge', command=snacks)
    btn14.place(x=380, y=160)

    btn18 = Button(janela, text='Sobremesas', fg='black', width=7,height=3, relief='ridge', command=sobremesas)
    btn18.place(x=480, y=160)
    btn19 = Button(janela, text='Bebidas', fg='black', width=7,height=3, relief='ridge', command=bebidas)
    btn19.place(x=580, y=160)

    btn26 = Button(janela, text='Outros', fg='black', width=7,height=3, relief='ridge', command=outros)
    btn26.place(x=680, y=160)

    # Constroi menu Sair, com comando quit
    barra_Menu.add_command(label="Sair", command=janela.quit)
    janela.configure(menu=barra_Menu)

    janela.mainloop()

def pag_user():
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_leitura.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            nome2 = str(valores[1])
            nome3 = str(valores[2])
            tudo_junto = nome1 + ";" + nome2 + ";" + nome3
            print(tudo_junto)
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    def adicionar():
        f_dados = open("ficheiros\\dados_ttk.txt", "a", encoding="utf-8")
        nome_receita = txt_nreceita.get()
        categoria = cb_categorias.get()
        descricao = caixa_txt.get("1.0", "end")
        linha = nome_receita  + ";" + categoria + ";" + descricao
        f_dados.write(linha)
        f_dados.close()
        janela_add.destroy()
        pag_user()
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def verificar_admin():
        admin_user = open('ficheiros\\tipo_user.txt', 'r', encoding='utf-8')
        for linha in admin_user:
            campos = linha.split(";")
        if (campos[0] == campos[0]):
            janela_gerir_categorias = Tk()
            janela_gerir_categorias.title('Recipe Manager')
            janela_gerir_categorias.geometry("400x400")
            # Listbox para ler todas as categorias
            lbox_gerir = Listbox(janela_gerir_categorias, width = 30, height = 10, bd = "3", relief = "sunken")
            lbox_gerir.place(x=10, y=10)
            # Preencher listbox categorias
            ficheiro_categorias = open("ficheiros\\categorias.txt", "r", encoding="utf-8")
            lista_categorias = []
            for i in ficheiro_categorias:
                lista_categorias.append(i)
            for j in lista_categorias:
                lbox_gerir.insert(END, j)

            def adicionar_categoria():
                with open('ficheiros\\categorias.txt', 'a', encoding="utf-8") as arquivoCategorias_1:
                    arquivoCategorias_1.write(txt_ncategoria.get() + '\n')
            def remover_categoria():
                with open("ficheiros\\categorias.txt", "r") as f_categorias:
                    lines = f_categorias.readlines()
                with open("ficheiros\\categorias.txt", "w") as f_categorias:
                    for line in lines:
                        if line.strip("\n") != txt_ncategoria.get():
                            f_categorias.write(line)
            # Inserir nome da categoria
            txt_ncategoria=Entry(janela_gerir_categorias, width=30)
            txt_ncategoria.place(x=20, y=220)
            lbl_name=Label(janela_gerir_categorias, text="Nome da categoria :", fg="black", font=("Helvetica", 11))
            lbl_name.place(x=16, y=180)
                    
            # Botão Adicionar
            btn_adicionar=Button(janela_gerir_categorias, text='Adicionar', fg='white', width=20, height=3, relief='ridge', command = adicionar_categoria, bg="#499dc0")
            btn_adicionar.place(x=50, y=300)    

            # Botão Remover
            btn_remove=Button(janela_gerir_categorias, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover_categoria, bg="#499dc0")
            btn_remove.place(x=230, y=300)
            janela_gerir_categorias.mainloop()
        else:
            messagebox.showwarning("Error", "O utilizador não tem permissão para executar estas funções!")
    janela_add = Toplevel(janela_principal) 
    janela_add.geometry("1366x800")
    janela_add.title("Recipe Manager")

    # Painel Adicionar receita
    panel1 = LabelFrame(janela_add, text = 'Adicionar receita', width = 350, height = 500, bd = "3", relief = "sunken")
    panel1.place(x=10, y=10)

    # Painel Consultar
    panel2 = LabelFrame(janela_add, text = 'Consultar', width = 800, height = 500, bd = "3", relief = "sunken")
    panel2.place(x=500, y=10)
    
    # Caixa de texto para inserção de dados
    caixa_txt=Text(panel1, width=30, height=15)
    caixa_txt.place(x=20, y=15)

    # Entry nome da receita
    txt_nreceita=Entry(panel1, width=40)
    txt_nreceita.place(x=20, y=310)
    lbl_name=Label(panel1, text="Nome da receita :", fg="black", font=("Helvetica", 11))
    lbl_name.place(x=16, y=280)
        
    # ---Botões---
    # Botão Adicionar
    btn1=Button(panel1, text='Adicionar', fg='white', width=40, height=1, relief='ridge', command = adicionar, bg="#499dc0")
    btn1.place(x=20, y=420)

    # Botão consultar receita
    btn_consultar_receita=Button(janela_add, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=1100, y=50)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_add, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=1100, y=140)

    # Botão Editar
    btn_editar=Button(janela_add, text='Editar', fg='white', width=20, height=3, relief='ridge', command = verificar_admin, bg="#499dc0")
    btn_editar.place(x=1100, y=230)

    # Botão Remover
    btn_remove=Button(janela_add, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=1100, y=320)

    # Componente treeview 
    tree = ttk.Treeview(panel2, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=15, y=10)
    
    # Inserir os dados na treeview 
    ficheiro_tree = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
    lista = ficheiro_tree.readlines()
    ficheiro_tree.close()

    # Caixa de texto para a leitura de dados
    caixa_txt_leitura=Text(panel2, width=50, height=12)
    caixa_txt_leitura.place(x=40, y=270)


    # ---COMBOBOX COM AS CATEGORIAS---

    with open('ficheiros\\categorias.txt', 'r', encoding="utf-8") as arquivoCategorias:
        categoria = arquivoCategorias.readlines()
    categoria = list(map(lambda x: x.replace('\n',''), categoria))
    lista = []
    for linha in categoria:
        lista.append(linha)
    # Combobox para a categoria
    lbl_categorias=Label(panel1, text="Selecione a categoria a que pretende adicionar :", fg="black", font=("Helvetica", 11))
    lbl_categorias.place(x=16, y=340)
    cb_categorias = Combobox(panel1, values = lista)
    cb_categorias.place(x=20, y=370)
    janela_add.mainloop()

def sopas():
    janela_sopas = Tk()
    janela_sopas.title('Gestão de Sopas')
    janela_sopas.geometry("800x600")
    janela_sopas.configure(bg='#aff7ff')
    janela_sopas.resizable(0, 0)
    # Container Canvas
    ctn_canvas = Canvas(janela_sopas, width = 200, height = 200, bd = 0, relief = "sunken")
    ctn_canvas.place(x=20, y=20)
    # Cria a imagem
    """img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
    ctn_canvas.create_image(100,100, image = img_sopas)"""
    # Caixa de texto para leitura de dados
    caixa_txt_sopas=Text(janela_sopas, width=40, height=12)
    caixa_txt_sopas.place(x=270, y=20)
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_sopas.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if (campos[1] == 'Sopas'):
                tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    # ---Botões---
    # Botão consultar receita
    btn_consultar_receita=Button(janela_sopas, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=640, y=20)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_sopas, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=640, y=100)

    # Botão Editar
    btn_editar=Button(janela_sopas, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "verificar_admin", bg="#499dc0")
    btn_editar.place(x=640, y=180)

    # Botão Remover
    btn_remove=Button(janela_sopas, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=640, y=260)

    # Componente treeview 
    tree = ttk.Treeview(janela_sopas, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=170, y=300)
    janela_sopas.mainloop()

def carne():

    janela_carne = Tk()
    janela_carne.title('Gestão de Carne')
    janela_carne.geometry("800x600")
    janela_carne.configure(bg='#aff7ff')
    janela_carne.resizable(0, 0)
    # Container Canvas
    ctn_canvas = Canvas(janela_carne, width = 200, height = 200, bd = 0, relief = "sunken")
    ctn_canvas.place(x=20, y=20)
    # Cria a imagem
    """img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
    ctn_canvas.create_image(100,100, image = img_sopas)"""
    # Caixa de texto para leitura de dados
    caixa_txt_carne=Text(janela_carne, width=40, height=12)
    caixa_txt_carne.place(x=270, y=20)
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_carne.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if (campos[1] == 'Carne'):
                tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    # ---Botões---
    # Botão consultar receita
    btn_consultar_receita=Button(janela_carne, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=640, y=20)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_carne, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=640, y=100)

    # Botão Editar
    btn_editar=Button(janela_carne, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "verificar_admin", bg="#499dc0")
    btn_editar.place(x=640, y=180)

    # Botão Remover
    btn_remove=Button(janela_carne, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=640, y=260)

    # Componente treeview 
    tree = ttk.Treeview(janela_carne, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=170, y=300)
    janela_carne.mainloop()

def peixe():    
    janela_peixe = Tk()
    janela_peixe.title('Gestão de Peixe')
    janela_peixe.geometry("800x600")
    janela_peixe.configure(bg='#aff7ff')
    janela_peixe.resizable(0, 0)
    # Container Canvas
    ctn_canvas = Canvas(janela_peixe, width = 200, height = 200, bd = 0, relief = "sunken")
    ctn_canvas.place(x=20, y=20)
    # Cria a imagem
    """img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
    ctn_canvas.create_image(100,100, image = img_sopas)"""
    # Caixa de texto para leitura de dados
    caixa_txt_carne=Text(janela_peixe, width=40, height=12)
    caixa_txt_carne.place(x=270, y=20)
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_carne.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if (campos[1] == 'Peixe'):
                tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    # ---Botões---
    # Botão consultar receita
    btn_consultar_receita=Button(janela_peixe, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=640, y=20)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_peixe, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=640, y=100)

    # Botão Editar
    btn_editar=Button(janela_peixe, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "verificar_admin", bg="#499dc0")
    btn_editar.place(x=640, y=180)

    # Botão Remover
    btn_remove=Button(janela_peixe, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=640, y=260)

    # Componente treeview 
    tree = ttk.Treeview(janela_peixe, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=170, y=300)
    janela_peixe.mainloop()

def breakfast():    
    janela_breakfast = Tk()
    janela_breakfast.title('Gestão de Carne')
    janela_breakfast.geometry("800x600")
    janela_breakfast.configure(bg='#aff7ff')
    janela_breakfast.resizable(0, 0)
    # Container Canvas
    ctn_canvas = Canvas(janela_breakfast, width = 200, height = 200, bd = 0, relief = "sunken")
    ctn_canvas.place(x=20, y=20)
    # Cria a imagem
    """img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
    ctn_canvas.create_image(100,100, image = img_sopas)"""
    # Caixa de texto para leitura de dados
    caixa_txt_carne=Text(janela_breakfast, width=40, height=12)
    caixa_txt_carne.place(x=270, y=20)
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_carne.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if (campos[1] == 'Breakfast'):
                tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    # ---Botões---
    # Botão consultar receita
    btn_consultar_receita=Button(janela_breakfast, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=640, y=20)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_breakfast, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=640, y=100)

    # Botão Editar
    btn_editar=Button(janela_breakfast, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "verificar_admin", bg="#499dc0")
    btn_editar.place(x=640, y=180)

    # Botão Remover
    btn_remove=Button(janela_breakfast, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=640, y=260)

    # Componente treeview 
    tree = ttk.Treeview(janela_breakfast, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=170, y=300)
    janela_breakfast.mainloop()

def massas():
    janela_massas = Tk()
    janela_massas.title('Gestão de Massas')
    janela_massas.geometry("800x600")
    janela_massas.configure(bg='#aff7ff')
    janela_massas.resizable(0, 0)
    # Container Canvas
    ctn_canvas = Canvas(janela_massas, width = 200, height = 200, bd = 0, relief = "sunken")
    ctn_canvas.place(x=20, y=20)
    # Cria a imagem
    """img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
    ctn_canvas.create_image(100,100, image = img_sopas)"""
    # Caixa de texto para leitura de dados
    caixa_txt_carne=Text(janela_massas, width=40, height=12)
    caixa_txt_carne.place(x=270, y=20)
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_carne.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if (campos[1] == 'Massas'):
                tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    # ---Botões---
    # Botão consultar receita
    btn_consultar_receita=Button(janela_massas, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=640, y=20)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_massas, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=640, y=100)

    # Botão Editar
    btn_editar=Button(janela_massas, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "verificar_admin", bg="#499dc0")
    btn_editar.place(x=640, y=180)

    # Botão Remover
    btn_remove=Button(janela_massas, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=640, y=260)

    # Componente treeview 
    tree = ttk.Treeview(janela_massas, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=170, y=300)
    janela_massas.mainloop()    

def vegetais():
    janela_vegetais = Tk()
    janela_vegetais.title('Gestão de Vegetais')
    janela_vegetais.geometry("800x600")
    janela_vegetais.configure(bg='#aff7ff')
    janela_vegetais.resizable(0, 0)
    # Container Canvas
    ctn_canvas = Canvas(janela_vegetais, width = 200, height = 200, bd = 0, relief = "sunken")
    ctn_canvas.place(x=20, y=20)
    # Cria a imagem
    """img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
    ctn_canvas.create_image(100,100, image = img_sopas)"""
    # Caixa de texto para leitura de dados
    caixa_txt_carne=Text(janela_vegetais, width=40, height=12)
    caixa_txt_carne.place(x=270, y=20)
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_carne.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if (campos[1] == 'Vegetais'):
                tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    # ---Botões---
    # Botão consultar receita
    btn_consultar_receita=Button(janela_vegetais, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=640, y=20)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_vegetais, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=640, y=100)

    # Botão Editar
    btn_editar=Button(janela_vegetais, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "verificar_admin", bg="#499dc0")
    btn_editar.place(x=640, y=180)

    # Botão Remover
    btn_remove=Button(janela_vegetais, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=640, y=260)

    # Componente treeview 
    tree = ttk.Treeview(janela_vegetais, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=170, y=300)
    janela_vegetais.mainloop()    

def snacks():
    janela_snacks = Tk()
    janela_snacks.title('Gestão de Snacks')
    janela_snacks.geometry("800x600")
    janela_snacks.configure(bg='#aff7ff')
    janela_snacks.resizable(0, 0)
    # Container Canvas
    ctn_canvas = Canvas(janela_snacks, width = 200, height = 200, bd = 0, relief = "sunken")
    ctn_canvas.place(x=20, y=20)
    # Cria a imagem
    """img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
    ctn_canvas.create_image(100,100, image = img_sopas)"""
    # Caixa de texto para leitura de dados
    caixa_txt_carne=Text(janela_snacks, width=40, height=12)
    caixa_txt_carne.place(x=270, y=20)
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_carne.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if (campos[1] == 'Snacks'):
                tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    # ---Botões---
    # Botão consultar receita
    btn_consultar_receita=Button(janela_snacks, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=640, y=20)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_snacks, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=640, y=100)

    # Botão Editar
    btn_editar=Button(janela_snacks, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "verificar_admin", bg="#499dc0")
    btn_editar.place(x=640, y=180)

    # Botão Remover
    btn_remove=Button(janela_snacks, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=640, y=260)

    # Componente treeview 
    tree = ttk.Treeview(janela_snacks, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=170, y=300)
    janela_snacks.mainloop()    

def sobremesas():
    janela_sobremesas = Tk()
    janela_sobremesas.title('Gestão de Sobremesas')
    janela_sobremesas.geometry("800x600")
    janela_sobremesas.configure(bg='#aff7ff')
    janela_sobremesas.resizable(0, 0)
    # Container Canvas
    ctn_canvas = Canvas(janela_sobremesas, width = 200, height = 200, bd = 0, relief = "sunken")
    ctn_canvas.place(x=20, y=20)
    # Cria a imagem
    """img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
    ctn_canvas.create_image(100,100, image = img_sopas)"""
    # Caixa de texto para leitura de dados
    caixa_txt_carne=Text(janela_sobremesas, width=40, height=12)
    caixa_txt_carne.place(x=270, y=20)
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_carne.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if (campos[1] == 'Sobremesas'):
                tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    # ---Botões---
    # Botão consultar receita
    btn_consultar_receita=Button(janela_sobremesas, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=640, y=20)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_sobremesas, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=640, y=100)

    # Botão Editar
    btn_editar=Button(janela_sobremesas, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "verificar_admin", bg="#499dc0")
    btn_editar.place(x=640, y=180)

    # Botão Remover
    btn_remove=Button(janela_sobremesas, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=640, y=260)

    # Componente treeview 
    tree = ttk.Treeview(janela_sobremesas, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=170, y=300)
    janela_sobremesas.mainloop()    

def bebidas():
    janela_bebidas = Tk()
    janela_bebidas.title('Gestão de Bebidas')
    janela_bebidas.geometry("800x600")
    janela_bebidas.configure(bg='#aff7ff')
    janela_bebidas.resizable(0, 0)
    # Container Canvas
    ctn_canvas = Canvas(janela_bebidas, width = 200, height = 200, bd = 0, relief = "sunken")
    ctn_canvas.place(x=20, y=20)
    # Cria a imagem
    """img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
    ctn_canvas.create_image(100,100, image = img_sopas)"""
    # Caixa de texto para leitura de dados
    caixa_txt_carne=Text(janela_bebidas, width=40, height=12)
    caixa_txt_carne.place(x=270, y=20)
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_carne.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if (campos[1] == 'Bebidas'):
                tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    # ---Botões---
    # Botão consultar receita
    btn_consultar_receita=Button(janela_bebidas, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=640, y=20)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_bebidas, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=640, y=100)

    # Botão Editar
    btn_editar=Button(janela_bebidas, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "verificar_admin", bg="#499dc0")
    btn_editar.place(x=640, y=180)

    # Botão Remover
    btn_remove=Button(janela_bebidas, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=640, y=260)

    # Componente treeview 
    tree = ttk.Treeview(janela_bebidas, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=170, y=300)
    janela_bebidas.mainloop()    

def outros():
    janela_outros = Tk()
    janela_outros.title('Gestão de Outros')
    janela_outros.geometry("800x600")
    janela_outros.configure(bg='#aff7ff')
    janela_outros.resizable(0, 0)
    # Container Canvas
    ctn_canvas = Canvas(janela_outros, width = 200, height = 200, bd = 0, relief = "sunken")
    ctn_canvas.place(x=20, y=20)
    # Cria a imagem
    """img_sopas = ImageTk.PhotoImage(Image.open("imagens\\Soup.png"))
    ctn_canvas.create_image(100,100, image = img_sopas)"""
    # Caixa de texto para leitura de dados
    caixa_txt_carne=Text(janela_outros, width=40, height=12)
    caixa_txt_carne.place(x=270, y=20)
    def consultar():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            descricao_receita = str(valores[2])
            caixa_txt_carne.insert("end", descricao_receita)
            print(descricao_receita)
            
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")
    def ver_receitas():
        f = open("ficheiros\\dados_ttk.txt", "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if (campos[1] == 'Outros'):
                tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
    def remover():
        try:
            itemSelecionado = tree.selection()[0]
            valores = tree.item(itemSelecionado,"values")
            print(valores)
            nome1 = str(valores[0])
            tree.delete(itemSelecionado)
            with open("ficheiros\\dados_ttk.txt", "r") as f_receitas:
                lines = f_receitas.readlines()
            with open("ficheiros\\dados_ttk.txt", "w") as f_receitas:
                for line in lines:
                    campos = line.split(";")
                    if campos[0] != nome1:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")  

    # ---Botões---
    # Botão consultar receita
    btn_consultar_receita=Button(janela_outros, text='Consultar receita', fg='white', width=20, height=3, relief='ridge', command = consultar, bg="#499dc0")
    btn_consultar_receita.place(x=640, y=20)

    # Botão ver receitas
    btn_ver_receitas=Button(janela_outros, text='Ver Receitas', fg='white', width=20, height=3, relief='ridge', command = ver_receitas, bg="#499dc0")
    btn_ver_receitas.place(x=640, y=100)

    # Botão Editar
    btn_editar=Button(janela_outros, text='Editar', fg='white', width=20, height=3, relief='ridge', command = "verificar_admin", bg="#499dc0")
    btn_editar.place(x=640, y=180)

    # Botão Remover
    btn_remove=Button(janela_outros, text='Remover', fg='white', width=20, height=3, relief='ridge', command = remover, bg="#499dc0")
    btn_remove.place(x=640, y=260)

    # Componente treeview 
    tree = ttk.Treeview(janela_outros, columns = ("Nome da Receita", "Categoria", "Descrição"), show = "headings")
    tree.column("Nome da Receita", width = 250, anchor="c")
    tree.column("Categoria", width = 100, anchor="c")
    tree.column("Descrição", width = 100, anchor="c")
    tree.heading("Nome da Receita", text="Nome da Receita")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Descrição", text="Descrição")
    tree.place(x=170, y=300)
    janela_outros.mainloop() 

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

