import pymongo

#documento com array de referencias
#consultorio com um array de referencias para veterinarios

def run():
    clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
    bd = clinica_vet['banco_de_dados']

    bd.veterinarios.delete_many({})
    bd.consultorios.delete_many({})

    bd.veterinarios.insert_many([
        {"id": 11, 
        "nome": "Dra. Ana"},
        {"id": 12, 
        "nome": "Dr. João"}, 
        {"id": 13, 
        "nome": "Dra. Vanessa"},
    ])

    bd.consultorios.insert_many([
        {"id": 1,
        "nome": "PetFeliz",
        "endereco": "Rua Gaspar Perez, 123", 
        "ids_veterinarios": [11, 12]},
        {"id": 2,
        "nome": "Clinica24",
        "endereco": "Rua João Borges, 456", 
        "ids_veterinarios": [13]},
    ])

    # CONSULTA

    #Busca o id de "PetFeliz"
    #Procura em veterinario os ids que estão no array de referencia
    consultorio = bd.consultorios.find_one({"nome": "PetFeliz"}) #retorna todas as informações desse consultorio
    resultado = bd.veterinarios.find(
        #"id": {"$in": [11, 12]} -> significa “pegar todos os veterinários cujo campo id esteja dentro dessa lista"
        {"id": {"$in": consultorio["ids_veterinarios"]}},
        {"_id": 0, "nome": 1}
    )

    print("Cenario 3", list(resultado))