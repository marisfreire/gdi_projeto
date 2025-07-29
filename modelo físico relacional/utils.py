import sqlite3
import io

def insert(db):
    try:
        nome = input("Nome: ")
        db.cursor.execute("""
        INSERT INTO clinicavet (nome)
        VALUES (?)
                          """, nome)
        db.commit()
        print("Registro inserido com sucesso.")
        return
    except sqlite3.IntegrityError:
        print("Aviso: Erro no registro.")
        return False

def delete(id, db):
    try:
        resultado = db.execute('SELECT * FROM clinicavet WHERE nome = ?', (id,))
        if(resultado):
            db.execute("""
            DELETE FROM clinicavet WHERE id = ?
""", (id,))
            db.commit()
            print("Registro %d excluído com sucesso." % id)
        else:
            print("Não existe cliente com o nome informado.")
    except:
        return

def update(id, db):
    try:
        resultado = db.execute('SELECT * FROM clinicavet WHERE nome = ?', (id,))
        if(resultado):
            db.execute("""
                UPDATE clinicavet
                SET id = ?
            """, ())
        db.commit()
        print('Dados atualizados com sucesso.')
    except:
        return

def read(db):
    sql = "SELECT * FROM clientes ORDER BY nome"
    r = db.execute(sql)
    lista = r.fetchall()

    for c in lista:
        print(c)

    return


def commands(id, db):

    if(id == 1):
        insert(db)
    elif(id == 2):
        delete(db)
    elif(id == 3):
        update(db)
    elif(id == 4):
        read(db)
    else:
        print("Comando inválido. Tente novamente.")
    