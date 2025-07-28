import sqlite3 as sql3
from utils import commands
conn = sql3.connect('clinicavet.db')
print("Bem vindo(a) a Clínica Veterinária:\n")
print()

cursor = conn.cursor()

# criando

cursor.execute("""
    CREATE TABLE clinicavet (
               )
""")

# solicitando os dados ao usuário
continuar = True

while(continuar):
    command_id = int(input(
    "- Digite 1 para fazer um INSERT\n" 
    "- Digite 2 para fazer uma LEITURA\n" 
    "- Digite 3 para fazer uma DELEÇÃO\n" 
    "- Digite 4 para fazer um UPDATE\n"
    "- Digite 0 para SAIR\n"
    "Aperte ENTER para confirmar\n"
    ))
    if(command_id):
        commands(command_id, cursor)
    else:
        continuar = False

conn.close()
print("Até a próxima!\n")