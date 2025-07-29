import pymongo


clinica_vet = pymongo.MongoClient("mongodb://localhost:27017/")

clinica_bd = clinica_vet['banco_de_dados']

## coleção é o que no SQL são tabelas
## um documento no mongodb é como um registro nos bancos de dados sql
## 