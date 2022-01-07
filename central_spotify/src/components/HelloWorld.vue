<template>
  <v-container>
    <v-row class="text-center align-center" justify="center" align="center">
      <v-col cols="12">
        <v-img
          class="my-3"
          contain
          height="350"
          :src="require('../assets/logoComNome.png')"
        ></v-img>
        <!-- <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        /> -->
      </v-col>

      <!-- <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to Vuetify
        </h1>

        <p class="subheading font-weight-regular">
          For help and collaboration with other Vuetify developers,
          <br>please join our online
          <a
            href="https://community.vuetifyjs.com"
            target="_blank"
          >Discord Community</a>
        </p>
      </v-col> -->
      <v-col cols="12" justify="center" align="center">

        <v-card width="80%" class="pa-6 mb-8" border-radius="20px" elevation="5">
          <h4 class="font-weight-bold mb-6">
          O Listify é um website que funciona como uma central de dados musicais do spotify!
          </h4>
          <v-sheet width="80%">
            <ul class="text-justify">
              <li>Criar automaticamente, a partir de palavras-chave, playlists com músicas compatíveis. </li>
              <li>Verifique o sentimento geral das músicas de uma playlist, e entenda qual é a sua vibe preferida.</li>
              <li>Olhar as estatísticas do site para ver quais são as musicas mais buscadas do momento</li>
            </ul> 
          </v-sheet>
            <!-- O Listify é um website que funciona como uma central de dados musicais do spotify! 
            <br>
            Você pode criar automaticamente, a partir de palavras-chave, playlists com músicas compatíveis, permitindo criar playlists para eventos específicos, e verificar o sentimento geral das músicas. 
            <br>
            Também existe a opção de olhar as estatísticas do site e ver quais são as musicas mais buscadas do momento
            <br> -->
        </v-card>
        <h5 class="my-6">
          O Projeto faz parte do Trabalho Prático 1 de Engenharia de Software, sendo desenvolvido pelos alunos André Luiz, Antônio Isaac, Emanuel Juliano e Marcos Vinicius.
        </h5>
      </v-col>

      <v-col
        class="mb-5"
        cols="12"
         justify="center" align="center"
      >
        <v-sheet
          color="white"
          elevation="15"
          rounded="xl"
          height="150"
          width="50%"
          class="py-6 my-2"
          >

          <h2 class="headline font-weight-bold mb-8">
            Experimente:
          </h2>

          <v-row justify="center">
            <div class="mb-16">

              <v-btn color="info" class="mx-1" @click="keyword()">
                <v-icon class="mr-2">mdi-magnify</v-icon>
                PALAVRA-CHAVE
              </v-btn>
              <v-btn color="info" class="mx-1" @click="dashboard()">
                <v-icon class="mr-2">mdi-chart-box</v-icon>
                ESTATÍSTICAS
              </v-btn>
              <!-- <v-btn class="mx-1" @click="about()">
                <v-icon class="mr-2">mdi-help-circle</v-icon>
                SOBRE NÓS
              </v-btn> -->

            </div>
            <!-- <a
              v-for="(next, i) in whatsNext"
              :key="i"
              :href="next.href"
              class="subheading mx-3"
              target="_blank"
            >
              {{ next.text }}
            </a> -->
          </v-row>
        </v-sheet>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',

    data: () => ({
      
    }),
  }
</script>
