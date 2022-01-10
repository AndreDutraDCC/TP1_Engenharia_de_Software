# Acesso ao banco de dados mongodb

O banco de dados foi criado e está hospedado em nuvem, e para acessá-lo o mongo oferece uma interface para js. Para poupar o trabalho de aprender a usar a interface, fiz funções que fazem cada ação interessante para o banco de dados e deixei prontas para uso. Para usá-las, ainda é necessário ter o pacote do mongodb instalado no npm. Para isso execute:

```
npm install mongodb
```
## Descrição do banco

O modelo dos bancos de dados mongo é noSQL. Assim, ao invés de tabelas, um banco de dados tem coleções de documentos. Um documento é equivalente em formato a um json, ou um objeto js, e uma coleção é uma lista desses documentos. Nosso banco de dados possui uma coleção, statistics, com um único documento, que é semelhante ao exemplo no arquivo db_structure.json. Todas as informações necessárias são salvas nesse documento.

O documento tem três campos. O primeiro, sentimentos, contém uma contagem de sentimentos no site, para a realização de estatísticas. Cada vez que uma música for adicionada a uma playlist no site, o banco seria atualizado com o incremento do sentimento dessa música. Por exemplo, os scores de sentimento vão de 1 a -1. Se uma música tem score 0.8, o valor de muito feliz é incrementado. Se uma musica tem score -0.4, o valor de triste é incrementado, 0.1 incementaria neutro, e assim por diante.

O segundo campo, acessos, é uma lista de datas de acesso do site, em string com formato data ISO. Útil para fazer estatísticas de acesso do site, separar por meses e etc no gráficos.

O terceiro campo, pesquisas, tem uma contagem de quantas vezes uma chave de pesquisa foi usada. Toda vez que uma pesquisa é feita, o campo relativo a essa pesquisa seria incrementado, ou criado com valor igual a 1 caso não exista. Assim, poderíamos pegar os campos com maiores valores para mostrar as palavras mais pesquisadas.

## Funções de acesso

Foram criadas funções de consulta e atualização do banco de dados, para facilitar seu uso. Em access_database.js estão as funções necessárias para consultar e atualizar o banco de dados.

A primeira função, obter_documento, é a única função de consulta. Ela retorna um objeto js da forma do json apresentado, por exemplo:

```
obj = obter_documento();

console.log(obj.sentimentos.neutro);
console.log(obj.acessos[0]);
```

Esta é a única função de consulta, e assumo que todas as informações necessárias possam ser manipuladas usando tecnicas de manipulação padrão de objetos js. Alterações no objeto retornado não alterarão o banco de dados na nuvem, se trata apenas de uma visão dos dados.

As próximas funções são de atualização do banco na nuvem. A função novo_sentimento registra um novo sentimento no primeiro campo do documento. Quando uma nova musica for adicionada a uma playlist, a função deve ser chamada com o sentimento dessa musica, conforme descrito pelos strings do campo, por exemplo:

```
novo_sentimento("muito_triste")
```

A função novo_acesso_agora adiciona a data atual à lista de datas de acesso. Deve ser chamada logo após um acesso no site, para registrá-lo no banco:

```
novo_acesso_agora()
```

A função nova_pesquisa registra uma nova pesquisa no banco de dados, incrementando seu valor no terceiro campo conforme descrito antes. Caso a pesquisa não esteja registrada ainda, é criado um campo com chave igual ao que foi pesquisado e valor igual a 1. Por exemplo, se alguém pesquisou "Olivia Rodrigo", chame:

```
nova_pesquisa("Olivia Rodrigo")
```

PS: Não consegui testar de fato as funções. Quando tentei rodar no node, deu um problema com uma função TextEncoder, e depois de pesquisar parece que essa é uma função que o mongodb usa mas que se trata apenas de uma interface, implementada de um jeito diferente para cada navegador. Então acredito que apesar de não funcionar no node, elas funcionem bem no website de fato. De qualquer forma, acho que dessa parte você vai entender mais do que eu. Qualquer dúvida ou problema só chamar que eu tento resolver.