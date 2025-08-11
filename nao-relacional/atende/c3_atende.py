#documento com array de referencias
#consultorio com um array de referencias para veterinarios

def inserir_cenario3(bd):
    """
    Inserir animais com array de referências para veterinários
    """
    animais_c3 = [
        {
            "_id": "a001",
            "nome": "Paçoca",
            "sexo": "F",
            "nascimento": "24/10/2023",
            "veterinarios_ids": [1]  # Referências para veterinários
        },
        {
            "_id": "a002",
            "nome": "Dudu",
            "sexo": "M",
            "nascimento": "07/07/2025",
            "veterinarios_ids": [3,2]  # Referência para veterinário
        }
    ]

    veterinarios = [
        {"_id": 1, "nome": "Dra. Ana"},
        {"_id": 2, "nome": "Dr. João"},
        {"_id": 3, "nome": "Dra. Vanessa"}
    ]

    bd.animal_c3.insert_many(animais_c3)
    bd.veterinario.insert_many(veterinarios)
    print("Dados do cenário 3 inseridos.\n")


def consulta_cenario3(bd):
    """
    Buscar veterinários que atendem 'Paçoca' usando o array de referências
    """
    print("Consulta no cenário 3")
    
    resultado = bd.animal_c3.aggregate([
        {
            "$match": {"nome": "Paçoca"}  # Encontra o animal Paçoca
        },
        {
            "$lookup": {  # Faz o join com a coleção de veterinários
                "from": "veterinario",
                "localField": "veterinarios_ids",
                "foreignField": "_id",
                "as": "veterinarios"
            }
        },
        {
            "$unwind": "$veterinarios"  # Desagrega o array de veterinários
        },
        {
            "$project": {  # Seleciona apenas o nome do veterinário
                "_id": 0,
                "nome_veterinario": "$veterinarios.nome"
            }
        }
    ])

    veterinarios = [doc["nome_veterinario"] for doc in resultado]
    print("Veterinários que atendem a Paçoca:", veterinarios)


def executar_cenario3(bd):
    inserir_cenario3(bd)
    consulta_cenario3(bd)