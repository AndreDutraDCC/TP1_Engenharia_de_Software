<template>
  <div class="small">
    <canvas :id='chartId' :width="chartWidth" :height="chartHeight"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js"
import numeral from 'numeral'

export default {
  props:['chartType', 'datasets', 'labels', 'startColor', 'options', 'setWidth', 'setHeight', 'responsive', 'colors', 'changeColors', 'monetary', 'sufix', 'prefix', 'beginAtZero', 'title', 'hasDots', 'multiAxis', 'hideLegend', 'prefixRight', 'sufixRight', 'monetaryRight'],
  data() {
  return {
    defaultColors: ['#182247', '#2A448C', '#E85D75', '#F1B71C'],


    ChartData: {
      type: '',
      data: {
        labels: [],
        datasets: []
      },
      options: {
        responsive: false,
        lineTension: 1,
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true,
              padding: 25,
              maintainAspectRatio: true,
            },
          }]
        }
      }
    },
  }
},

computed:{
  chartId(){
    return 'Chart' + Math.random()
  },
  chartWidth(){
    return this.setWidth ? this.setWidth : 600
  },
  chartHeight(){
    return this.setHeight ? this.setHeight : 400
  },
  dots(){
    return this.hasDots === false ? 0 : this.hasDots 
  }
},

methods:{
  fillDefault(){
    this.ChartData.type = this.chartType ? this.chartType : 'line'
    this.ChartData.data = this.fillData()
    this.fillOptions()
  },
  fillData(){
    let result = {
      labels: [],
      datasets: []
    }
    let amountLabels = 0
    let amountDataset = this.datasets.length

    //Set datasets
    for(let i = 0; i < amountDataset; i++){
      amountLabels = Math.max(amountLabels, this.datasets[i].data.length)
      let color = this.startColor ? parseInt(this.startColor) : 0
      result.datasets.push({})
      result.datasets[i].label = this.datasets[i].label ? this.datasets[i].label : ''
      result.datasets[i].data = this.datasets[i].data
      result.datasets[i].type = this.datasets[i].type
      result.datasets[i].stack = this.datasets[i].stack
      result.datasets[i].yAxisID = this.datasets[i].yAxisID
      result.datasets[i].fill = !!this.datasets[i].fill
      result.datasets[i].borderWidth = this.datasets[i].borderWidth ? this.datasets[i].borderWidth : 3
      if (this.ChartData.type == 'doughnut'){
        result.datasets[i].backgroundColor = []
        result.datasets[i].borderColor = []
        for(let j = 0; j < this.datasets[i].data.length; j++){
            result.datasets[i].backgroundColor.push(this.colors && this.colors.length > j ? this.colors[j] : (this.defaultColors[(j+color) % this.defaultColors.length]))
            result.datasets[i].borderColor.push("#fff")
        }
        result.datasets[i].backgroundColor = result.datasets[i].backgroundColor.reverse()
        result.datasets[i].borderColor = result.datasets[i].borderColor.reverse()
        result.datasets[i].data = result.datasets[i].data.reverse()
      }
      else{
        result.datasets[i].backgroundColor = this.changeColors ? (this.colors ? this.colors.map(x => x + 'B1') : this.defaultColors) : (this.colors && this.colors.length > i ? this.colors[i] + 'B1' : (this.defaultColors[(i+color) % this.defaultColors.length] + 'B1'))
        result.datasets[i].borderColor =  this.changeColors ? (this.colors ? this.colors.map(x => x + 'E1') : this.defaultColors) : (this.colors && this.colors.length > i ? this.colors[i] + 'E1' : (this.defaultColors[(i+color) % this.defaultColors.length] + 'E1'))
      }
    }

    //Set labels
    if(this.labels){
      result.labels = this.ChartData.type == 'doughnut' ? this.labels.reverse() : this.labels
    }
    else{
      for(let i = 0; i < amountLabels; i++){
        result.labels.push('')
      }
    }
    return result
  },
  fillOptions(){
    if(this.dots == 0) this.ChartData.options.elements = {...this.ChartData.options.elements, point: { radius: this.dots} }
    this.ChartData.options.scales.xAxes = [{gridLines: {display: false}}]
    this.ChartData.options.legend = { display: !this.hideLegend}
    if(this.ChartData.type == "doughnut"){
      this.ChartData.options.scales.xAxes[0].ticks = {display: false}
      this.ChartData.options.scales.yAxes[0].gridLines = {display: false}
      this.ChartData.options.scales.yAxes[0].ticks.display = false
      this.ChartData.options.legend = {...this.ChartData.options.legend, reverse: true }
    }
    this.ChartData.options = {...this.ChartData.options,...this.options}
    this.ChartData.options.scales.yAxes[0].ticks.beginAtZero = this.beginAtZero === false ? this.beginAtZero : this.ChartData.options.scales.yAxes[0].ticks.beginAtZero // false !== undefined
    this.ChartData.options.monetary = !!this.monetary
    this.ChartData.options.prefix = this.prefix ? this.prefix : (this.ChartData.options.prefix || '')
    this.ChartData.options.sufix = this.sufix ? this.sufix : (this.ChartData.options.sufix || '')
    let currentDataset = 0
    this.ChartData.options.scales.yAxes[0].ticks.callback = (value, index, values) => {
        if(index == 0) currentDataset += 1
        if(currentDataset == 1){
          let monetary = !!this.ChartData.options.monetary
          let prefix = this.ChartData.options.prefix || ''
          let sufix = this.ChartData.options.sufix || ''
          if ((parseInt(value) >= 1000) && monetary) {
            return prefix + numeral(value).format('#,###.##') + sufix
          } else {
            return prefix + value + sufix
          }
        }
        else if(currentDataset == 2){
          let monetaryR = !!this.monetaryRight
          let prefixR = this.prefixRight ? this.prefixRight : ''
          let sufixR = this.sufixRight ? this.sufixRight : ''
          if ((parseInt(value) >= 1000) && monetaryR) {
            return prefixR + numeral(value).format('#,###.##') + sufixR
          } else {
            return prefixR + value + sufixR
          }
        }
    },
    this.ChartData.options.responsive = !!this.responsive
    if(this.title){
      this.ChartData.options.title = {
        display: true,
        text: this.title
      }
    }
    ///MULTIAXIS
    if(this.multiAxis){
      this.ChartData.options.tooltips = {mode: 'index', intersect: false}
      this.ChartData.options.scales.yAxes[0].id = 'left'
      this.ChartData.options.scales.yAxes[0].type = 'linear'
      this.ChartData.options.scales.yAxes[0].position = 'left'
      this.ChartData.options.scales.yAxes.push({...this.ChartData.options.scales.yAxes[0]})
      this.ChartData.options.scales.yAxes[1].id = 'right'
      this.ChartData.options.scales.yAxes[1].type = 'linear'
      this.ChartData.options.scales.yAxes[1].position = 'right'
      this.ChartData.options.scales.yAxes[1].gridLines = {drawOnChartArea:false}
    }
  },
  createChart(chartId, chartData) {
    const ctx = document.getElementById(chartId);
    const myChart = new Chart(ctx, chartData);
  }
},

mounted() {
  this.fillDefault()
  this.createChart(this.chartId, this.ChartData);
},
}

</script>