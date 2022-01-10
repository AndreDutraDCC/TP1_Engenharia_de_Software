import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getDatabase } from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCV0lR2EMT8WlVoliFkmo1I9jI4mfz8fHc",
  authDomain: "listify-es.firebaseapp.com",
  projectId: "listify-es",
  storageBucket: "listify-es.appspot.com",
  messagingSenderId: "960922406101",
  appId: "1:960922406101:web:d81c7387cd20b39b26665c",
  measurementId: "G-EES9L4Y5EM"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

Vue.prototype.$database = getDatabase(app)


new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
