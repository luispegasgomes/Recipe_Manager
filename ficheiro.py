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
                    if line.strip("\n") != tudo_junto:
                        f_receitas.write(line)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado.")