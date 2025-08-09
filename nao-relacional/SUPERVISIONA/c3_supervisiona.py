# Cenário 3: Array de Referências (Supervisor referencia os Supervisionados)

def inserir_cenario3(bd):
    """Insere os dados no banco de dados para o cenário 3."""
    print("Iniciando inserção de dados para o Cenário 3...")
    
    veterinarios = [
        # Supervisor com um array de referências aos seus supervisionados
        {'_id': 'v01', 'nome': 'Dr. House', 'crmv': '1111-PE', 'supervisionados_ids': ['v02', 'v03']},
        
        # Os supervisionados como documentos separados
        {'_id': 'v02', 'nome': 'Dr. Chase', 'crmv': '2222-PE'},
        {'_id': 'v03', 'nome': 'Dra. Cameron', 'crmv': '3333-PE'},
        
        # Veterinário aleatório
        {'_id': 'v04', 'nome': 'Dr. Wilson', 'crmv': '4444-PE'}
    ]
    
    bd.veterinarios.insert_many(veterinarios)
    print("Dados do Cenário 3 inseridos com sucesso.\n")

def consulta_cenario3(bd):
    """Realiza a consulta para encontrar os supervisionados de um supervisor específico."""
    print("Iniciando a consulta do Cenário 3...")
    
    # Passo 1: Encontrar o supervisor e pegar o array de IDs
    supervisor = bd.veterinarios.find_one({'nome': 'Dr. House'})
    ids_dos_supervisionados = supervisor.get('supervisionados_ids', [])
    
    # Passo 2: Usar o operador $in para buscar todos os documentos com esses IDs
    if ids_dos_supervisionados:
        supervisionados = bd.veterinarios.find({'_id': {'$in': ids_dos_supervisionados}})
    else:
        supervisionados = []
        
    return supervisionados

def executar_cenario3(bd):
    """Executa a inserção, consulta e exibe os resultados para o Cenário 3."""
    inserir_cenario3(bd)
    resultado = consulta_cenario3(bd)
    
    print("--- Resultado da Consulta ---")
    print("Veterinários supervisionados por Dr. House:")
    for doc in resultado:
        print(f"- {doc['nome']}")
    print("---------------------------\n")