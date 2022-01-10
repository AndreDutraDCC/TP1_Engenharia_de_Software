<template>
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

        <v-list-item-content class="py-2">
        <v-list-item-title>{{ item.track_name }}</v-list-item-title>
        <v-list-item-subtitle > {{artists}} </v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action>
        <v-btn
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
        </v-btn>
        </v-list-item-action>
    </v-list-item>
</template>

<script>

export default {
    name: 'Music',
    props: ["music"],

    data: () => ({
        defaultMusic: {
            color: "#faf",
            fullName: "Fulano Tal",
            initials: "F T",
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
    },
}
</script>

<style scoped>
.v-avatar{
    border-radius: 4px !important;
}
</style>