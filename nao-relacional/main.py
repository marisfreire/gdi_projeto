import pymongo
import json


def read(nome_arquivo):
    arquivo = open(f'{nome_arquivo}', 'r')
    dados = json.load(arquivo)
    arquivo.close()
    return dados

def insert_document(documento, colecao):
    try:
        if(type(documento) == type(['2'])):
            colecao.insert_many(documento)
        else:
            colecao.insert_one(documento)
        print('Documento inserido com sucesso!')
    except:
        print('Falha em inserir documento')

def find_document(documento, colecao):
    return colecao.find(documento)

clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
##  Criando banco 

bd = clinica_vet['banco_de_dados']

## Criando as tabelas

pessoa = bd['pessoa']

tel_pessoa = bd['tel_pessoa']

especialidade = bd['especialidade']

consultorio = bd['consultorio']

veterinario = bd['veterinario']

tutor = bd['tutor']

animal = bd['animal']

receita = bd['receita']

internacao = bd['internacao']

registro_diario = bd['registro diario']

carteira_vacina = bd['carteira_vacina']

vacina = bd['vacina']
