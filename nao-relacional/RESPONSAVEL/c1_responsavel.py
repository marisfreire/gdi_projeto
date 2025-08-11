import pymongo

clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
bd = clinica_vet['banco_de_dados']

# documento referenciando apenas um documento 
# documentos separados, animal referenciando tutor via ID
def inserir_cenario1(colecao):
    bd.tutor.delete_many({})
    bd.animal.delete_many({})

    # lista de animais
    animal_doc = [
        {"_id" : 1, "nome" : "Umbigo"},
        {"_id" : 4, "nome" : "Paçoca"}, 
        {"_id" : 6, "nome" : "Bolinha"}, 
        {"_id" : 7, "nome" : "Luna"}, 
        {"_id" : 8, "nome" : "Caramelo"}, 
    ]

    # lista de tutores
    tutor_doc = [
        {"_id": 111, "nome": "Giovanna Mafra", "id_animal": 1}, 
        {"_id": 222, "nome": "Ana Silva", "id_animal": 6}, 
        {"_id": 333, "nome": "Paulo Gustavo", "id_animal": 7}, 
        {"_id": 444, "nome": "Andson Baladeiro, "id_animal": 5}, 
        {"_id": 555, "nome": "Maria Fernanda", "id_animal": 4},
        {"_id": 666, "nome": "Pedro Mafra", "id_animal": 1},
        {"_id": 777, "nome": "Helena Mafra", "id_animal": 1},
    ]

    bd.animal.insert_many(animal_doc)
    bd.tutor.insert_many(tutor_doc)
    print("Cenário 1 inserido com sucesso!")

def remover_cenario1(colecao):
    bd.animal.delete_many({})
    bd.tutor.delete_many({})
    print("Cenário 1 deletado com sucesso!")
    print()

def consulta_cenario1():
    nome_busca = "Umbigo"

    # buscar animais com esse nome
    animais = bd.animal.find({"nome": nome_busca})

    # armazenar resultado
    resultados = []

    for animal in animais:
        id_animal = tutor.get("id_animal")
        animal = bd.animal.find({"_id" : id_animal})

        for t in tutor:
            resultados.append({"id_animal": t['_id'], "nome_tutor": t['nome']})

    print(f"Os tutores de {nome_busca} são: ")
    for r in resultados:
        print(f"Tutor ID: {r['tutor_id']} - Tutor: {r['nome_tutor']}")
