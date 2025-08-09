# Cenário 1
# Documento que referencia apenas um documento

def inserir_cenario1(bd):
    
    animal_c1 = {
        '_id': 'a001',
        'nome': 'Paçoca',
        'sexo': 'F',
        'nascimento': '24/10/2023'
    }

    animal_random = {
        '_id': 'a002',
        'nome': 'Dudu',
        'sexo': 'M',
        'nascimento': '07/07/2025'
    }

    internacoes = [
        {
        "_id": 'i001',
        "animal_id" : "a001",
        "momento_entrada": "14:30:05 15/08/2024"
        },
        {
            "_id": 'i002',
            "animal_id": "a001",
            "momento_entrada": "09:01:50 10/02/2025"
        }
    ]

    bd.animal.insert_one(animal_c1)
    bd.animal.insert_one(animal_random)
    bd.internacao.insert_many(internacoes)
    print("Dados do cenário 1 inseridos. \n")

def consulta_cenario1(bd):
    print("Iniciando a consulta: ")
    resultado = bd.internacao.aggregate([
        {'$lookup':
            {
                'from': 'animal',
                'localField': 'animal_id',
                'foreignField': '_id',
                'as': 'animal'
            }
        }
    ])
    return resultado

def executar_cenario1(bd):
    inserir_cenario1(bd)
    resultado = consulta_cenario1(bd)

    for doc in resultado: 
        print(f"Paçoca foi internada em {doc['momento_entrada']}")
    
