import pandas as pd

PLANILHA = pd.read_csv("NOME_ID_TOTAL.csv", encoding='latin-1', index_col="NOME")

#ORDENAR DADOS DA TABELA ATRAVÉS DA FUNÇÃO "sort_values"

# ORDENANDO DECRESCENTE
tabela_maior = PLANILHA.sort_values(['GASTO','ID'], ascending=False)
tabela_maior[['GASTO','ID']].head(10)
print(tabela_maior)

# ORDENANDO CRESCENTE
tabela_menor = PLANILHA.sort_values(['GASTO','ID'])
tabela_menor[['GASTO','ID']].head(10)
print(tabela_menor)

