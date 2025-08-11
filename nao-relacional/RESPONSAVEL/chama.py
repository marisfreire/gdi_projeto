import pymongo

clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
bd = clinica_vet['banco_de_dados']

from c1_responsavel import inserir_cenario1, consulta_cenario1, remover_cenario1
from c2_responsavel import inserir_cenario2, consulta_cenario2, remover_cenario2
from c3_responsavel import inserir_cenario3, consulta_cenario3, remover_cenario3
from c4_responsavel import inserir_cenario4, consulta_cenario4, remover_cenario4

# parte de luma
# relacionamento "responsável"
# tutor N : N animal 
# ACHAR TUTORES DE ANIMAIS ESPECÍFICOS

def menu():
    print("\nEscolha um cenário para rodar:")
    print("1 - Inserir e consultar cenário 1")
    print("2 - Inserir e consultar cenário 2")
    print("3 - Inserir e consultar cenário 3")
    print("4 - Inserir e consultar cenário 4")
    print("0 - Sair")
    while True:

        escolha = input("Digite a opção: ")

        if escolha == '1':
            inserir_cenario1(bd)
            print()
            consulta_cenario1(bd)
            print("----")
            remover_cenario1(bd)
            
        elif escolha == '2':
            inserir_cenario2(bd)
            print()
            consulta_cenario2()
            print()
            remover_cenario2(bd)

        elif escolha == '3':
            inserir_cenario3(bd)
            print()
            consulta_cenario3()
            print()
            remover_cenario3(bd)

        elif escolha == '4':
            inserir_cenario4(bd)
            print()
            consulta_cenario4()
            print()
            remover_cenario4(bd)

        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
