<template>
    <v-sheet color="primary" class="ma-1" rounded="xl">

    <v-list-item>
        
        <!-- <v-list-item-avatar> -->
        <v-avatar
            :color="item.color"
            class="white--text ma-2"
            size="80"
        >
            <v-img
            :src="item.album_img_url.url"
            alt="Album"
        ></v-img>
        </v-avatar>
        <!-- </v-list-item-avatar> -->

        <v-list-item-content class="py-2 white--text">
        <v-list-item-title>{{ item.track_name }}</v-list-item-title>
        <v-list-item-subtitle class="white--text" > {{artists}} </v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action>
            <v-row>
                <v-col class="ma-n2">
                    <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn
                            :color="feelingColor"
                            fab
                            dark
                            small
                            v-bind="attrs"
                            v-on="on"
                        >
                            <v-icon>{{feeling.icon}}</v-icon>
                        </v-btn>
                    </template>
                    <span>Sentimento: {{feeling.feel}}</span><br>
                    <div v-if="!item.sentiment.message">
                        <span>Pontuação: {{Number((item.sentiment.score).toFixed(3))}}</span><br>
                        <span>Variação: {{item.sentiment.magnitude}}</span>
                    </div>
                    </v-tooltip>
                </v-col>
                <v-col class="ma-n2">
                    <v-btn fab small color="info" @click.prevent="playSound(item.preview_url)">
                        <v-icon >{{soundState == "paused" ? "mdi-play" : "mdi-pause"}}</v-icon>
                    </v-btn>
                </v-col>
                <v-col class="ma-n2">
                    <v-btn fab small color="secondary" @click="open()">
                        <v-icon >mdi-spotify</v-icon>
                    </v-btn>
                </v-col>
                <v-col class="ma-n2">
                    <v-btn v-if="!playlist" fab small color="success" @click="add()">
                        <v-icon >mdi-plus</v-icon>
                    </v-btn>
                    <v-btn v-if="playlist" fab small color="error" @click="remove()">
                        <v-icon >mdi-minus</v-icon>
                    </v-btn>
                </v-col>
            </v-row>
        <!-- <v-btn
            depressed
            small
        >
            View User

            <v-icon
            color="orange darken-4"
            right
            >
            mdi-open-in-new
            </v-icon>
        </v-btn> -->
        </v-list-item-action>
    </v-list-item>
    </v-sheet>
</template>

<script>

export default {
    name: 'Music',
    props: ["music", "playlist"],

    data: () => ({
        soundState: "paused",
        soundData: "",
        defaultMusic: {
            "track_name": "Ronson Princess",
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
                "score": -0.20000000298023224,
                "magnitude": 3.0
                }
            },
    }),

    computed: {
        feelingColor(){
            if(!this.item.sentiment.message){
                let s = (this.item.sentiment.score + 1)/2
                s = s*100
                s = Math.max(s, 1)
                return "hsl(" + s + ", 80%, 45%)";
            }else{
                return "#AAA"
            }
        },
        feeling(){
            if(!!this.item.sentiment.message){
                return {
                    icon: "mdi-help",
                    feel: "Desconhecido"
                }
            }else if(this.item.sentiment.score >= 0.7){
                return {
                    icon: "mdi-emoticon-excited",
                    feel: "Muito Positivo"
                }
            }else if(this.item.sentiment.score >= 0.3){
                return {
                    icon: "mdi-emoticon-happy",
                    feel: "Positivo"
                }
            }else if(this.item.sentiment.score > -0.3){
                if(this.item.sentiment.magnitude > 2){
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
            }else if(this.item.sentiment.score > -0.7){
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
        item(){
            return !!this.music ? this.music : this.defaultMusic
        },
        artists(){
            if(this.item.artists_involved.length > 1){
                let names = ""
                this.item.artists_involved.forEach((x) => {
                    if(names.length > 0){
                        names = names + ", "
                    }
                    names = names + this.item.artists_involved
                })
                return names
            }else if(this.item.artists_involved.length == 1){
                return this.item.artists_involved[0]
            }
        }
    },

    methods: {
        add(){
            this.$emit("add", this.item)
        },
        remove(){
            this.$emit("remove", this.item)
        },
        open(){
            window.open(this.item.external_urls.spotify, '_blank')
        },
        stopAll(obj){
            if(obj != this.item){
                if(this.soundData != ""){
                    // console.log(this.soundData)
                    if(this.soundState == "playing"){
                        this.soundData.pause()
                        this.soundState = "paused"
                    }
                    this.soundData.currentTime = 0
                    this.soundData = ""
                }
            }
        },
        playSound(sound) {
            // this.item.sentiment.score += 0.1
            if(this.soundData == ""){
                if(sound) {
                    var audio = new Audio(sound);
                    audio.play();
                    audio.volume = 0.08
                    audio.onended = ()=>{this.soundState = "paused"}
                    this.soundData = audio
                    this.soundState = "playing"
                    this.$emit("playing", this.item)
                    // console.log("a")
                }
            }else{
                if(this.soundData.ended){
                    this.soundData = ""
                    this.playSound(sound)
                    // console.log("b")
                }else{
                    if(this.soundData.paused){
                        this.soundData.play();
                        this.soundData.volume = 0.08
                        this.soundState = "playing"
                        this.$emit("playing", this.item)
                        // console.log("c")
                    }else{
                        this.soundData.pause()
                        this.soundState = "paused"
                        // console.log("d")
                    }
                }
            }
        },
    },
}
</script>

<style scoped>
.v-avatar{
    border-radius: 4px !important;
}
</style>