# c4_atende.py
def inserir_cenario4(bd):
    """
    Veterinários com array de animais embutidos.
    Usamos a mesma referência de ids/nomes definida no Cenário 1 + a003 (Thor) do C3.
    """
    veterinarios_c4 = [
        {
            "nome": "Dr. João",
            "consultorio_id": 1,
            "animais": [
                {"_id": "a001", "nome": "Paçoca", "sexo": "F", "nascimento": "24/10/2023"},
                {"_id": "a003", "nome": "Thor",   "sexo": "M", "nascimento": "10/03/2022"}
            ]
        },
        {
            "nome": "Dra. Maria",
            "consultorio_id": 2,
            "animais": [
                {"_id": "a002", "nome": "Dudu",  "sexo": "M", "nascimento": "07/07/2025"}
            ]
        }
    ]

    bd.veterinario_c4.insert_many(veterinarios_c4)
    print("Dados do cenário 4 inseridos.\n")


def consulta_cenario4(bd):
    """
    Buscar veterinário que atende 'Paçoca' e mostrar só o nome
    """
    print("Consulta no cenário 4")
    resultado = bd.veterinario_c4.find(
        {"animais.nome": "Paçoca"},
        {"_id": 0, "nome": 1}  # Apenas o campo 'nome'
    )

    nomes = [doc["nome"] for doc in resultado]
    print("Veterinários que atendem Paçoca:", nomes)


def executar_cenario4(bd):
    inserir_cenario4(bd)
    consulta_cenario4(bd)
