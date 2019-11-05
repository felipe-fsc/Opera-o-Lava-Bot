import pandas as pd
import matplotlib.pyplot as plt

PLANILHA = pd.read_csv("NOME_ID_TOTAL.csv", encoding='latin-1', sep=';')

CONTROLE = 10

while CONTROLE != 0 :

    qtd_dp = str(input("\n \nINFORME A QUANTIDADE DE DEPUTADOS PARA ANALISE:  \n"))

    print("PARA TABELA COM OS " + qtd_dp + " DEPUTADOS MAIS GASTÕES   = 1 \nPARA TABELA COM OS " + qtd_dp + " DEPUTADOS MENOS GASTÕES  = 2 \n"
      "PARA GRAFICO COM OS " + qtd_dp + " DEPUTADOS MAIS GASTÕES  = 3 \nPARA GRAFICO COM OS " + qtd_dp + " DEPUTADOS MENOS GASTÕES = 4\n"
      "PARA SAIR = 0\n")

    CONTROLE = int(input("INFORME A ANALISE DESEJADA: "))

    qtd_dp = int(qtd_dp)

# ORDENAR DADOS DA TABELA ATRAVÉS DA FUNÇÃO "sort_values"

# ORDENANDO DECRESCENTE
    tabela_maior = PLANILHA.sort_values(['GASTO','ID'], ascending=False)
    tabela_maior[['GASTO','ID']]

# ORDENANDO CRESCENTE
    tabela_menor = PLANILHA.sort_values(['GASTO','ID'])
    tabela_menor[['GASTO','ID']]

    if CONTROLE == 1:

        print(tabela_maior.head(qtd_dp))

    elif CONTROLE == 2:

        print(tabela_menor.head(qtd_dp))

    elif CONTROLE == 3:
# PLOTANDO OS MAIS
        plt.rcParams['xtick.labelsize'] = 8
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.title('OS 10 DEPUTADOS QUE MAIS GASTARAM EM 09/2019')
        x = (tabela_maior['NOME'].head(qtd_dp))
        plt.ylabel('NOME DO DEPUTADO')
        y = (tabela_maior['GASTO'].head(qtd_dp))
        plt.xlabel('GASTOS EM R$')
        plt.barh(x, y, color="black")
        plt.show()

    elif CONTROLE == 4:
# PLOTANDO OS MENOS
        plt.rcParams['xtick.labelsize'] = 8
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.title('OS 10 DEPUTADOS QUE MAIS GASTARAM EM 09/2019')
        x = (tabela_menor['NOME'].head(qtd_dp))
        plt.ylabel('NOME DO DEPUTADO')
        y = (tabela_menor['GASTO'].head(qtd_dp))
        plt.xlabel('GASTOS EM R$')
        plt.barh(x, y, color="black")
        plt.show()
