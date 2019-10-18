import requests

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
resp = requests.get(url).json()

aux = 0.0
total = 0.0

file_csv = open('NOME_ID_TOTAL.csv', 'w')  # criando arquivo csv para escrever nome, ID, e total de gastos de cada deputado

for d in resp['dados']: # for usado para buscar nome, id e as diversas despesas de cada deputado
    nome_deputado = str(d['nome'])
    id_deputado = str(d['id'])
    url = 'https://dadosabertos.camara.leg.br/api/v2/deputados/' + id_deputado + '/despesas?ano=2019&mes=09&ordem=ASC&ordenarPor=ano'
    post = requests.get(url).json()
    print(post)

    file = open('DESPESAS_' + nome_deputado + '_' + id_deputado + '.txt', 'w') # criando arquivo txt para escrever as diversas despesas de cada deputado


    soma = 0.0

    for d in post['dados']:
        b = (d['tipoDespesa'] + " = " + str(d['valorDocumento']) + "\n")
        file.writelines(b)      # escrevendo as despesas no arquivo txt

        t = float(d['valorDocumento'])
        soma = soma + t
        som = str("%.2f" % soma)
    file.writelines("TOTAL DE DESPESAS = " + som)    #escrevendo o total de despesas no arquivo txt

    linha_csv = (nome_deputado + ',' + id_deputado  + ',' + som + '\n')
    file_csv.writelines(linha_csv)     # escrevendo nome, ID e total de despesas de cada deputado no arquivo csv


