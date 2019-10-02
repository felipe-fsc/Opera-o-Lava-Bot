import requests
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
resp = requests.get(url).json()
# file = open('id_dep.txt', 'w')
# for d in resp['dados']:
#     a = (str(d['id']) + "\n")
#     file.writelines(a)

for d in resp['dados']:
    id_deputado = str(d['id'])
    url = 'https://dadosabertos.camara.leg.br/api/v2/deputados/' + id_deputado + '/despesas?ano=2019&mes=09&ordem=ASC&ordenarPor=ano'
    post = requests.get(url).json()
    print(post)

    file = open('despesas' + id_deputado + '.txt', 'w')

    for d in post ['dados']:
         b = (d['tipoDespesa'] + " = " + str(d['valorDocumento']) + "\n")
         file.writelines(b)
