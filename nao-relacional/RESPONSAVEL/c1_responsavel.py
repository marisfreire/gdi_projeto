import pymongo

clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
bd = clinica_vet['banco_de_dados']

# documento referenciando apenas um documento 
# documentos separados, animal referenciando tutor via ID
def inserir_cenario1(colecao):
    bd.tutor.delete_many({})
    bd.animal.delete_many({})

    # lista de tutores
    tutor_doc = [
        {"_id": 111, "nome": "Giovanna Mafra"}, 
        {"_id": 222, "nome": "Ana Silva"}, 
        {"_id": 333, "nome": "Paulo Gustavo"}, 
        {"_id": 444, "nome": "Andson Baladeiro"}, 
        {"_id": 555, "nome": "Maria Fernanda"},
        {"_id": 666, "nome": "Pedro Mafra"},
        {"_id": 777, "nome": "Helena Mafra"},
    ]
    
    # lista de animais
    animal_doc = [
        {"_id" : 1, "nome" : "Umbigo", "id_tutor": 111},
        {"_id" : 2, "nome" : "Umbigo", "id_tutor": 666},
        {"_id" : 3, "nome" : "Umbigo", "id_tutor": 777},
        {"_id" : 4, "nome" : "Paçoca", "id_tutor": 333}, 
        {"_id" : 5, "nome" : "Paçoca", "id_tutor": 444}, 
        {"_id" : 6, "nome" : "Bolinha", "id_tutor": 222}, 
        {"_id" : 7, "nome" : "Luna", "id_tutor": 444}, 
        {"_id" : 8, "nome" : "Caramelo", "id_tutor": 555}, 
    ]

    bd.tutor.insert_many(tutor_doc)
    bd.animal.insert_many(animal_doc)
    print("Cenário 1 inserido com sucesso!")

def remover_cenario1(colecao):
    bd.animal.delete_many({})
    bd.tutor.delete_many({})
    print("Cenário 1 deletado com sucesso!")
    print()

def consulta_cenario1(colecao):
    nome_busca = "Umbigo"

    # buscar animais com esse nome
   
   
    # armazenar resultado
    resultados = colecao.animal.aggregate([
        {
            '$lookup':
            {
                'from': 'tutor',
                'localField': 'id_tutor',
                'foreignField': '_id',
                'as': 'tutor'
            }
        }
    ])
    print(f"Os tutores de {nome_busca} são: ")
    for r in resultados:
        print(f"Tutor ID: {r['_id']} - Tutor: {r['nome']}")
