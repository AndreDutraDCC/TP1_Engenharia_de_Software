<template>
    <v-row>
        <v-col cols="6" xl="3" lg="3" md="6" sm="6" xs="6">
            <v-btn color='secondary' text @click="lastPage()" :disabled="page == 1">ANTERIOR</v-btn>
        </v-col>
        <v-spacer class="hidden-md-and-down"></v-spacer>
        <v-col cols="3"  class="hidden-md-and-down">
            <v-btn v-for="i in pages" :key="i" :disabled="i > page" color="primary" @click="goPage(i)" fab x-small elevation="0" :class="page == i ? 'controler' : 'controler notThis'" ></v-btn>
        </v-col>
        <v-spacer class="hidden-md-and-down"></v-spacer>
        <v-col class="ml-auto" cols="6" xl="3" lg="3"  md="6" sm="6" xs="6">
            <v-btn v-if="page !== pages" color='info' text :disabled="!allowNext" @click="nextPage()">PRÓXIMA</v-btn>
            <v-btn v-else color='info' text :disabled="!allowNext" @click="nextPage()">{{lastPageText}}</v-btn>
        </v-col>
    </v-row>
</template>
<script>
export default {
    name: 'pageControler',
    props: ['pages', 'allowNext', 'lastPageText'],
    data(){
        return {
            page: 1
        }
    },
    watch: {
        page(){
            this.$emit('input', this.page)
        }
    },
    methods: {
        nextPage(){
            window.scrollTo(0,0);
            if(this.page!==this.pages){
                this.page++
            }else{
                this.$emit('finish')
            }
        },
        lastPage(){
            window.scrollTo(0,0);
            this.page--
        },
        goPage(page){
            window.scrollTo(0,0);
            this.page = page
        }
    }
}
</script>
<style lang="scss">
    .controler{
        transform: scale(0.5);
        border: 2px solid #2A335D;
    }
    .notThis{
        background-color: rgba(0,0,0,0);
    }
</style>