import c1_consulta
import c2_consulta
import c3_consulta
import c4_consulta

if __name__ == "__main__":

    while True:
        escolha = input("Digite a opção: ")

        if escolha == '1':
            c1_consulta.run()
        elif escolha == '2':
            c2_consulta.run()
        elif escolha == '3':
            c3_consulta.run()
        elif escolha == '4':
            c4_consulta.run()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
    
    
    
   
