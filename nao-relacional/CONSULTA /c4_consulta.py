import pymongo

#Embutido múltiplo: um documento embutindo vários documentos
#consultorio embutindo os veterinarios 

def run():
    clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")
    bd = clinica_vet['banco_de_dados']

    bd.veterinarios.delete_many({})
    bd.consultorios.delete_many({})

    bd.consultorios.insert_many([
        {"id": 1,
        "nome": "PetFeliz",
        "endereco": "Rua Gaspar Perez, 123", 
        "veterinarios": [
        {"nome": "Dra. Ana"},
        {"nome": "Dr. João"}]},
        
        {"id": 2,
        "nome": "Clinica24",
        "endereco": "Rua João Borges, 456", 
        "veterinarios": [
        { "nome": "Dra. Vanessa"}]},
    ])

    # CONSULTA

    #Busca o id de "PetFeliz"
    #o nome de todos os veterinarios no array
    consultorio = bd.consultorios.find_one({"nome": "PetFeliz"}) #retorna todas as informações desse consultorio
    resultado = []
    for vet in consultorio["veterinarios"]:
        resultado.append(vet["nome"])

    print("Cenario 4", list(resultado))