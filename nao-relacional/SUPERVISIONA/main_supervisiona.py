import pymongo
from c1_supervisiona import executar_cenario1
from c2_supervisiona import executar_cenario2
from c3_supervisiona import executar_cenario3
from c4_supervisiona import executar_cenario4

# Conexão com o MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Limpa bancos de dados antigos (opcional, mas bom para testes)
db_list = client.list_database_names()
for db_name in db_list:
    if db_name not in ['admin', 'config', 'local']:
        client.drop_database(db_name)

# Define o banco de dados e a coleção a ser usada
bd = client['clinica_vet']
veterinarios = bd.create_collection('veterinarios')

# Menu de escolha para o usuário
while True:
    print("\nEscolha um cenário de modelagem para o relacionamento SUPERVISIONA:")
    print("1 - Cenário 1: Referência Única")
    print("2 - Cenário 2: Embutido Único")
    print("3 - Cenário 3: Array de Referências")
    print("4 - Cenário 4: Embutido Múltiplo")
    print("0 - Sair")

    escolha = input("Digite a opção desejada: ")

    if escolha == '1':
        executar_cenario1(bd)
    elif escolha == '2':
        executar_cenario2(bd)
    elif escolha == '3':
        executar_cenario3(bd)
    elif escolha == '4':
        executar_cenario4(bd)
    elif escolha == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        continue

    # Limpa a coleção para a próxima execução
    print("Limpando a coleção 'veterinarios' para o próximo teste...")
    bd.veterinarios.delete_many({})

client.close()