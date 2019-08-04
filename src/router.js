import Vue from 'vue'
import Router from 'vue-router'

import Main from './views/Main.vue'
import Products from './views/Products.vue'
import Services from './views/Services.vue'
import Contacts from './views/Contacts.vue'


Vue.use(Router)
const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: Main,
      name: 'main',
      ru_name: 'Greenkoff - столярная мастерская №1'
    },
    {
      path: '/products',
      component: Products,
      name: 'products',
      ru_name: 'Greenkoff - товары'
    },
    {
      path: '/services',
      component: Services,
      name: 'services',
      ru_name: 'Greenkoff - услуги'
    },
     {
      path: '/contacts',
      component: Contacts,
      name: 'contacts',
      ru_name: 'Greenkoff - контакы'
    }
  ]
})

export default router
