<template>
  <div>
    <!-- <Chart/> -->
    <Chart chartType='bar' align="center" :labels='labels' :datasets='dataset' :setHeight='250' :setWidth='500' class="ma-4"/>
    <v-bnt @click="base">
      Hm
    </v-bnt>
  </div>
</template>

<script>
  // import {obter_colecao} from "@/services/access_database"

  export default {
    name: 'Dashboard',

    components: {
      Chart: () => {return import("@/components/Chart/Chart.vue");}
    },

    data(){
      return {
          labels: ["TesteA","TestaeA","TeaaateA"],
          dataset: [{
            label: 'Faturamento',
            data: [25,1,2],
        },{
            label: 'Faturamento2',
            data: [5,10,25],
        }],
      }
    },

    methods: {
      base(){
        // obj = obter_colecao();
        // console.log(obj)
      }
    }

  }
</script>
