<template>
  <v-sheet  color="primary" class="white--text pb-16">
    <v-row class="text-center align-center" justify="center" align="center">
      <v-col style="padding:0px !important;" cols="12" justify="center" align="center">
        <v-parallax src="@/assets/homem.jpg"> 
      <span style="font-size:80px;" class="font-weight-bold">Dashboard</span>
        </v-parallax>
      </v-col>
      <v-col cols="12" class="mt-n16" justify="center" align="center">
        <v-card width="850px" color="secondary" class="pa-6 my-2 white--text" border-radius="20px" elevation="5">
          <h1 class="font-weight-bold">
            Dados coletados dos usuários do site
          </h1>
        </v-card>
      </v-col>
      <v-col cols="6" justify="center" align="center">
        <v-sheet color="accent" width="80%" rounded="xl" class="py-1">
          {{sentimentos}}
          <Chart chartType='doughnut' title="Sentimentos Mais Escolhidos" align="center" :colors="coresSentimentos" :labels='labelSentimentos' :datasets='sentimentos' :setHeight='250' :setWidth='500' class="ma-4"/>
        </v-sheet>
      </v-col>
      <v-col cols="6" justify="center" align="center">
        <v-sheet color="accent"  width="80%" rounded="xl" class="py-1">
          {{acessos}}
        <Chart chartType='bar' title="Acessos na Última Semana" align="center" :colors="coresAcessos" :labels='labelAcessos' :datasets='acessos' :setHeight='250' :setWidth='500' class="ma-4"/>
        </v-sheet>
      </v-col>
      <v-col cols="12" justify="center" align="center">
        <v-sheet color="accent"  width="80%" rounded="xl" class="py-1">
        <!-- <Chart chartType='bar' title="Palavras Mais Buscadas" align="center" :labels='labels' :datasets='dataset' :setHeight='250' :setWidth='800' class="ma-4"/> -->
        </v-sheet>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
  // import {obter_colecao} from "@/services/access_database"
  import axios from "axios"

  export default {
    name: 'Dashboard',

    components: {
      Chart: () => {return import("@/components/Chart/Chart.vue");}
    },

    data(){
      return {
          dados: {},
          loading: true,
          sentimentos: [{
            label: 'Quantidade de Acessos',
            data: [1, 2, 3, 4, 5, 6],
        }],
          acessos: [{
            label: 'Quantidade de Acessos',
            data: [1, 2, 3, 4, 5, 6, 10],
        }],
          labelAcessos: ["Sete dias atrás", "Seis dias atrás","Cinco dias atrás","Quatro dias atrás", "Três dias atrás","Dois dias atrás", "Um dia atrás"],
          coresAcessos: ["#911947", "#8E235C","#8B2D71","#883786","#84419A","#7D55C4","#7668ED"],
          labelSentimentos: ["Muito Positivo","Positivo","Neutro", "Negativo","Muito Negativo", "Misto"],
          coresSentimentos: ["#45A32E","#84BB61","#D1D9A5","#EC7E68","#E86348","#7668ED"],
          dataset: [{
            label: 'Faturamento',
            data: [25,1,2],
        },{
            label: 'Faturamento2',
            data: [5,10,25],
        }],
      }
    },
    computed: {
      // acessos(){
      //   let atual = (new Date()).getTime()
      //   let dates = [0, 0, 0, 0, 0, 0, 0]
      //   console.log(this.dados)
      //   Object.keys(this.dados.acessos).forEach((key) => {
      //     let x = this.dados.acessos[key];
      //     // console.log(atual)
      //     // console.log(x)
      //     // console.log(
      //     let dist = (atual-x)/1000
      //       // use val
      //   // });
      //   // this.dados.acessos.forEach((x) => {
      //     if(dist <= 1*60*60*24){
      //       dates[6] += 1
      //     }else if(dist <= 2*60*60*24){
      //       dates[5] += 1
      //     }else if(dist <= 3*60*60*24){
      //       dates[4] += 1
      //     }else if(dist <= 4*60*60*24){
      //       dates[3] += 1
      //     }else if(dist <= 5*60*60*24){
      //       dates[2] += 1
      //     }else if(dist <= 6*60*60*24){
      //       dates[1] += 1
      //     }else if(dist <= 7*60*60*24){
      //       dates[0] += 1
      //     }
      //   })
      //   return [{
      //       label: 'Quantidade de Acessos',
      //       data: dates,
      //   }]
      // },
      // sentimentos(){
      //   let dataset = {
      //     label: "Sentimentos",
      //     data: [],
      //   }
      //   if(!!this.dados.sentimentos){
      //     dataset.data.push(this.dados.sentimentos.muito_feliz)
      //     dataset.data.push(this.dados.sentimentos.feliz)
      //     dataset.data.push(this.dados.sentimentos.neutro)
      //     dataset.data.push(this.dados.sentimentos.triste)
      //     dataset.data.push(this.dados.sentimentos.muito_triste)
      //     dataset.data.push(this.dados.sentimentos.misto)
      //   }
      //   // console.log([dataset])
      //   return [dataset]
      //   // return [ { "label": "Sentimentos", "data": [ 6, 7, 2, 7, 1, 2 ] } ]
      // }
    },
    methods: {
      // async base(){
      //   let obj = await axios.get("https://listify-es-default-rtdb.firebaseio.com/data.json")
      //   obj = obj.data
      //   // obj = obter_colecao();
      //   console.log(obj)
      // }
    },
    async mounted() {
        let obj = await axios.get("https://listify-es-default-rtdb.firebaseio.com/data.json")
        this.dados = obj.data
        let dataset = {
          label: "Sentimentos",
          data: [],
        }
        if(!!this.dados.sentimentos){
          dataset.data.push(this.dados.sentimentos.muito_feliz)
          dataset.data.push(this.dados.sentimentos.feliz)
          dataset.data.push(this.dados.sentimentos.neutro)
          dataset.data.push(this.dados.sentimentos.triste)
          dataset.data.push(this.dados.sentimentos.muito_triste)
          dataset.data.push(this.dados.sentimentos.misto)
        }
        this.sentimentos = [dataset]
        
        let atual = (new Date()).getTime()
        let dates = [0, 0, 0, 0, 0, 0, 0]
        Object.keys(this.dados.acessos).forEach((key) => {
          let x = this.dados.acessos[key];
          let dist = (atual-x)/1000
          console.log(dist)
          if(dist <= 1*60*60*24){
            dates[6] += 1
          }else if(dist <= 2*60*60*24){
            dates[5] += 1
          }else if(dist <= 3*60*60*24){
            dates[4] += 1
          }else if(dist <= 4*60*60*24){
            dates[3] += 1
          }else if(dist <= 5*60*60*24){
            dates[2] += 1
          }else if(dist <= 6*60*60*24){
            dates[1] += 1
          }else if(dist <= 7*60*60*24){
            dates[0] += 1
          }
        })
        this.acessos = [{
            label: 'Quantidade de Acessos',
            data: dates,
        }]
    },

  }
</script>
