import pymongo

clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
bd = clinica_vet['banco_de_dados']

# documento com um array de referências para documentos
# tutor com array de referência em animal 
def inserir_cenario3(colecao):
    bd.tutor.delete_many({})
    bd.animal.delete_many({})

    tutor1 = {"_id": 111, "nome": "Giovanna Mafra"}
    tutor2 = {"_id": 222, "nome": "Ana Silva"}
    tutor3 = {"_id": 333, "nome": "Paulo Gustavo"}
    tutor4 = {"_id": 444, "nome": "Andson Baladeiro"}
    tutor5 = {"_id": 555, "nome": "Paula Baladeiro"}
    tutor6 = {"_id": 666, "nome": "Pedro Mafra"}
    tutor7 = {"_id": 777, "nome": "Helena Mafra"}

    animal = [
        {"_id" : 1, 
        "nome" : "Umbigo", 
        "tutor_id": [tutor1["_id"], tutor6["_id"], tutor7["_id"]]
        },
        {"_id" : 2, 
        "nome" : "Bolinha", 
        "tutor_id": tutor2["_id"]
        },
        {"_id" : 3, 
        "nome" : "Paçoca", 
        "tutor_id": tutor3["_id"]
        },
        {"_id" : 4, 
        "nome" : "Caramelo", 
        "tutor_id": [tutor4["_id"], tutor4["_id"]]
        }
    ]
    
    bd.tutor.insert_many([tutor1, tutor2, tutor3, tutor4, tutor5, tutor6, tutor7])
    bd.animal.insert_many(animal)
    print("Cenário 3 inserido com sucesso!")

def remover_cenario3(colecao):
    bd.tutor.delete_many({})
    bd.animal.delete_many({})
    print("Cenário 3 deletado com sucesso!")

def consulta_cenario3():
    nome_busca = "Umbigo"

    animais = bd.animal.find({"nome": nome_busca})

    resultados = []

    for a in animais:
        tutor_id = a.get("tutor_id", [])

        for t in tutor_id:
            tutor = bd.tutor.find_one({"_id": t})
            resultados.append({"tutor_id": tutor['_id'], "nome_tutor": tutor['nome']})
        
    print(f"Os tutores de {nome_busca} são: ")
    for r in resultados:
        print(f"Tutor ID: {r['tutor_id']} - Tutor: {r['nome_tutor']}")
