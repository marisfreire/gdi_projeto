import pymongo

clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
bd = clinica_vet['banco_de_dados']

# documento embutido apenas um documento 
# documento embutido único (tutor dentro de animal)
def inserir_cenario2(colecao):
    bd.tutor.delete_many({})

    tutor_doc = [
        {"_id" : 111, 
        "nome" : "Giovanna Mafra", 
        "animal": {
            "nome": "Umbigo",
            }
        },
        {"_id" : 222, 
        "nome" : "Zuiderly Mafra", 
        "animal": {
            "nome": "Umbigo"
            }
        },
        {"_id" : 333, 
        "nome" : "Helena Mafra", 
        "animal": {
            "nome": "Umbigo"
            }
        },
        {"_id" : 444, 
        "nome" : "Andson Baladeiro", 
        "animal": {
            "nome": "Bolinha"
            }
        }
    ]

    bd.tutor.insert_many(tutor_doc)
    print("Cenário 2 inserido com sucesso!")

def remover_cenario2(colecao):
    bd.tutor.delete_many({})
    print("Cenário 2 deletado com sucesso!")

def consulta_cenario2():
    nome_busca = "Umbigo"

    # buscar animais com esse nome
    resultados = bd.tutor.find({"animal.nome": nome_busca})
    
    print(f"Os tutores de {nome_busca} são: ")
    for r in resultados:
        print(f"Tutor: {r['nome']}")

