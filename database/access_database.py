import pymongo
#IMPORTANTE:
# Além do pacote pymongo, pymongo[srv] também é necessário no pip. Ambos estão no arquivo requirements.txt
# O mongodb só conecta se o endereço ip de onde a request é feita estiver na whitelist de endereços, e isso tem que ser alterado manualmente no site por mim
# Então sempre que for usar uma máquina me mande o endereço ip dela no momento para que eu possa adicionar (inclusive o edereço do servidor onde o código será rodado)

#Retorna uma visão do documento principal do bd em forma de dicionário
def get_view():
    Client = pymongo.MongoClient("mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    colecao = Client.Listify_db.statistics
    return colecao.find_one()

#Atualiza o bd com a contagem de um novo sentimento
def set_novo_sentimento(sentimento):
    Client = pymongo.MongoClient("mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    colecao = Client.Listify_db.statistics
    colecao.update_one({},{"$inc": {"sentimentos."+sentimento:1}})

#Atualiza o bd com a data de um novo acesso
def set_novo_acesso(date):
    Client = pymongo.MongoClient("mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    colecao = Client.Listify_db.statistics
    colecao.update_one({},{"$push": {"acessos": date}})

#Atualiza o bd com a chave de uma nova pesquisa
def set_nova_pesquisa(query):
    Client = pymongo.MongoClient("mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    colecao = Client.Listify_db.statistics
    colecao.update_one({},{"$inc": {"pesquisas."+query: 1}})

