import pymongo

Client = pymongo.MongoClient("mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
col = Client.Listify_db.statistics

col.delete_one({})
col.insert_one({
                    "sentimentos": {
                        "muito_feliz": 0,
                        "feliz": 0,
                        "neutro": 0,
                        "triste": 0,
                        "muito_triste": 0
                    },

                    "acessos":[],

                    "pesquisas": {}
                })