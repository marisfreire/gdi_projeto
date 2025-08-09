# Cenário 4
# Um documento embutindo vários documentos

def inserir_cenario4(bd):
    
    animal_c4 = {
        '_id': 'a001',
        'nome': 'Paçoca',
        'sexo': 'F',
        'nascimento': '24/10/2003',
        'internacoes': [
            {
            "momento_entrada": "14:12:47 03/02/2025",
            "motivo" : "Fratura no braço" 
            },   
            { 
            "momento_entrada": "07:45:22 18/08/2025",
            "motivo" : "Tosse persistente" 
            }
        ]
    }

    animal_random = {
        '_id': 'a002',
        'nome': 'Dudu',
        'sexo': 'M',
        'nascimento': '07/07/2025',
        'internacoes': [
            { 
            "momento_entrada": "22:05:09 11/11/2024",
            "motivo" : "Reação alérgica" 
            }
            ,
            { 
            "momento_entrada": "12:33:58 01/01/2025",
            "motivo" : "Febre alta" 
            }
        ]
    }

    bd.animal.insert_one(animal_c4)
    bd.animal.insert_one(animal_random)
    print("Dados do cenário 4 inseridos com sucesso. \n")

def consulta_cenario4(bd):
    print("Iniciando a consulta: ")

    resultado = bd.animal.find({"nome": "Paçoca"})
    return resultado

def executar_cenario4(bd):
    inserir_cenario4(bd)
    resultado = consulta_cenario4(bd).to_list()

    for doc in resultado[0]['internacoes']:
        print(f"Paçoca foi internada em {doc['momento_entrada']}")