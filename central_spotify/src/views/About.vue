<template>
  <div class="about" color="#0FF" >
    <v-parallax justify="center" align="center"  src="@/assets/computer.jpg">
      <span style="font-size:80px;" class="font-weight-bold">Sobre o Listify</span>
    </v-parallax>
    <v-row justify="center" align="center">
      <v-col justify="center" align="center">
        <v-sheet class="white--text py-8 secondary">
          <h3 class="my-6">
            O Projeto faz parte do Trabalho Prático 1 de Engenharia de Software, sendo desenvolvido pelos alunos: <br> André Luiz, Antônio Isaac, Emanuel Juliano e Marcos Vinicius.
          </h3>
        </v-sheet>
        <v-sheet class="white--text py-4" color="#101010">
          <v-carousel
            cycle
            height="400"
            hide-delimiter-background
            show-arrows-on-hover
          >
            <v-carousel-item
              v-for="(slide, i) in slides"
              :key="i"
            >
              <v-sheet
                color="#0000"
                height="100%"
              >
                <v-row
                  class="fill-height"
                  align="center"
                  justify="center"
                >
                <v-card
                  class="py-6"
                  max-width="434"
                  elevation="20"
                  rounded="xl"
                  color="primary"
                >
                    <v-row
                      align="end"
                      class="fill-height"
                    >
                      <v-col
                        align-self="start"
                        class="pa-0"
                        cols="12"
                      >
                        <v-avatar
                          class="profile"
                          color="grey"
                          size="164"
                        >
                          <v-img :src="images[i]"></v-img>
                        </v-avatar>
                      </v-col>
                      <v-col class="py-0">
                        <v-list-item
                          color="rgba(0, 0, 0, .4)"
                          dark
                        >
                          <v-list-item-content>
                            <v-list-item-title class="text-h6">
                            <v-btn fab small class="ml-n8 mr-2" :href="git[i]"><v-icon>mdi-github</v-icon></v-btn>
                              {{slides[i]}}
                            </v-list-item-title>
                            <v-list-item-subtitle>{{func[i]}}</v-list-item-subtitle>
                            <div class="text-justify px-2 pt-2">
                              <p5>{{texto[i]}}</p5>
                            </div>
                          </v-list-item-content>
                        </v-list-item>
                      </v-col>
                    </v-row>
                </v-card>
                  <!-- <v-avatar>
                    <img
                      src="https://cdn.vuetifyjs.com/images/john.jpg"
                      height="100px"
                    >
                  </v-avatar>
                  <div class="text-h2">
                    {{ slide }} 
                  </div> -->
                </v-row>
              </v-sheet>
            </v-carousel-item>
          </v-carousel>
        </v-sheet>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        colors: [
          'primary',
          'primary',
          'primary',
          'primary',
        ],
        slides: [
          'André Dutra',
          'Isaac Lima',
          'Emanuel Juliano',
          'Marcos Pacheco',
        ],
        func: [
          'Back-end',
          'Back-end',
          'Front-end',
          'Front-end',
        ],
        images: [
          'https://firebasestorage.googleapis.com/v0/b/listify-es.appspot.com/o/andre.jpg?alt=media&token=376a645a-2425-4a79-bb82-6ba315b8e80e',
          'https://firebasestorage.googleapis.com/v0/b/listify-es.appspot.com/o/isaac.jpg?alt=media&token=b073ffc8-7b35-41eb-92a2-955327f48158',
          'https://firebasestorage.googleapis.com/v0/b/listify-es.appspot.com/o/emanuel.jpg?alt=media&token=c32d6ab1-41d1-44b9-aa23-6783b5ba22cb',
          'https://firebasestorage.googleapis.com/v0/b/listify-es.appspot.com/o/marcos.jpg?alt=media&token=6b5a460b-8da0-496d-9517-1b6e07ae3360',
        ],
        git: [
          'https://github.com/AndreDutraDCC',
          'https://github.com/isaacs4m',
          'https://github.com/emanueljuliano',
          'https://github.com/MVCP1',
        ],
        texto: [
          "André Dutra é o responsável pela criação e manutenção do Banco de Dados. Criou uma maneira de armazenar dados de acesso do site para que possam ser mostrados.",
          "Isaac Lima é o responsável pelas APIs utilizadas pelo site. Isso envolve a API de busca do Spotify, busca de letra das músicas, bem como análise de setimento.",
          "Emanuel Juliano é o responsável pelo Design das Telas. Utilizou Figma para construir a roupagem do Site, trabalhando de forma direta com Marcos na criação das telas.",
          "Marcos Pacheco é o responsável pela criação das páginas. Também implementou as funcionalidades do site utilisando as APIs e o Banco de Dados.",
        ]
      }
    },
  }
</script>