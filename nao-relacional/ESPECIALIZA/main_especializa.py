import pymongo
from c1_especializa import executar_cenario1
from c2_especializa import executar_cenario2
from c3_especializa import executar_cenario3
from c4_especializa import executar_cenario4

def main():
    # Conectar ao MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Limpar bancos de dados existentes (exceto os padrões)
    db_list = client.list_database_names()
    for db_name in db_list:
        if db_name not in ['admin', 'config', 'local']:
            client.drop_database(db_name)
    
    # Criar banco de dados e coleções
    bd = client['clinica_vet']
    bd.create_collection('veterinario')
    bd.create_collection('especialidade')
    
    # Menu interativo
    while True:
        print("\nEscolha um cenário para rodar:")
        print("1 - Executar cenário 1")
        print("2 - Executar cenário 2")
        print("3 - Executar cenário 3")
        print("4 - Executar cenário 4")
        print("0 - Sair")
        
        escolha = input("Digite a opção: ")
        
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
            print("Opção inválida, tente novamente.")
        
        # Limpar coleções após cada execução
        bd.veterinario.delete_many({})
        bd.especialidade.delete_many({})

if __name__ == "__main__":
    main()