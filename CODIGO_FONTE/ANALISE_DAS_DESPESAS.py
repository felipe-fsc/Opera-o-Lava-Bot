import os
import pandas as pd
import matplotlib.pyplot as plt

# ABRINDO O ARQUIVO CSV ATRAVES DA BIBLIOTECA PANDAS
PLANILHA = pd.read_csv("NOME_ID_TOTAL.csv", encoding='latin-1', sep=';')

CONTROLE = 10

while CONTROLE != 0 :

# MENU DE INTERAÇÃO COM O USUARIO
    qtd_dp = str(input("\n \nINFORME A QUANTIDADE DE DEPUTADOS PARA ANALISE:  \n"))
    MES = str(input('\nINFORME O MES DE REFERENCIA: \n'))
    print("PARA TABELA COM OS " + qtd_dp + " DEPUTADOS MAIS GASTÕES   = 1 \nPARA TABELA COM OS " + qtd_dp + " DEPUTADOS MENOS GASTÕES  = 2 \n"
      "PARA GRAFICO COM OS " + qtd_dp + " DEPUTADOS MAIS GASTÕES  = 3 \nPARA GRAFICO COM OS " + qtd_dp + " DEPUTADOS MENOS GASTÕES = 4\n"
      "PARA VISUALIZAÇÃO INDIVIDUAL = 5\nPARA GERAR DADOS POR UF = 6\nPARA GERAR DADOS POR PARTIDO = 7\nPARA SAIR = 0\n \n")

    CONTROLE = int(input("INFORME A ANALISE DESEJADA: "))

    qtd_dp = int(qtd_dp)

# ORDENANDO OS DADOS DA TABELA ATRAVÉS DA FUNÇÃO "sort_values"
# ORDENANDO OS GASTOS EM ORDEM DECRESCENTE A PARTIR DO MES SELECIONADO
    tabela_maior = PLANILHA.sort_values(['GASTO' + MES], ascending=False)

# ORDENANDO OS GASTOS EM ORDEM CRESCENTE A PARTIR DO MES SELECIONADO
    tabela_menor = PLANILHA.sort_values(['GASTO' + MES])

    if CONTROLE == 1:

        print(tabela_maior[['NOME','ID', 'PARTIDO','UF','GASTO' + MES ]].head(qtd_dp))

    elif CONTROLE == 2:

        print(tabela_menor[['NOME','ID', 'PARTIDO','UF','GASTO' + MES ]].head(qtd_dp))

    elif CONTROLE == 3:
# PLOTANDO EM UM GRAFICO DE BARRAS A QUANTIDADE SELECIONADA DOS DEPUTADOS QUE MAIS GASTARAM
        plt.rcParams['xtick.labelsize'] = 8
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.title('OS 10 DEPUTADOS QUE MAIS GASTARAM EM 0' + MES + '/2019')
        x = (tabela_maior['NOME'].head(qtd_dp))
        plt.ylabel('NOME DO DEPUTADO')
        y = (tabela_maior['GASTO' + MES].head(qtd_dp))
        plt.xlabel('GASTOS EM R$')
        plt.barh(x, y, color="black")
        plt.show()

    elif CONTROLE == 4:
# PLOTANDO EM UM GRAFICO DE BARRAS A QUANTIDADE SELECIONADA DOS DEPUTADOS QUE MENOS GASTARAM
        plt.rcParams['xtick.labelsize'] = 8
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.title('OS 10 DEPUTADOS QUE MAIS GASTARAM EM 0' + MES + '/2019')
        x = (tabela_menor['NOME'].head(qtd_dp))
        plt.ylabel('NOME DO DEPUTADO')
        y = (tabela_menor['GASTO' + MES].head(qtd_dp))
        plt.xlabel('GASTOS EM R$')
        plt.barh(x, y, color="black")
        plt.show()

    elif CONTROLE == 5:
# EXIBINDO OS GASTOS DETALHADOS INDIVIDUALMENTE
        NOME_DEPUTADO = str(input('INFORME O NOME DO DEPUTADO: \n'))
        dep_id = PLANILHA.query("NOME == '{}'".format(NOME_DEPUTADO)).ID

        if len(dep_id.values) > 0:
            A = str(dep_id.values[0])

            os.startfile('C:/Users/n4hta/Desktop/webbot/operacao-lava-bot/CODIGO_FONTE/GASTOS_INDIVIDUAIS/MES_' + MES + '/GASTOS_' + NOME_DEPUTADO +'_'+ A + '.txt')

    elif CONTROLE == 6:
# EXIBINDO OS GASTOS SEPARADOS POR UF
        UF = str(input('INFORME A UF: \n'))
        dep_uf = PLANILHA.query("UF == '{}'".format(UF))
        dep_uf.to_csv(r'C:/Users/n4hta/Desktop/webbot/operacao-lava-bot/CODIGO_FONTE/GASTOS_UF/' + UF + '.csv', sep = ';')

    elif CONTROLE == 7:
# EXIBINDO OS GASTOS SEPARADOS POR PARTIDO
        PARTIDO = str(input('INFORME O NOME DO PARTIDO: \n'))
        dep_uf = PLANILHA.query("PARTIDO == '{}'".format(PARTIDO))
        dep_uf.to_csv(r'C:/Users/n4hta/Desktop/webbot/operacao-lava-bot/CODIGO_FONTE/GASTOS_PARTIDO/' + PARTIDO + '.csv', sep = ';')


CONTROLE = 0
