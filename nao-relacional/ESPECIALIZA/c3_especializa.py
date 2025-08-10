import pymongo

def inserir_cenario3(bd):
    bd.veterinario.delete_many({})
    bd.especialidade.delete_many({})

    # Inserir especialidades
    especialidades = [
        {"_id": "e001", "nome": "Cardiologia"},
        {"_id": "e002", "nome": "Ortopedia"},
        {"_id": "e003", "nome": "Dermatologia"},
        {"_id": "e004", "nome": "Cirurgia"},
        {"_id": "e005", "nome": "Oncologia"}
    ]
    bd.especialidade.insert_many(especialidades)

    # Inserir veterinários com array de referências a especialidades
    veterinarios = [
        {
            "_id": "11111111111",
            "nome": "Dr. João Silva",
            "crmv_uf": "PE",
            "crmv_num": "1234",
            "especialidades_ids": ["e001", "e002"]
        },
        {
            "_id": "22222222222",
            "nome": "Dra. Maria Souza",
            "crmv_uf": "PE",
            "crmv_num": "5678",
            "especialidades_ids": ["e003"]
        },
        {
            "_id": "33333333333",
            "nome": "Dr. Carlos Oliveira",
            "crmv_uf": "PE",
            "crmv_num": "9012",
            "especialidades_ids": ["e004", "e005"]
        }
    ]
    bd.veterinario.insert_many(veterinarios)

    print("Dados do cenário 3 inseridos com sucesso!\n")

def consulta_cenario3(bd):
    print("Consultando especialidades do Dr. João Silva:")
    
    resultado = bd.veterinario.aggregate([
        {
            "$match": {"_id": "11111111111"}
        },
        {
            "$lookup": {
                "from": "especialidade",
                "localField": "especialidades_ids",
                "foreignField": "_id",
                "as": "especialidades"
            }
        },
        {
            "$project": {
                "_id": 0,
                "nome": 1,
                "especialidades.nome": 1
            }
        }
    ])
    
    for doc in resultado:
        print(f"Veterinário: {doc['nome']}")
        for esp in doc['especialidades']:
            print(f" - Especialidade: {esp['nome']}")

def executar_cenario3(bd):
    inserir_cenario3(bd)
    consulta_cenario3(bd)