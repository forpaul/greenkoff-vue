<template>
  <div>
    <v-tabs
      v-model="active"
      color="cyan"
      dark
      slider-color="yellow"
    >
      <v-tab ripple>
        Товары

      </v-tab>
      <v-tab ripple>
        Услуги

      </v-tab>
      <v-tab-item lazy>
        <ProductsAdmin/> 
      </v-tab-item>
      <v-tab-item lazy>
        <ServicesAdmin/>
      </v-tab-item>
    </v-tabs>
  </div>
</template>
<script>
import ProductsAdmin from './ProductsAdmin.vue'
import ServicesAdmin from './ServicesAdmin.vue'


export default {
    components:{
        ProductsAdmin,
        ServicesAdmin
    },
  data() {
    return {
      active: null
    }
  },
    methods:{
      
    }
}
</script>