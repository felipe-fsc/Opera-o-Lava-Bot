import pandas as pd
import matplotlib.pyplot as plt

PLANILHA = pd.read_csv("NOME_ID_TOTAL.csv", encoding='latin-1', sep=';')

print("PARA TABELA COM OS 10 DEPUTADOS MAIS GASTÕES   = 1 \nPARA TABELA COM OS 10 DEPUTADOS MENOS GASTÕES  = 2 \n"
      "PARA GRAFICO COM OS 10 DEPUTADOS MAIS GASTÕES  = 3 \nPARA GRAFICO COM OS 10 DEPUTADOS MENOS GASTÕES = 4\n"
      "PARA SAIR = 0\n")

CONTROLE = int(input("INFORME A ANALISE DESEJADA: "))

# ORDENAR DADOS DA TABELA ATRAVÉS DA FUNÇÃO "sort_values"

# ORDENANDO DECRESCENTE
tabela_maior = PLANILHA.sort_values(['GASTO','ID'], ascending=False)
tabela_maior[['GASTO','ID']]

# ORDENANDO CRESCENTE
tabela_menor = PLANILHA.sort_values(['GASTO','ID'])
tabela_menor[['GASTO','ID']]

if CONTROLE == 1:

    print(tabela_maior.head(10))

elif CONTROLE == 2:

    print(tabela_menor.head(10))

elif CONTROLE == 3:
# PLOTANDO OS MAIS
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.title('OS 10 DEPUTADOS QUE MAIS GASTARAM EM 09/2019')
    x = (tabela_maior['NOME'].head(10))
    plt.ylabel('NOME DO DEPUTADO')
    y = (tabela_maior['GASTO'].head(10))
    plt.xlabel('GASTOS EM R$')
    plt.barh(x, y, color="black")
    plt.show()

elif CONTROLE == 4:
# PLOTANDO OS MENOS
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.title('OS 10 DEPUTADOS QUE MAIS GASTARAM EM 09/2019')
    x = (tabela_menor['NOME'].head(10))
    plt.ylabel('NOME DO DEPUTADO')
    y = (tabela_menor['GASTO'].head(10))
    plt.xlabel('GASTOS EM R$')
    plt.barh(x, y, color="black")
    plt.show()
