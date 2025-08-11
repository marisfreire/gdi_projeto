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
        {"_id": 111, "nome": "Giovanna Mafra", "id_animal": 1}, 
        {"_id": 222, "nome": "Ana Silva"}, 
        {"_id": 333, "nome": "Paulo Gustavo"}, 
        {"_id": 444, "nome": "Andson Baladeiro"}, 
        {"_id": 555, "nome": "Maria Fernanda"},
        {"_id": 666, "nome": "Zuiderly Mafra", "id_animal": 1},
        {"_id": 777, "nome": "Helena Mafra", "id_animal": 1},
    ]
    
    # lista de animais
    animal_doc = [
        {"_id" : 1, "nome" : "Umbigo"},
        {"_id" : 4, "nome" : "Paçoca"}, 
        {"_id" : 6, "nome" : "Bolinha"}, 
        {"_id" : 7, "nome" : "Luna"}, 
        {"_id" : 8, "nome" : "Caramelo"}, 
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
    animal_busca = colecao.animal.find_one({'nome':nome_busca})
    animal_id = animal_busca['_id']
    resultados = colecao.tutor.find({'id_animal': animal_id})
    print(f"Os tutores de {nome_busca} são: ")

    for r in resultados:
        print(f"Tutor ID: {r['_id']} - Tutor: {r['nome']}")
