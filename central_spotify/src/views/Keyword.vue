<template>
  <v-sheet  color="primary" class="white--text pb-16">
    <v-row class="text-center align-center" justify="center" align="center">
      <v-col style="padding:0px !important;" cols="12" justify="center" align="center">
          <v-parallax src="@/assets/dancing-woman-small2.jpg"> 
          </v-parallax>
      </v-col>
      <v-col cols="12" class="mt-n16" justify="center" align="center">

        <v-card width="850px" color="secondary" class="pa-6 my-2 white--text" border-radius="20px" elevation="5">
          <h1 class="font-weight-bold">
            Encontre uma playlist que é a sua cara!
          </h1>
        </v-card>
      </v-col>

      <v-col
        class="mb-5"
        cols="12"
         justify="center" align="center"
      >
        <v-sheet
          color="secondary"
          elevation="15"
          rounded="xl"
          width="50%"
          class="pa-6 my-2 white--text"
          >

          <h2 class="font-weight-bold mb-8">
            Experimente:
          </h2>
          <v-text-field 
            color="white"
            dark
            class="" 
            v-model="text" 
            label="Palavras chave"
            outlined
            clearable>
          </v-text-field>
          <v-btn color="success" :loading="loading" @click="buscar()">
            Buscar Músicas
          </v-btn>
        </v-sheet>
      </v-col>
      <v-col cols="6">
          <MusicList :playlist="false" @add="add" @addAll="addAll" :musics="busca" />
      </v-col>
      <v-col cols="6">
          <MusicList :playlist="true" @remove="remove" @removeAll="removeAll" :musics="playlist" />
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
  import MusicList from '@/components/MusicList.vue'
  import axios from "axios"
  // import { getDatabase, ref, onValue } from "firebase/database";

  // const db = getDatabase();

  export default {
    name: 'Home',

    components: {
      MusicList,
    },

    data() {
      return {
        text: "",
        busca: [],
        playlist: [],
        loading: false,
        tracks: [{
            "track_name": "AAAs",
            "artists_involved": [
                "Clarence James"
            ],
            "album_img_url": {
                "height": 640,
                "url":
                "https://i.scdn.co/image/ab67616d0000b273f04d1a966bad353c07f12115",
                "width": 640
            },
            "external_urls": {
                "spotify":
                "https://o1pen.spotify.com/track/2Xk3MunfpZwHSJktWNhRbz"
            },
            "preview_url": "https://p.scdn.co/mp3-preview/e08a796b1ca940c872e6d85a9a3634b31ff0185e?cid=3daeddc98fd94f57aed5e2e65c3b385f",
            "sentiment": {
                "score": -0.20000000298023224,
                "magnitude": 3.0
                }
            },{
            "track_name": "BBBBs",
            "artists_involved": [
                "Clarence James"
            ],
            "album_img_url": {
                "height": 640,
                "url":
                "https://i.scdn.co/image/ab67616d0000b273f04d1a966bad353c07f12115",
                "width": 640
            },
            "external_urls": {
                "spotify":
                "https://op2en.spotify.com/track/2Xk3MunfpZwHSJktWNhRbz"
            },
            "preview_url": "https://p.scdn.co/mp3-preview/e08a796b1ca940c872e6d85a9a3634b31ff0185e?cid=3daeddc98fd94f57aed5e2e65c3b385f",
            "sentiment": {
                "score": -0.20000000298023224,
                "magnitude": 3.0
                }
            },{
            "track_name": "CCCs",
            "artists_involved": [
                "Clarence James"
            ],
            "album_img_url": {
                "height": 640,
                "url":
                "https://i.scdn.co/image/ab67616d0000b273f04d1a966bad353c07f12115",
                "width": 640
            },
            "external_urls": {
                "spotify":
                "https://open.spotify.com/track/2Xk3MunfpZwHSJktWNhRbz"
            },
            "preview_url": "https://p.scdn.co/mp3-preview/e08a796b1ca940c872e6d85a9a3634b31ff0185e?cid=3daeddc98fd94f57aed5e2e65c3b385f",
            "sentiment": {
                "message": "Hmmm não tem"
                }
            },
        ]
      };
    },

    methods: {
      feel(score, vari){
        if(score >= 0.7){
                return "muito_feliz"
            }else if(score >= 0.3){
                return "feliz"
            }else if(score > -0.3){
                if(vari > 2){
                    return "misto"
                }else{
                    return "neutro"
                }
            }else if(score > -0.7){
                return "triste"
            }else{
                return "muito_triste"
            }
        },
      // async teste(){
      //   const db = this.$database
      //   console.log(db)
      //   let l = await db.ref('data').once('value')
      //   console.log(l)
      //   // const starCountRef = ref(db, 'data');
      //   // console.log(starCountRef)
      // // onValue(starCountRef, (snapshot) => {
      // //   const data = snapshot.val();
      // //   updateStarCount(postElement, data);
      // // });
      // },
      async buscar() {
        this.loading = true
        try {
          await axios.post("https://listify-es-default-rtdb.firebaseio.com/data/pesquisas.json", JSON.stringify(this.text))
          let key = {
            keyword: this.text
          }
          let result = await axios.post("https://6fcfz9bcw4.execute-api.us-east-1.amazonaws.com/", JSON.stringify(key))
          this.busca = result.data.track_list
          this.loading = false
        } catch (error) {
          console.log("Erro: ", error)
          this.loading = false
        }
        this.loading = false
        // console.log(result)
      },
      async add(obj){
        if(!obj.sentiment.message){
          await axios.post("https://listify-es-default-rtdb.firebaseio.com/data/sentimentos.json",  JSON.stringify(this.feel(obj.sentiment.score, obj.sentiment.magnitude)))
        }
        this.busca = this.busca.filter((x) => { return x.external_urls.spotify != obj.external_urls.spotify }); 
        if(this.playlist.filter((x) => { return x.external_urls.spotify == obj.external_urls.spotify}).length == 0){
          this.playlist.push(obj)
        }
      },
      remove(obj){
        this.playlist = this.playlist.filter((x) => { return x.external_urls.spotify != obj.external_urls.spotify }); 
        // this.playlist.push(obj)
      },
      addAll(){
        this.busca.forEach((x) => {
          this.add(x)
        })
      },
      removeAll(){
        this.playlist.forEach((x) => {
          this.remove(x)
        })
      }
    },
  }
</script>
