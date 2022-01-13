# TP1 Engenharia de Software

## Equipe:

* André Luiz Moreira Dutra: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Back-end Developer
* Antônio Isaac Silva Lima: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Back-end Developer
* Emanuel Juliano Morais Silva: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Front-end Developer
* Marcos Vinicius Caldeira Pacheco: &nbsp;&nbsp;Front-end Developer

## Escopo:
O Listify será um website que funcione como uma central de dados musicais do spotify. Nela, o usuário poderá criar automaticamente, a partir de palavras-chave, playlists com músicas compatíveis, permitindo criar playlists para eventos específicos, ou baseadas em um sentimento, por exemplo. Além disso, cada usuário poderá associar sua conta e observar seus dados de uso, bem como faixas e playlists salvas, dentre outros informações relevantes de sua conta.

## Backlog do Sprint:

### História:
  Como amante de músicas, gostaria de um site de músicas conectado ao Spotify.
  * **Tarefas:**
    * Design Base das Telas [Marcos e Emanuel]
    * Construir Telas [Marcos]
    * Plugar Back-end no Front-end; [Isaac] 
    * Implementar e Plugar Banco de dados; [André]

### História:
Como usuário do site, eu gostaria de pesquisar músicas por palavras-chave.
* **Tarefas:**
  * Definir viabilidade das APIs e testar funcionalidades [André]
  * Criar tela que coleta palavra-chave e direciona para back-end  [Emanuel]
  * Pega a palavra-chave e retorna uma lista de músicas (back-end) [Isaac];
  * Exibir lista de músicas vindas do back-end (front-end) [Marcos];


### História:
Como amante de músicas, eu gostaria de obter músicas relacionadas a sentimentos.
* **Tarefas:**
  * Criar tela para coletar sentimentos da pesquisa do usuário [Marcos]
  * Obter sinônimos a partir da palavra-chave (back-end) [Isaac];
  * Projetar a modelagem do sentimento (back-end) [André];
  * Exibir lista de músicas pelo sentimento [Emanuel];


### História:
Gostaria de ver informações sobre o site e sobre como outras pessoas o usam.
* **Tarefas:**
  * Definir estatísticas relevantes do site e sua viabilidade [Emanuel]
  * Coletar informações de interesse do usuário pela API; [Isaac]
  * Criar estatísticas a partir das informações coletadas e salvar no banco de dados; (back-end) [André]
  * Exibir as estatísticas no site; (front-end) [Marcos]


### História:
Gostaria de salvar as playlists montadas pelo site na minha conta do spotify.
* **Tarefas:**
  * Descobrir como conectar com uma conta no spotify [André]
  * Criar tela de conectar usuário [Emanuel]
  * Utilizar API para salvar playlist na conta [Isaac]
  * Criar wigdet de salvar playlist [Marcos]
  * Salvar usuário no banco de dados [André]

## Principais tecnologias
O projeto foi programado na linguagem **JavaScript** no front-end, usando o framework **Vue.js**, e **python** e **AWS** no backend. Para a coleta de dados, foi usada a **Spotify Web API**, que permite acesso aos bancos de dados de usuários, faixas, playlists e outros dados do Spotify relevantes para a aplicação, e a **Google Natural Language API**, que permitiu a classificação de sentimentos para cada texto.


## Retrospectiva do Sprint

Para o próximo sprint pretendemos realizar algumas melhorias e implementar novas funções no projeto:

Todas as histórias foram implementadas, com exceção da última que era relacionada à conexão do usuário do site com sua conta do spotify, portanto deixamos essa conexão para o próximo sprint.

Em relação ao banco de dados, utilizamos o firebase provisoriamente, para retrospectivas futuras pretendemos modificar pelo mongoDB pois é mais robusto.

O sistema não está otimizado para ser utilizado no navegador do celular, portanto pretendemos realizar essa otimização para o próximo sprint.

Ficamos felizes com a página de estatísticas, nos dá uma ideia de como os usuários utilizam nosso site. Porém, outras estatísticas poderiam ser adicionadas e que também são úteis, como as últimas músicas pesquisadas no site.

Durante a implementação do trabalho e criação do Design tivemos ideias melhores sobre como apresentar os sentimentos para o usuário. Ao invés de utilizar uma API de sinônimos encontramos uma outra API que retornava informações acerca do sentimento da música, o que foi ideal para a ideia do sistema.
