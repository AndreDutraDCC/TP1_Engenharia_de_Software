<template>
  <v-sheet  color="primary" class="white--text pb-16">
    <v-row class="text-center align-center" justify="center" align="center">
      <v-col style="padding:0px !important;" cols="12" justify="center" align="center">
        <v-parallax src="@/assets/homem.jpg"> 
      <span style="font-size:80px; color: #FFF !important;" class="font-weight-bold">Estatísticas</span>
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
        <v-sheet color="accent" width="70%" rounded="xl" class="py-1 ml-16">
          <Chart chartType='doughnut' :responsive="true" title="Sentimentos Mais Escolhidos" align="center" :colors="coresSentimentos" :labels='labelSentimentos' :datasets='sentimentos' :setHeight='250' :setWidth='450' class="ma-4"/>
        </v-sheet>
      </v-col>
      <v-col cols="6" justify="center" align="center">
        <v-sheet color="accent"  width="70%" rounded="xl" class="py-1 mr-16">
        <Chart chartType='bar' :hideLegend="true" :responsive="true" title="Acessos na Última Semana" align="center" :colors="coresAcessos" :labels='labelAcessos' :datasets='acessos' :setHeight='250' :setWidth='450' class="ma-4"/>
        </v-sheet>
      </v-col>
      <v-col cols="12" justify="center" align="center">
        <v-sheet color="accent"  width="80%" rounded="xl" class="py-1">
        <Chart chartType='bar' :hideLegend="true" title="Termos Mais Buscados" align="center" :labels='palavras' :datasets='datasetPalavras' :setHeight='250' :setWidth='800' class="ma-4"/>
        </v-sheet>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<script>
  import axios from "axios"

  export default {
    name: 'Dashboard',

    components: {
      Chart: () => {return import("@/components/Chart/Chart.vue");}
    },

    data(){
      return {
          words: 10,
          dados: {},
          loading: true,
          sentimentos: [],
          labelAcessos: ["Sete dias atrás", "Seis dias atrás","Cinco dias atrás","Quatro dias atrás", "Três dias atrás","Dois dias atrás", "Um dia atrás"],
          coresAcessos: ["#911947", "#8E235C","#8B2D71","#883786","#84419A","#7D55C4","#7668ED"],
          labelSentimentos: ["Muito Positivo","Positivo","Neutro", "Negativo","Muito Negativo", "Misto"],
          coresSentimentos: ["#45A32E","#84BB61","#D1D9A5","#EC7E68","#E86348","#7668ED"],
      }
    },
    computed: {
      palavras(){
        let tratado = {}
        if(this.dados.pesquisas){
          Object.keys(this.dados.pesquisas).forEach((key) => {
            if(!tratado[this.dados.pesquisas[key]]){
              tratado[this.dados.pesquisas[key]] = 1
            }else{
              tratado[this.dados.pesquisas[key]] += 1
            }
          })
          console.log(tratado)
          let p = this.biggest_Ns(this.words, tratado)
          console.log(p)
          let k = []
          p.forEach((x) => {
            k.push(x[0])
          })
          return k
        }else{
          return []
        }
      },
      datasetPalavras(){
        let result
        let tratado = {}
        if(this.dados.pesquisas){
          Object.keys(this.dados.pesquisas).forEach((key) => {
            if(!tratado[this.dados.pesquisas[key]]){
              tratado[this.dados.pesquisas[key]] = 1
            }else{
              tratado[this.dados.pesquisas[key]] += 1
            }
          })
          let p = this.biggest_Ns(this.words, tratado)
          let k = []
          p.forEach((x) => {
            k.push(x[1])
          })
          result = k
        }else{
          result = []
        }
        return [{ 
          label: "Quantidade de Buscas", 
          data: result
        }]
      },
      acessos(){
      // if(this.dados.acessos){
        let atual = (new Date()).getTime()
        let dates = [0, 0, 0, 0, 0, 0, 0]
        // console.log(this.dados)
          Object.keys(this.dados.acessos).forEach((key) => {
            let x = this.dados.acessos[key];
            let dist = (atual-x)/1000
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
        // }
        return [{
            label: 'Quantidade de Acessos',
            data: dates,
        }]
      },
    },
    methods: {
      call(){
        console.log(this.dados.pesquisas)
      },
      biggest_Ns(N, obj) {
        let l = [];
        Object.keys(obj).forEach((key) => {
          l.push([key,obj[key]]);
        })
        l.sort((a,b) => {return b[1] - a[1]})
        return l.slice(0,N)
      }
    },
    async mounted() {
      // console.log("UIUI")
        let obj = await axios.get("https://listify-es-default-rtdb.firebaseio.com/data.json")
        this.dados = obj.data
        let dataset = {
          label: "Sentimentos",
          data: [],
        }
        let tratado = {}
        // console.log("Tratar sentimentos")
        // console.log(this.dados.sentimentos)
        // if(!!this.dados.sentimentos){
          Object.keys(this.dados.sentimentos).forEach((key) => {
            if(!tratado[this.dados.sentimentos[key]]){
              tratado[this.dados.sentimentos[key]] = 1
            }else{
              tratado[this.dados.sentimentos[key]] += 1
            }
          })
        // }
        // console.log("Tratado")
        // console.log(tratado)
        if(!!this.dados.sentimentos){
          dataset.data.push(tratado.muito_feliz)
          dataset.data.push(tratado.feliz)
          dataset.data.push(tratado.neutro)
          dataset.data.push(tratado.triste)
          dataset.data.push(tratado.muito_triste)
          dataset.data.push(tratado.misto)
        }
        this.sentimentos = [dataset]
    },

  }
</script>
