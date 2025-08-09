# Cenário 3 
# Um documento com array de referências para documentos

def inserir_cenario3(bd):

    animal_c3 = {
        '_id': 'a001',
        'nome': 'Paçoca',
        'sexo': 'F',
        'nascimento': '24/10/2023',
        'internacoes_ref': ['i001', 'i002', 'i004']
    }

    animal_random = {
        '_id': 'a002',
        'nome': 'Dudu',
        'sexo': 'M',
        'nascimento': '07/07/2025',
        'internacoes_ref': ['i003', 'i005']   
    }

    internacoes = [{
        '_id': 'i001',
        "momento_entrada": "09:30:05 25/12/2024"
        },
        {
         '_id': 'i002',
         'momento_entrada': '07:56:38 03/05/2024'   
        }, 
        {
         '_id': 'i003',
         'momento_entrada': '17:25:11 17/09/2025'   
        }, 
        {
         '_id': 'i004',
         'momento_entrada': '03:02:15 30/11/2024'   
        }, 
        {
            '_id': 'i005',
            'momento_entrada': '12:45:20 01/01/2026'
        }]

    bd.animal.insert_one(animal_c3)
    bd.animal.insert_one(animal_random)
    bd.internacao.insert_many(internacoes)
    print("Dados do cenário 3 inseridos. \n")

def consulta_cenario3(bd):
    print("Iniciando a consulta: ")

    resultado = bd.animal.aggregate([
        { '$lookup':
            {
                'from': 'internacao',
                'localField': 'internacoes_ref',
                'foreignField': '_id',
                'as': 'internacoes'
        
            }
        }, 
        {
            '$match': {'nome': 'Paçoca'}
        },
        {
            '$project': {'_id': 0, 'internacoes.momento_entrada':1 }
        }
    ])
    return resultado

def executar_cenario3(bd):
    inserir_cenario3(bd)
    resultado = consulta_cenario3(bd).to_list()

    for doc in resultado[0]['internacoes']:
        print(f"Paçoca foi internada em {doc['momento_entrada']}")