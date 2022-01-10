<template>
  <v-sheet color="primary" class="white--text">
    <v-row class="text-center align-center" justify="center" align="center">
      <v-col style="padding:0px !important;" cols="12" justify="center" align="center">
        <v-parallax height="500" src="@/assets/party-xsmall.jpg"> 
        <v-row justify="center" align="center">
          <v-col justify="center" align="center">
            <v-sheet width="400px" height="350px" color="#FFF0" elevation="0" style="border-radius:40px !important" >
              <v-img
                class="my-3"
                contain
                height="350"
                :src="require('../assets/logoComNomeWhite.png')"
              ></v-img>
            </v-sheet>
          </v-col>
        </v-row>
        </v-parallax>

        <!-- <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        /> -->
      </v-col >

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
      <v-col cols="12" class="mt-n16" justify="center" align="center">

        <v-card width="80%" rounded="xl" color="secondary" class="white--text pa-6 mb-8" border-radius="20px" elevation="5">
          <h2 class="font-weight-bold mb-6">
          O Listify é um website que funciona como uma central de dados musicais do spotify!
          </h2>
          <v-sheet width="70%" color="secondary"  class="white--text">
            <ul class="text-justify">
              <li>Crie automaticamente, a partir de palavras-chave, playlists com músicas compatíveis. </li>
              <li>Verifique o sentimento geral das músicas de uma playlist, e entenda qual é a sua vibe preferida.</li>
              <li>Olhe as estatísticas do site para ver quais são as musicas mais buscadas do momento.</li>
            </ul> 
          </v-sheet>
            <!-- O Listify é um website que funciona como uma central de dados musicais do spotify! 
            <br>
            Você pode criar automaticamente, a partir de palavras-chave, playlists com músicas compatíveis, permitindo criar playlists para eventos específicos, e verificar o sentimento geral das músicas. 
            <br>
            Também existe a opção de olhar as estatísticas do site e ver quais são as musicas mais buscadas do momento
            <br> -->
        </v-card>
      </v-col>

      <v-col
        class="mb-5"
        cols="12"
         justify="center" align="center"
      >
        <v-sheet
          color="secondary"
          elevation="20"
          rounded="xl"
          height="150"
          width="50%"
          class="py-6 my-2 white--text"
          >

          <h2 class="headline font-weight-bold mb-8">
            Experimente:
          </h2>

          <v-row justify="center">
            <div class="mb-16">

              <v-btn color="success" class="mx-4" @click="keyword()">
                <v-icon class="mr-2">mdi-magnify</v-icon>
                PALAVRA-CHAVE
              </v-btn>
              <v-btn color="success" class="mx-4" @click="dashboard()">
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
        <h5 class="my-6">
          O Projeto faz parte do Trabalho Prático 1 de Engenharia de Software, sendo desenvolvido pelos alunos André Luiz, Antônio Isaac, Emanuel Juliano e Marcos Vinicius.
        </h5>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
  export default {
    name: 'HelloWorld',

    data: () => ({
      
      }),
  }
</script>
