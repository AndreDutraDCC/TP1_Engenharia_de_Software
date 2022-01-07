const { MongoClient } = require('mongodb');

function novo_sentimento(sentimento) {
    const uri = "mongodb+srv://ListifyES:musiquinhastopzera@projetoes1.tm97r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
    client.connect(err => {
      const collection = client.db("test").collection("devices");
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
      const collection = client.db("test").collection("devices");
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
      const collection = client.db("test").collection("devices");
      key = "pesquisas."+query;
      collection.updateOne(
          {},
          {
              "$inc": { key : 1 }
          });
      client.close();
    });
}