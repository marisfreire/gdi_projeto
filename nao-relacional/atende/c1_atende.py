# Cenário 1
# Documento que referencia apenas um documento

def inserir_cenario1(bd):
    animais_c1 = [
        {
            '_id': 'a001',
            'nome': 'Paçoca',
            'sexo': 'F',
            'nascimento': '24/10/2023'
        },
        {
            '_id': 'a002',
            'nome': 'Dudu',
            'sexo': 'M',
            'nascimento': '07/07/2025'
        }
    ]

    veterinarios = [
        {"nome": "Dra. Ana", "consultorio_id": 1, "animal_id": "a001"},
        {"nome": "Dr. João", "consultorio_id": 1, "animal_id": "a002"},
        {"nome": "Dra. Vanessa", "consultorio_id": 2, "animal_id": "a002"}
    ]
# Inserir animais e veterinários no banco de dados
    bd.animal.insert_many(animais_c1)
    bd.veterinario.insert_many(veterinarios)
    print("Dados do cenário 1 inseridos.\n")


def consulta_cenario1(bd):
    print("Nova consulta no cenário 1")

    # Buscar ID do consultório que atendeu Paçoca
    animal = bd.animal.find_one({"nome": "Paçoca"})
    if not animal:
        print("Animal não encontrado!")
        return

    # Pegar todos veterinários que atenderam esse animal
    resultado = bd.veterinario.find(
        {"animal_id": animal["_id"]},
        {"_id": 'a001', "nome": 1}
    )

    # Extrair apenas os nomes dos veterinários
    nomes_veterinarios = [vet["nome"] for vet in resultado]
    
    print("Veterinários que atenderam a Paçoca:", nomes_veterinarios)

def executar_cenario1(bd):
    inserir_cenario1(bd)
    consulta_cenario1(bd)
