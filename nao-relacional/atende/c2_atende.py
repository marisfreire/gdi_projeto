# Cenário 2 - Um documento embutindo apenas um documento

def inserir_cenario2(bd):
    veterinarios_c2 = [
        {
            "nome": "Dr. João",
            "consultorio_id": 1,
            "animal": {
                "_id": "a001",
                "nome": "Rex",
                "sexo": "M",
                "nascimento": "01/01/2020"
            }
        },
        {
            "nome": "Dra. Maria",
            "consultorio_id": 2,
            "animal": {
                "_id": "a002",
                "nome": "Mia",
                "sexo": "F",
                "nascimento": "05/05/2021"
            }
        }
    ]

    bd.veterinario.insert_many(veterinarios_c2)
    print("Dados do cenário 2 inseridos.\n")


def consulta_cenario2(bd):
    print("Nova consulta no cenário 2")
    
    resultado = bd.veterinario.find(
        {"animal.nome": "Mia"},
        {"_id": 0, "nome": 1}  
    )
    
    # Extrai apenas os nomes dos veterinários
    veterinarios = [vet["nome"] for vet in resultado]
    
    print("Veterinários que atendem Mia:", veterinarios)

def executar_cenario2(bd):
    inserir_cenario2(bd)
    consulta_cenario2(bd)
