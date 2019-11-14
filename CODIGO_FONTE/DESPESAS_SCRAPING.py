import requests

URL = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
RESP = requests.get(URL).json()

FILE_CSV = open('NOME_ID_TOTAL.csv', 'w')  # criando arquivo csv para escrever nome, ID, e total de gastos de cada deputado

CONTADOR = 2
GUIA_SOMA = 2
SOM = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
politicos = {}

while CONTADOR <= 9:

    for INFO in RESP['dados']: # for usado para buscar nome, id e as diversas despesas de cada deputado
        NOME_DEPUTADO = str(INFO['nome'])
        ID_DEPUTADO = str(INFO['id'])
        PARTIDO_DEPUTADO = str(INFO['siglaPartido'])
        UF_DEPUTADO = str(INFO['siglaUf'])
        URL = 'https://dadosabertos.camara.leg.br/api/v2/deputados/' + ID_DEPUTADO + '/despesas?ano=2019&mes=0' + str(GUIA_SOMA) + '&ordem=ASC&ordenarPor=ano'
        POST = requests.get(URL).json()
        print(POST)

    # criando arquivo txt para escrever as diversas despesas de cada deputado
    #     FILE_TXT = open('DESPESAS_' + NOME_DEPUTADO + '_' + ID_DEPUTADO + '_' + PARTIDO_DEPUTADO + '_' + UF_DEPUTADO + '.txt', 'w')

        SOMA = 0.0

        for INFO in POST['dados']:
#            DESPESAS_TXT = (INFO['tipoDespesa'] + " = " + str(INFO['valorDocumento']) + "   (" + str(INFO['dataDocumento']) + ")\n")
#            FILE_TXT.writelines(DESPESAS_TXT)      # escrevendo as despesas no arquivo txt

            VALOR_DOC = float(INFO['valorDocumento'])
            SOMA = SOMA + VALOR_DOC
            SOMA = float("%.2f" %SOMA)
            CONTADOR = int(CONTADOR)
#        FILE_TXT.writelines("TOTAL DE DESPESAS = " + SOM + '\n' "PARTIDO DEPUTADO = " + PARTIDO_DEPUTADO + '\n' "UF DEPUTADO = " + UF_DEPUTADO)    #escrevendo o total de despesas no arquivo txt

        if NOME_DEPUTADO in politicos:
            politicos[NOME_DEPUTADO].append(SOMA)
        else:
            politicos[NOME_DEPUTADO] = [NOME_DEPUTADO, ID_DEPUTADO, PARTIDO_DEPUTADO, UF_DEPUTADO, SOMA]

#        LINHA_CSV = (NOME_DEPUTADO + ';' + ID_DEPUTADO  + ';' + PARTIDO_DEPUTADO + ';' + UF_DEPUTADO + ';' + str(SOM[2]) + ';' + str(SOM[3]) + '\n')
#        FILE_CSV.writelines(LINHA_CSV)     # escrevendo nome, ID e total de despesas de cada deputado no arquivo csv
#    print(politicos)
    CONTADOR = CONTADOR + 1
    GUIA_SOMA = GUIA_SOMA + 1

    for politico in politicos:
        dados = (';'.join(map(str, politicos[politico])))
        print(dados)
    FILE_CSV.writelines(dados)

