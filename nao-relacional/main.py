import pymongo
import json

clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")

bd = clinica_vet['banco_de_dados']

## Criando as tabelas

pessoa = bd['pessoa']

tel_pessoa = bd['tel_pessoa']

especialidade = bd['especialidade']

consultorio = bd['consultorio']

veterinario = bd['veterinario']

tutor = bd['tutor']

especialidade_vet = bd['especialidade_vet']

animal = bd['animal']

consulta = bd['consulta']

receita = bd['receita']

internacao = bd['internacao']

registro_diario = bd['registro diario']

ficha_emergencia = bd['ficha emergencia']


## Um documento é um registro no banco de dados SQL

arquivo = open('./pessoas.json', 'r')
pessoas = json.load(arquivo)
arquivo.close()


pessoa.insert_many(pessoas)

for itens in pessoa.find():
    print(itens)