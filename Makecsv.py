import pandas as pd

def msgConcluido(): # SOMENTE PERFUMARIA

    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
    print("\033[1;32m║              \033[1;33mArquivo Exportado com Sucesso!!              \033[1;32m║")
    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")


def export_csv(name, output):
    if output == 'cred_valida.csv':

        export_data = open('txt/'+name)
        export_data_lines = export_data.readlines()
        listaEmail = []
        listaSenha = []
        for i in export_data_lines:
            email, senha = i.split(";")
            listaEmail.append(email)
            listaSenha.append(senha)


        df = pd.DataFrame(columns=['Email','Senha']) # Criando DataFrame das Frases

        df['Email'] = listaEmail # Escrevendo na coluna Frase 
        df['Senha'] = listaSenha # Escrevendo na coluna Autor

        df.to_csv(output) # Exportando Frases para .CSV
        print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
        print("\033[1;32m║            \033[1;33mCredenciais válidas: cred_valida.csv           \033[1;32m║")
        print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
    elif output == 'cred_encontrada.csv':
        export_data = open('txt/'+name)
        export_data_lines = export_data.readlines()
        listaEmail = []
        listaSenha = []
        for i in export_data_lines:
            email, senha = i.split(";")
            listaEmail.append(email)
            listaSenha.append(senha)


        df = pd.DataFrame(columns=['Email','Senha']) # Criando DataFrame das Frases

        df['Email'] = listaEmail # Escrevendo na coluna Frase 
        df['Senha'] = listaSenha # Escrevendo na coluna Autor

        df.to_csv(output) # Exportando Frases para .CSV
        print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
        print("\033[1;32m║        \033[1;33mCredenciais encontradas: cred_encontrada.csv       \033[1;32m║")
        print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")