# Cenário 4: Embutido Múltiplo (Supervisor embute os Supervisionados)

def inserir_cenario4(bd):
    """Insere os dados no banco de dados para o cenário 4."""
    print("Iniciando inserção de dados para o Cenário 4...")
    
    veterinarios = [
        # Supervisor com um array embutido de seus supervisionados
        {
            '_id': 'v01', 
            'nome': 'Dr. House', 
            'crmv': '1111-PE', 
            'supervisionados': [
                {'nome': 'Dr. Chase', 'crmv': '2222-PE'},
                {'nome': 'Dra. Cameron', 'crmv': '3333-PE'}
            ]
        },
        # Veterinário aleatório
        {'_id': 'v04', 'nome': 'Dr. Wilson', 'crmv': '4444-PE'}
    ]
    
    bd.veterinarios.insert_many(veterinarios)
    print("Dados do Cenário 4 inseridos com sucesso.\n")

def consulta_cenario4(bd):
    """Realiza a consulta para encontrar os supervisionados de um supervisor específico."""
    print("Iniciando a consulta do Cenário 4...")
    
    # A consulta é muito simples: basta encontrar o supervisor.
    # Os dados dos supervisionados já estão dentro do documento dele.
    supervisor_com_dados = bd.veterinarios.find_one({'nome': 'Dr. House'})
    
    # Retorna o array de supervisionados, ou um array vazio se não encontrar
    if supervisor_com_dados:
        return supervisor_com_dados.get('supervisionados', [])
    return []

def executar_cenario4(bd):
    """Executa a inserção, consulta e exibe os resultados para o Cenário 4."""
    inserir_cenario4(bd)
    resultado = consulta_cenario4(bd)
    
    print("--- Resultado da Consulta ---")
    print("Veterinários supervisionados por Dr. House:")
    for doc in resultado:
        print(f"- {doc['nome']}")
    print("---------------------------\n")