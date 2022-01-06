import pymongo

def novo_sentimento(collection,sentimento):
    collection.update_one({},{"$inc": {"sentimentos."+sentimento:1}})

def novo_acesso(collection,date):
    collection.update_one({},{"$push": {"acessos": date}})

def nova_pesquisa(collection,query):
    collection.update_one({},{"$inc": {"pesquisas."+query: 1}})

Client = pymongo.MongoClient("mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = Client.Listify_db

#Estatísticas do site
db.statistics.insert_one({
                        #Número de músicas do respectivo sentimento selecionadas para uma playlist
                        "sentimentos": {
                            "muito_feliz": 0,
                            "feliz": 0,
                            "neutro": 0,
                            "triste": 0,
                            "muito_triste": 0
                        },

                        #lista de datas de acesso
                        "acessos":[],

                        #Numero de vezes que uma chave foi pesquisada
                        "pesquisas": {
                            "Marcos": 1,
                            "Vinicius": 1,
                            "Caldeira": 1,
                            "Nos te amamos": 1
                        }
                    })

novo_sentimento(db.statistics, "muito_feliz")
nova_pesquisa(db.statistics, "Xuxa parabens pra voce")