<template>     
  <v-card
    class="mx-auto"
    max-width="500"
    elevation="20"
    color="accent"
  >
    <v-card-title class="white--text primary darken-4">
     <v-icon class="white--text mx-2">{{playlist ? "mdi-music" : "mdi-magnify"}}</v-icon> {{playlist ? "Playlist" : "Resultado"}}

      <v-spacer></v-spacer>
        <v-tooltip left>
        <template v-slot:activator="{ on, attrs }">
            <v-btn
                color="white"
                class="text--primary"
                fab
                small
                v-bind="attrs"
                v-on="on"
                @click="doAll()"
            >
                <v-icon> {{playlist ? "mdi-minus" : "mdi-plus"}}</v-icon>
            </v-btn>
        </template>
        <span> {{playlist ? "Remover Todas" : "Adicionar Todas"}}</span>
        </v-tooltip>

    </v-card-title>
    <v-card-text class="pt-4" :color="feelingColor">
        <v-tooltip bottom v-if="this.lista.length > 0">
            <template v-slot:activator="{ on, attrs }">
                <v-btn
                    :color="feelingColor"
                    fab
                    dark
                    small
                    v-bind="attrs"
                    v-on="on"
                    class="mx-2"
                >
                    <v-icon>{{feeling.icon}}</v-icon>
                </v-btn>
            </template>
            <span>Sentimento: {{feeling.feel}}</span><br>
            <div v-if="!media.message">
                <span>Pontuação: {{Number((media.total).toFixed(3))}}</span><br>
                <span>Variação: {{Number((media.vari).toFixed(3))}}</span>
            </div>
        </v-tooltip>
      {{texto}}
    </v-card-text>

    <v-divider></v-divider>

    <v-virtual-scroll
        ref="mus"
      :items="lista"
      :item-height="100"
      height="500"
    >
    <template v-slot:default="{ item }" >
        <Music :music="item" :playlist="playlist" @playing="stopAll" @add="add" @remove="remove"/>
        <!-- <Music :music="item"/> -->
    </template>
    </v-virtual-scroll>
  </v-card>
</template>

<script>
import Music from '@/components/Music'

export default {
    name: 'MusicList',
    props: ["playlist", "musics"],
    components: {
      Music,
    },
    data: () => ({
    }),

    computed: {
        lista(){
            return !!this.musics ? this.musics : []
        },
        media(){
            let m = 0
            let v = 0
            let total = 0
            this.lista.forEach((x) => {
                if(!x.sentiment.message){
                    total += 1
                    m += x.sentiment.score
                    v += x.sentiment.magnitude
                }
            })
            return total > 0 ? {
                total: m/total,
                vari: v/total,
            } : {message: "desconhecido"}
        },
        feelingColor(){
            if(!this.media.message){
                let s = (this.media.total + 1)/2
                s = s*100
                s = Math.max(s, 1)
                return "hsl(" + s + ", 80%, 45%)";
            }else{
                return "#AAA"
            }
        },
        feeling(){
            if(!!this.media.message){
                return {
                    icon: "mdi-help",
                    feel: "Desconhecido"
                }
            }else if(this.media.total >= 0.7){
                return {
                    icon: "mdi-emoticon-excited",
                    feel: "Muito Positivo"
                }
            }else if(this.media.total >= 0.3){
                return {
                    icon: "mdi-emoticon-happy",
                    feel: "Positivo"
                }
            }else if(this.media.total > -0.3){
                if(this.media.vari > 2){
                    return {
                        icon: "mdi-emoticon-cool",
                         feel: "Misto"
                    }  
                }else{
                    return {
                        icon: "mdi-emoticon-neutral",
                         feel: "Neutro"
                    }   
                }
            }else if(this.media.total > -0.7){
                return {
                    icon: "mdi-emoticon-confused",
                    feel: "Negativo"
                }
            }else{
                return {
                    icon: "mdi-emoticon-frown",
                    feel: "Muito Negativo"
                }
            }
        },
        texto(){
            if(this.lista.length > 0){
                return "Sentimento Médio Total: " + this.feeling.feel
            }else{
                return this.playlist ? "Adicione músicas encontradas aqui e monte sua playlist" : "Busque por músicas para encontrá-las aqui"
            }
        }
    },

    methods: {
      stopAll(obj){
        this.$refs.mus.$children.forEach((x) => {
              x.stopAll(obj)
          })
      },
      add(obj){
        this.$emit("add", obj)
      },
      remove(obj){
        this.$emit("remove", obj)
      },
      doAll(){
        if(this.playlist){
            this.$emit("removeAll")
        }else{
            this.$emit("addAll")
        }
      }
    },
}
</script>

<style>

</style>