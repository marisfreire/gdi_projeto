import pymongo

def inserir_cenario1(bd):
    bd.veterinario.delete_many({})
    bd.especialidade.delete_many({})

    # Inserir veterinários
    veterinarios = [
        {"_id": "11111111111", "nome": "Dr. João Silva", "crmv_uf": "PE", "crmv_num": "1234"},
        {"_id": "22222222222", "nome": "Dra. Maria Souza", "crmv_uf": "PE", "crmv_num": "5678"},
        {"_id": "33333333333", "nome": "Dr. Carlos Oliveira", "crmv_uf": "PE", "crmv_num": "9012"}
    ]
    bd.veterinario.insert_many(veterinarios)

    # Inserir especialidades (referenciando veterinários)
    especialidades = [
        {"_id": "e001", "nome": "Cardiologia", "vet_id": "11111111111"},
        {"_id": "e002", "nome": "Ortopedia", "vet_id": "11111111111"},
        {"_id": "e003", "nome": "Dermatologia", "vet_id": "22222222222"},
        {"_id": "e004", "nome": "Cirurgia", "vet_id": "33333333333"},
        {"_id": "e005", "nome": "Oncologia", "vet_id": "33333333333"}
    ]
    bd.especialidade.insert_many(especialidades)

    print("Dados do cenário 1 inseridos com sucesso!\n")

def consulta_cenario1(bd):
    print("Consultando especialidades do Dr. João Silva:")
    
    resultado = bd.especialidade.aggregate([
        {
            "$lookup": {
                "from": "veterinario",
                "localField": "vet_id",
                "foreignField": "_id",
                "as": "veterinario"
            }
        },
        {
            "$match": {"vet_id": "11111111111"}
        },
        {
            "$project": {
                "_id": 0,
                "nome_especialidade": "$nome",
                "nome_veterinario": {"$arrayElemAt": ["$veterinario.nome", 0]}
            }
        }
    ])
    
    for doc in resultado:
        print(f"Especialidade: {doc['nome_especialidade']} - Veterinário: {doc['nome_veterinario']}")

def executar_cenario1(bd):
    inserir_cenario1(bd)
    consulta_cenario1(bd)