# Cenário 2: Embutido Único (Supervisionado embute o Supervisor)

def inserir_cenario2(bd):
    """Insere os dados no banco de dados para o cenário 2."""
    print("Iniciando inserção de dados para o Cenário 2...")
    
    supervisor_doc = {'_id': 'v01', 'nome': 'Dr. House', 'crmv': '1111-PE'}

    veterinarios = [
        # Supervisionados embutindo o documento do supervisor
        {'_id': 'v02', 'nome': 'Dr. Chase', 'crmv': '2222-PE', 'supervisor': supervisor_doc},
        {'_id': 'v03', 'nome': 'Dra. Cameron', 'crmv': '3333-PE', 'supervisor': supervisor_doc},
        
        # Veterinário aleatório sem supervisor
        {'_id': 'v04', 'nome': 'Dr. Wilson', 'crmv': '4444-PE'}
    ]
    
    bd.veterinarios.insert_many(veterinarios)
    print("Dados do Cenário 2 inseridos com sucesso.\n")

def consulta_cenario2(bd):
    """Realiza a consulta para encontrar os supervisionados de um supervisor específico."""
    print("Iniciando a consulta do Cenário 2...")
    
    # A consulta é direta, usando a notação de ponto para acessar o campo embutido
    supervisionados = bd.veterinarios.find({'supervisor.nome': 'Dr. House'})
    return supervisionados

def executar_cenario2(bd):
    """Executa a inserção, consulta e exibe os resultados para o Cenário 2."""
    inserir_cenario2(bd)
    resultado = consulta_cenario2(bd)
    
    print("--- Resultado da Consulta ---")
    print("Veterinários supervisionados por Dr. House:")
    for doc in resultado:
        print(f"- {doc['nome']}")
    print("---------------------------\n")