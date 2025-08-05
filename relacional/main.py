import sqlite3 as sql3
import os
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

try:
    with open('povoamento.sql', 'r') as arquivo_povoamento:
        povoamento_sql = arquivo_povoamento.read()
        comandos_povoamento = povoamento_sql.split(';')
        for comando in comandos_povoamento:
            if comando.strip():
                cursor.execute(comando)
except OperationalError as e:
    print("Erro ao executar povoamento:", e)

while(continuar):
    print(" Digite sua consulta ou digite 0 para sair.\n")
    linha_consulta = ''
    consulta_toda =  ''
    while(linha_consulta != ';' and linha_consulta != '0'):
        linha_consulta = input()
        consulta_toda += linha_consulta + ' '

    if(linha_consulta == "0"):
        continuar = False
    else:
        resultado = cursor.execute(consulta_toda) 
        linhas = resultado.fetchall()
        for linha in linhas:
            print(linha)


os.remove('./clinicavet.db')
conn.close()
print("Até a próxima!\n")