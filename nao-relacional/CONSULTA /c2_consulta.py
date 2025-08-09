import pymongo

#documento embutindo apenas um documento 
#veterinario embutindo consultorio 

def run():
    clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
    bd = clinica_vet['banco_de_dados']

    bd.veterinarios.delete_many({})
    bd.consultorios.delete_many({})

    bd.veterinarios.insert_many([
        {"nome": "Dra. Ana", 
        "consultorio": {"nome": "PetFeliz",
        "endereco": "Rua Gaspar Perez, 123"}},
        {"nome": "Dr. João", 
        "consultorio": {"nome": "PetFeliz",
        "endereco": "Rua Gaspar Perez, 123"}},
        {"nome": "Dra. Vanessa", 
         "consultorio": {"nome": "Clinica24",
        "endereco": "Rua João Borges, 456"}}
    ])

    # CONSULTA

    #Procurar entre todos os veterianarios, os que trabalham no "PetFeliz"

    resultado = bd.veterinarios.find(
        {"consultorio.nome" : "PetFeliz"},
        {"nome": 1}
    )

    print("Cenario 2", list(resultado))