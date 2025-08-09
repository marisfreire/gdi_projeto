import pymongo

#documento referenciando apenas um documento 
#documentos separados, veterinario referenciando consultorio via ID

def run():
    clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
    bd = clinica_vet['banco_de_dados']

    bd.veterinarios.delete_many({})
    bd.consultorios.delete_many({})

    bd.consultorios.insert_many([
        {"id": 1,
        "nome": "PetFeliz",
        "endereco": "Rua Gaspar Perez, 123"},
        {"id": 2,
        "nome": "Clinica24",
        "endereco": "Rua João Borges, 456"}
    ])

    bd.veterinarios.insert_many([
        {"nome": "Dra. Ana", "consultorio_id": 1},
        {"nome": "Dr. João", "consultorio_id": 1}, 
        {"nome": "Dra. Vanessa", "consultorio_id": 2},
    ])

    # CONSULTA

    #Busca o id de "PetFeliz"
    #A partir dele procura em veterinario 
    consultorio = bd.consultorios.find_one({"nome": "PetFeliz"})
    consultorio_ID = consultorio["id"]
    resultado = bd.veterinarios.find(
        {"consultorio_id": consultorio_ID},
        {"_id": 0, "nome": 1}
    )

    print("Cenario 1", list(resultado))