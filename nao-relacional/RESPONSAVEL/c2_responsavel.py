import pymongo

clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
bd = clinica_vet['banco_de_dados']

# documento embutido apenas um documento 
# documento embutido único (tutor dentro de animal)
def inserir_cenario2(colecao):
    animal_doc = [
        {"_id" : 1, 
        "nome" : "Umbigo", 
        "tutor": {
            "nome": "Giovanna Mafra",
            "CPF": "111111111",
            "telefone": "81981026677"
            }
        },
        {"_id" : 2, 
        "nome" : "Umbigo", 
        "tutor": {
            "nome": "Pedro Mafra",
            "CPF": "222222222",
            "telefone": "8167666666"
            }
        },
        {"_id" : 3, 
        "nome" : "Umbigo", 
        "tutor": {
            "nome": "Helena Mafra",
            "CPF": "333333333",
            "telefone": "81675555555"
            }
        },
        {"_id" : 4, 
        "nome" : "Paçoca", 
        "tutor": {
            "nome": "Giovanna Mafra",
            "CPF": "111111111",
            "telefone": "81981026677"
            }
        },
        {"_id" : 5, 
        "nome" : "Bolinha", 
        "tutor": {
            "nome": "Ana Silva",
            "CPF": "22222222",
            "telefone": "81988888888"
            }
        },
        {"_id" : 6, 
        "nome" : "Luna", 
        "tutor": {
            "nome": "Paulo Gustavo",
            "CPF": "33333333",
            "telefone": "81999999999"
            }
        },
        {"_id" : 7, 
        "nome" : "Caramelo", 
        "tutor": {
            "nome": "Ana Silva",
            "CPF": "44444444",
            "telefone": "81977777777"
            }
        },
        {"_id" : 7, 
        "nome" : "Caramelo", 
        "tutor": {
            "nome": "Paulo Gustavo",
            "CPF": "33333333",
            "telefone": "81999999999"
            }
        }
    ]

    bd.animal.insert_many(animal_doc)
    print("✅ Cenário 2 inserido com sucesso!")

def remover_cenario2(colecao):
    bd.animal.delete_many({})
    print("🗑️ Cenário 2 deletado com sucesso!")

def consulta_cenario2():
    nome_busca = "Umbigo"
    resultados = []

    # buscar animais com esse nome
    animais = bd.animal.find({"nome": nome_busca})

    for animal in animais:
        tutor = animal.get("tutor", {})
        resultados.append({
            "nome_tutor": tutor.get("nome"),
            "cpf_tutor": tutor.get("CPF"),
            "telefone_tutor": tutor.get("telefone")
        })
    
    print(f"Os tutores de {nome_busca} são: ")
    for r in resultados:
        print(f"Animal: {r['nome_animal']} - Tutor: {r['nome_tutor']} - CPF: {r['cpf_tutor']} - Telefone: {r['telefone_tutor']}")
        print()

