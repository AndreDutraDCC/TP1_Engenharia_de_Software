import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Keyword from '../views/Keyword.vue'
import Feeling from '../views/Feeling.vue'
import Dashboard from '../views/Dashboard.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/keyword',
    name: 'Keyword',
    component: Keyword
  },
  {
    path: '/feeling',
    name: 'Feeling',
    component: Feeling
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router