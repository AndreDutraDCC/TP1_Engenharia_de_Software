import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import 'vuetify/'
// import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);


const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#181818',//'#000000',
        secondary: '#000000',//'#181818',
        accent: "#FFFFFF",
        error: "#E85D75",
        info: "#4B69A7",
        success: "#1ED760",
        warning: "#F1B71C",
      },
      dark: {
        primary: '#000000',
        secondary: '#181818',
        accent: "#FFFFFF",
        error: "#E85D75",
        info: "#4B69A7",
        success: "#1ED760",
        warning: "#F1B71C"
      },
    },
  },
})
  
// light: {
//     primary: '#182247',
//     secondary: '#181818',
//     accent: "#E4E9ED",
//     error: "#E85D75",
//     info: "#4B69A7",
//     success: "#4CAF50",
//     warning: "#F1B71C",
//     teste: "#f9fbfc",
//   },
//   dark: {
//     primary: '#2A335D',
//     secondary: '#181818',
//     accent: "#E4E9ED",
//     error: "#E85D75",
//     info: "#4B69A7",
//     success: "#4CAF50",
//     warning: "#F1B71C"
//   },

  export default vuetify