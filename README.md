# TP1 Engenharia de Software

## Equipe:

* André Luiz Moreira Dutra: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Back-end Developer
* Antônio Isaac Silva Lima: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Back-end Developer
* Emanuel Juliano Morais Silva: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Front-end Developer
* Marcos Vinicius Caldeira Pacheco: &nbsp;&nbsp;Front-end Developer

## Escopo:
A aplicação implementada será um website que funcione como uma central de dados musicais do spotify. Nela, o usuário poderá criar automaticamente, a partir de palavras-chave, playlists com músicas compatíveis, permitindo criar playlists para eventos específicos, ou baseadas em um sentimento, por exemplo. Além disso, cada usuário poderá associar sua conta e observar seus dados de uso, bem como faixas e playlists salvas, dentre outros informações relevantes de sua conta.

## Backlog do Sprint:

### História:
  Como amante de músicas, gostaria de um site de músicas conectado ao Spotify.
  * **Tarefas:**
    * Design Base das Telas [Marcos e Emanuel]
    * Construir Telas [Marcos]
    * Plugar Back-end no Front-end; [Isaac] 
    * Plugar Banco de dados; [André]

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
O projeto será programado inteiramente na linguagem **JavaScript**, e para o front-end será usado o framework **Vue.js**. Para a coleta de dados, será usada a **Spotify Web API**, que permite acesso aos bancos de dados de usuários, faixas, playlists e outros dados do Spotify relevantes para a aplicação, e a **STANDS4 Synonyms API**, que identifica sinônimos de palavras. Os testes serão feitos por meio dos frameworks de testes **Jest** e **Selenium**.
