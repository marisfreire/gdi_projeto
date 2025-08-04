import sqlite3 as sql3
from sqlite3 import OperationalError
conn = sql3.connect('clinicavet.db')
print("Bem vindo(a) a Clínica Veterinária:\n")
print()

cursor = conn.cursor()

arquivo = open('criacao.sql', 'r')
criacao = arquivo.read()
arquivo.close()

comandos = criacao.split(';') 

# executando os comandos pra criação
for comando in comandos:
        cursor.execute(comando)
    #    print("Comando pulado: ", comando)
# solicitando os dados ao usuário
continuar = True

while(continuar):
    consulta = input(" Digite sua consulta ou digite 0 para sair.")
    if(consulta == "0"):
        continuar = False
    else:
        resultado = cursor.execute(consulta) 
        linhas = resultado.fetchall
        for linha in linhas:
            print(linha) 
            
conn.close()
print("Até a próxima!\n")