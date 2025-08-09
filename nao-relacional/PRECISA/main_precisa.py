import pymongo
from c1_precisa import executar_cenario1
from c2_precisa import executar_cenario2
from c3_precisa import executar_cenario3
from c4_precisa import executar_cenario4

# Cria banco de dados
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Quero os dias em que "Paçoca" ficou internado
# Internações cujo nome_animal = "Paçoca" -> Seus momento_entrada 
db_list = client.list_database_names()

for db_name in db_list:
    if db_name not in ['admin', 'config', 'local']:
        client.drop_database(db_name)



bd = client['clinica_vet']
animal = bd.create_collection('animal')
internacao = bd.create_collection('internacao')

print("\nEscolha um cenário para rodar:")
print("1 - Executar cenário 1")
print("2 - Executar cenário 2")
print("3 - Executar cenário 3")
print("4 - Executar cenário 4")
print("0 - Sair")

print("Digite a opção: ")
escolha = ''

while(escolha != '0'):
    escolha = input()

    if escolha == '1':
        executar_cenario1(bd)
    elif escolha == '2':
        executar_cenario2(bd)
    elif escolha == '3':
        executar_cenario3(bd)
    elif escolha == '4':
        executar_cenario4(bd)

    if(escolha != '0'):
        print("Cenário Executado!\n")
    
    animal.delete_many({})
    internacao.delete_many({})
