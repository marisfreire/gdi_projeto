import pymongo

def inserir_cenario2(bd):
    bd.veterinario.delete_many({})

    # Inserir veterinários com especialidade embutida (apenas uma)
    veterinarios = [
        {
            "_id": "11111111111",
            "nome": "Dr. João Silva",
            "crmv_uf": "PE",
            "crmv_num": "1234",
            "especialidade": {
                "nome": "Cardiologia",
                "data_certificacao": "2020-05-15"
            }
        },
        {
            "_id": "22222222222",
            "nome": "Dra. Maria Souza",
            "crmv_uf": "PE",
            "crmv_num": "5678",
            "especialidade": {
                "nome": "Dermatologia",
                "data_certificacao": "2019-11-20"
            }
        },
        {
            "_id": "33333333333",
            "nome": "Dr. Carlos Oliveira",
            "crmv_uf": "PE",
            "crmv_num": "9012",
            "especialidade": {
                "nome": "Cirurgia",
                "data_certificacao": "2021-03-10"
            }
        }
    ]
    bd.veterinario.insert_many(veterinarios)

    print("Dados do cenário 2 inseridos com sucesso!\n")

def consulta_cenario2(bd):
    print("Consultando veterinários com especialidade em Cirurgia:")
    
    resultado = bd.veterinario.find(
        {"especialidade.nome": "Cirurgia"},
        {"_id": 0, "nome": 1, "especialidade.nome": 1}
    )
    
    for doc in resultado:
        print(f"Veterinário: {doc['nome']} - Especialidade: {doc['especialidade']['nome']}")

def executar_cenario2(bd):
    inserir_cenario2(bd)
    consulta_cenario2(bd)