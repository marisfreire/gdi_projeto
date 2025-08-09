# Cenário 1: Referência Única (Supervisionado referencia o Supervisor)

def inserir_cenario1(bd):
    """Insere os dados no banco de dados para o cenário 1."""
    print("Iniciando inserção de dados para o Cenário 1...")
    
    # Coleção de veterinarios
    veterinarios = [
        # O Supervisor
        {'_id': 'v01', 'nome': 'Dr. House', 'crmv': '1111-PE'},
        
        # Os Supervisionados, com a referência para o supervisor
        {'_id': 'v02', 'nome': 'Dr. Chase', 'crmv': '2222-PE', 'supervisor_id': 'v01'},
        {'_id': 'v03', 'nome': 'Dra. Cameron', 'crmv': '3333-PE', 'supervisor_id': 'v01'},

        # Um veterinário que não tem supervisor
        {'_id': 'v04', 'nome': 'Dr. Wilson', 'crmv': '4444-PE'}
    ]
    
    bd.veterinarios.insert_many(veterinarios)
    print("Dados do Cenário 1 inseridos com sucesso.\n")

def consulta_cenario1(bd):
    """Realiza a consulta para encontrar os supervisionados de um supervisor específico."""
    print("Iniciando a consulta do Cenário 1...")
    
    # Passo 1: Encontrar o _id do supervisor "Dr. House"
    supervisor = bd.veterinarios.find_one({'nome': 'Dr. House'})
    supervisor_id = supervisor['_id']
    
    # Passo 2: Encontrar todos os veterinários que referenciam esse _id
    supervisionados = bd.veterinarios.find({'supervisor_id': supervisor_id})
    return supervisionados

def executar_cenario1(bd):
    """Executa a inserção, consulta e exibe os resultados para o Cenário 1."""
    inserir_cenario1(bd)
    resultado = consulta_cenario1(bd)

    print("--- Resultado da Consulta ---")
    print("Veterinários supervisionados por Dr. House:")
    for doc in resultado:
        print(f"- {doc['nome']}")
    print("---------------------------\n")