import pandas as pd
import matplotlib.pyplot as plt

PLANILHA = pd.read_csv("NOME_ID_TOTAL.csv", encoding='latin-1')

# ORDENAR DADOS DA TABELA ATRAVÉS DA FUNÇÃO "sort_values"

# ORDENANDO DECRESCENTE
tabela_maior = PLANILHA.sort_values(['GASTO','ID'], ascending=False)
tabela_maior[['GASTO','ID']].head(10)
print(tabela_maior)

# ORDENANDO CRESCENTE
tabela_menor = PLANILHA.sort_values(['GASTO','ID'])
tabela_menor[['GASTO','ID']].head(10)
print(tabela_menor)


# PLOTANDO OS 10 MAIS
plt.rcParams['xtick.labelsize'] = 8
plt.title('OS 10 DEPUTADOS QUE MAIS GASTARAM EM 09/2019')
x = (tabela_maior['NOME'])
plt.xlabel('NOME DO DEPUTADO')
y = (tabela_maior['GASTO'])
plt.ylabel('GASTOS EM R$')
plt.bar(x, y, color="black")
plt.show()