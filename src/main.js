import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import routes from './router.js'
import axios from 'axios'
import Vuetify from 'vuetify';

import 'material-design-icons-iconfont/dist/material-design-icons.css'
import 'vuetify/dist/vuetify.min.css'

Vue.use(VueRouter)
Vue.use(Vuetify)

Vue.prototype.apps_api = axios.create({
  // baseURL: process.env.VUE_APP_API_URL,
  timeout: 110000,
});


Vue.config.productionTip = false

new Vue({
  router: routes,
  render: h => h(App),
}).$mount('#app')
