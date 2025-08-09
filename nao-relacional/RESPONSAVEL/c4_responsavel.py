import pymongo

clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
bd = clinica_vet['banco_de_dados']

# documento embutido vários documentos
# animal com vários responsáveis embutidos 
def inserir_cenario4(colecao):
    bd.animal.delete_many({})

    animal_doc = [
        {"_id": 1, 
        "nome": "Umbigo", 
        "responsaveis": [
            {"nome" : "Giovanna Mafra", "CPF": "11111111"}, 
            {"nome" : "Helena Mafra", "CPF": "22222222"},
            {"nome" : "Pedro Mafra", "CPF": "33333333"} 
        ]}, 
        {"_id": 2, 
        "nome": "Paçoca", 
        "responsaveis": [
            {"nome" : "Giovanna Mafra", "CPF": "11111111"}, 
            {"nome" : "Pedro Mafra", "CPF": "22222222"}, 
        ]}, 
        {"_id": 3, 
        "nome": "Bolinha", 
        "responsaveis": [
            {"nome" : "Andson Baladeiro", "CPF": "11111111"}, 
            {"nome" : "Luana Baladeira", "CPF": "22222222"}, 
        ]}, 
        {"_id": 4, 
        "nome": "Caramelo", 
        "responsaveis": [
            {"nome" : "Ana Júlia", "CPF": "11111111"},
        ]}, 
        {"_id": 5, 
        "nome": "Luna", 
        "responsaveis": [
            {"nome" : "Paulo Gustavo", "CPF": "11111111"}
        ]}, 
    ]

    bd.animal.insert_many(animal_doc)
    print("Cenário 4 inserido com sucesso!")

def remover_cenario4(colecao):
    bd.animal.delete_many({})
    print("Cenário 4 deletado com sucesso!")

def consulta_cenario4():
    nome_busca = "Umbigo"

    animais = bd.animal.find({"nome" : nome_busca})

    for a in animais:
        responsaveis = a.get("responsaveis", [])

        print(f"Os tutores de {nome_busca} são: ")
        for resp in responsaveis:
            print(f" - Nome: {resp['nome']} - CPF: {resp['CPF']}")