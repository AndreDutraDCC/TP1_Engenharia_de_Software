<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      elevation="15"
    >
      <div class="d-flex align-center" style="cursor:pointer" @click="clickLogo">
        <v-img
          alt="Listify Logo"
          class="shrink mr-2"
          src="@/assets/logo.png"
          contain
          transition="scale-transition"
          width="40"
        />

        <!-- <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        /> -->
        <v-img
          alt="Listify Text"
          class="shrink mx-2"
          src="@/assets/logoNomeWhite.png"
          contain
          transition="scale-transition"
          width="100"
        />
        <!-- <h2 class="pl-2">Listify</h2>  -->
        <h5 class="pt-1 pl-3"> Musiquinhas Top </h5>
      </div>

      <v-spacer></v-spacer>

      <div>
        <v-btn text class="mx-1" @click="keyword()">
          <v-icon class="mr-2">mdi-magnify</v-icon>
          PALAVRA-CHAVE
        </v-btn>
        <v-btn text class="mx-1" @click="dashboard()">
          <v-icon class="mr-2">mdi-chart-box</v-icon>
          ESTATÍSTICAS
        </v-btn>
        <v-btn text class="mx-1" @click="about()">
          <v-icon class="mr-2">mdi-help-circle</v-icon>
          SOBRE NÓS
        </v-btn>
      </div>

      <!-- <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn> -->
    </v-app-bar>

    <v-main>
      <!-- <v-sheet color="secondary"> -->
        <router-view/>
        <!-- <Playlist/> -->
      <!-- </v-sheet> -->
    </v-main>
    
    <v-footer color="primary">
      <v-card flat tile width="100%" class="primary text-center">

        <v-divider class="white"></v-divider>

        <v-card-text class="white--text">
          <v-btn
            class="mx-4 my-n7 white--text"
            icon
            href="https://github.com/AndreDutraDCC/TP1_Engenharia_de_Software"
          >
            <v-icon size="24px">
              mdi-github
            </v-icon>
          </v-btn>
          {{ new Date().getFullYear() }} — <strong> Musiquinhas Top </strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
import Playlist from '@/components/Playlist'

export default {
  name: 'App',

  components: {
    Playlist,
  },

  data: () => ({
    //
  }),

  methods: {
    clickLogo(){
      this.$router.push('/')
      console.log("click logo")
    },
    keyword(){
      this.$router.push('/keyword')
      console.log("click keyword")
    },
    dashboard(){
      this.$router.push('/dashboard')
      console.log("click dashboard")
    },
    about(){
      this.$router.push('/about')
      console.log("click about")
    }
  }
};
</script>
