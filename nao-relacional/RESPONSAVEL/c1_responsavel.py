import pymongo

clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
bd = clinica_vet['banco_de_dados']

# documento referenciando apenas um documento 
# documentos separados, animal referenciando tutor via ID
def inserir_cenario1(colecao):
    # lista de tutores
    tutor_doc = [
        {"_id": 111, "nome": "Giovanna Mafra"}, 
        {"_id": 222, "nome": "Ana Silva"}, 
        {"_id": 333, "nome": "Paulo Gustavo"}, 
        {"_id": 444, "nome": "Andson Baladeiro"}, 
        {"_id": 555, "nome": "Maria Fernanda"}, 
    ]
    
    # lista de animais
    animal_doc = [
        {"_id" : 1, "nome" : "Umbigo", "id_tutor": 111},
        {"_id" : 2, "nome" : "Umbigo", "id_tutor": 222},
        {"_id" : 3, "nome" : "Umbigo", "id_tutor": 333},
        {"_id" : 4, "nome" : "Paçoca", "id_tutor": 333}, 
        {"_id" : 5, "nome" : "Paçoca", "id_tutor": 444}, 
        {"_id" : 6, "nome" : "Bolinha", "id_tutor": 333}, 
        {"_id" : 7, "nome" : "Luna", "id_tutor": 444}, 
        {"_id" : 8, "nome" : "Caramelo", "id_tutor": 555}, 
    ]

    bd.tutor.insert_many(tutor_doc)
    bd.animal.insert_many(animal_doc)
    print("✅ Cenário 1 inserido com sucesso!")

def remover_cenario1(colecao):
    bd.animal.delete_many({})
    bd.tutor.delete_many({})
    bd.responsavel.delete_many({})
    print("🗑️ Cenário 1 deletado com sucesso!")

def consulta_cenario1():
    nome_busca = "Umbigo"

    # buscar animais com esse nome
    animais = bd.animal.find({"nome": nome_busca})

    # armazenar resultado
    resultados = []

    for animal in animais:
        tutor_id = animal.get["id_tutor"]
        tutor = bd.tutor.find({"_id" : tutor_id})

        for t in tutor:
            resultados.append({"tutor_id": t['_id'], "nome_tutor": t['nome']})

    print(f"Os tutores de {nome_busca} são: ")
    for r in resultados:
        print(f"Tutor ID: {r['tutor_id']} - Tutor: {r['nome_tutor']}")
        print()
