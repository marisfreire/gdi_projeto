import pymongo

def inserir_cenario4(bd):
    bd.veterinario.delete_many({})

    # Inserir veterinários com array de especialidades embutidas
    veterinarios = [
        {
            "_id": "11111111111",
            "nome": "Dr. João Silva",
            "crmv_uf": "PE",
            "crmv_num": "1234",
            "especialidades": [
                {"nome": "Cardiologia", "data_certificacao": "2020-05-15"},
                {"nome": "Ortopedia", "data_certificacao": "2021-02-20"}
            ]
        },
        {
            "_id": "22222222222",
            "nome": "Dra. Maria Souza",
            "crmv_uf": "PE",
            "crmv_num": "5678",
            "especialidades": [
                {"nome": "Dermatologia", "data_certificacao": "2019-11-20"}
            ]
        },
        {
            "_id": "33333333333",
            "nome": "Dr. Carlos Oliveira",
            "crmv_uf": "PE",
            "crmv_num": "9012",
            "especialidades": [
                {"nome": "Cirurgia", "data_certificacao": "2021-03-10"},
                {"nome": "Oncologia", "data_certificacao": "2022-01-05"}
            ]
        }
    ]
    bd.veterinario.insert_many(veterinarios)

    print("Dados do cenário 4 inseridos com sucesso!\n")

def consulta_cenario4(bd):
    print("Consultando especialidades do Dr. João Silva:")
    
    resultado = bd.veterinario.find(
        {"_id": "11111111111"},
        {"_id": 0, "nome": 1, "especialidades": 1}
    )
    
    for doc in resultado:
        print(f"Veterinário: {doc['nome']}")
        for esp in doc['especialidades']:
            print(f" - Especialidade: {esp['nome']} (Certificado em: {esp['data_certificacao']})")

def executar_cenario4(bd):
    inserir_cenario4(bd)
    consulta_cenario4(bd)