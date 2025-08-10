import pymongo

from c1_atende import executar_cenario1
from c2_atende import executar_cenario2
from c3_atende import executar_cenario3
from c4_atende import executar_cenario4

cliente = pymongo.MongoClient("mongodb://localhost:27017/")

# Apagar bancos antigos
db_list = cliente.list_database_names()
for db_name in db_list:
    if db_name not in ['admin', 'config', 'local']:
        cliente.drop_database(db_name)

# Criar banco
bd = cliente['clinica_vet']

while True:
    print("\nEscolha um cenário para rodar:")
    print("1 - Executar cenário 1")
    print("2 - Executar cenário 2")
    print("3 - Executar cenário 3")
    print("4 - Executar cenário 4")
    print("0 - Sair")

    escolha = input("Digite a opção: ")

    if escolha == '0':
        break
    elif escolha == '1':
        executar_cenario1(bd)
    elif escolha == '2':
        executar_cenario2(bd)
    elif escolha == '3':
        executar_cenario3(bd)
    elif escolha == '4':
        executar_cenario4(bd)
    else:
        print("Opção inválida!")
        continue

    print("Cenário Executado!\n")

    # Limpa todas as coleções criadas
    for colecao in bd.list_collection_names():
        bd[colecao].delete_many({})
