# Cenário 2
# Um documento embutindo apenas um documento

def inserir_cenario2(bd):

    internacoes = [

        {
            '_id': 'i001',
            'animal': {
                'nome': 'Paçoca',
                'sexo': 'F',
                'nascimento': '24/10/2023'
            },
            'motivo': 'Cirurgia de castração',
            'momento_entrada': '16:11:02 09/08/2025'
        },
        {
            '_id': 'i002',
            'animal': {
                'nome': 'Paçoca',
                'sexo': 'F',
                'nascimento': '24/10/2023'
            },
            'motivo': 'Febre alta',
            'momento_entrada': '23:12:04 03/01/2024'
        },
        {
            '_id': 'i003',
            'animal': {
                'nome': 'Dudu',
                'sexo': 'M',
                'nascimento': '07/07/2023'
            },
            'motivo': 'Febre alta',
            'momento_entrada': '23:12:04 13/09/2024'
        }
    ]

    bd.internacao.insert_many(internacoes)
    print("Dados do cenário 2 inseridos \n")

def consulta_cenario2(bd):
    print("Iniciando a consulta: ")
    resultado = bd.internacao.find({"animal.nome": "Paçoca"}, {"momento_entrada":1, "_id":0})
    return resultado

def executar_cenario2(bd):

    inserir_cenario2(bd)
    resultado = consulta_cenario2(bd)

    for doc in resultado:
        print(f"Paçoca foi internada em {doc['momento_entrada']}")
    return