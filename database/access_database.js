const { MongoClient } = require('mongodb');

function obter_colecao() {
    let doc = {};
    const uri = "mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
    client.connect(err => {
      const collection = client.db("Listify_db").collection("statistics");
      doc = collection.find({})
    });
    return doc
}

function novo_sentimento(sentimento) {
    const uri = "mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
    client.connect(err => {
      const collection = client.db("Listify_db").collection("statistics");
      key = "sentimentos."+sentimento;
      collection.updateOne(
          {},
          {
              "$inc": { key : 1 }
            });
      client.close();
    });
}

function novo_acesso_agora(){
    const uri = "mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
    client.connect(err => {
      const collection = client.db("Listify_db").collection("statistics");
      collection.updateOne(
          {},
          {
              "$push": { "acessos" : new Date()}
          });
      client.close();
    });
}

function nova_pesquisa(query){
    const uri = "mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
    client.connect(err => {
      const collection = client.db("Listify_db").collection("statistics");
      key = "pesquisas."+query;
      collection.updateOne(
          {},
          {
              "$inc": { key : 1 }
          });
      client.close();
    });
}