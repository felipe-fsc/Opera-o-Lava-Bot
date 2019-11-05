import requests

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
resp = requests.get(url).json()

file_csv = open('NOME_ID_TOTAL.csv', 'w')  # criando arquivo csv para escrever nome, ID, e total de gastos de cada deputado

for d in resp['dados']: # for usado para buscar nome, id e as diversas despesas de cada deputado
    nome_deputado = str(d['nome'])
    id_deputado = str(d['id'])
    partido_deputado = str(d['siglaPartido'])
    UF_deputado = str(d['siglaUf'])
    url = 'https://dadosabertos.camara.leg.br/api/v2/deputados/' + id_deputado + '/despesas?ano=2019&mes=09&ordem=ASC&ordenarPor=ano'
    post = requests.get(url).json()
    print(post)

# criando arquivo txt para escrever as diversas despesas de cada deputado
    file = open('DESPESAS_' + nome_deputado + '_' + id_deputado + '_' + partido_deputado + '_' + UF_deputado + '.txt', 'w')


    soma = 0.0

    for d in post['dados']:
        b = (d['tipoDespesa'] + " = " + str(d['valorDocumento']) + "   (" + str(d['dataDocumento']) + ")\n")
        file.writelines(b)      # escrevendo as despesas no arquivo txt

        t = float(d['valorDocumento'])
        soma = soma + t
        som = str("%.2f" % soma)
    file.writelines("TOTAL DE DESPESAS = " + som + '\n' "PARTIDO DEPUTADO = " + partido_deputado + '\n' "UF DEPUTADO = " + UF_deputado)    #escrevendo o total de despesas no arquivo txt
    linha_csv = (nome_deputado + ';' + id_deputado  + ';' + som + ';' + partido_deputado + ';' + UF_deputado + '\n')
    file_csv.writelines(linha_csv)     # escrevendo nome, ID e total de despesas de cada deputado no arquivo csv


