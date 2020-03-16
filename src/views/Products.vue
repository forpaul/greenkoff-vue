<template>
<div class="product">
  <div class="cart-items">
  <v-layout wrap class="cart-item" justify-center >
    <v-flex xs12 sm2 class="item" v-for="product in products" :key="product.id">
      <v-card @click="openModal(product)">
        <v-img
          class="white--text"
          height="200px"
          :src="items[product.id -1] ? items[product.id -1] : ''"
        >
          <v-container fill-height fluid>
            <v-layout fill-height>
              <v-flex xm12 align-end flexbox>
                <span class="headline">{{ product.name }}</span>
              </v-flex>
            </v-layout>
          </v-container>
        </v-img>
        <v-card-title>
          <div>
            <div class="description">{{ product.description.slice(0, 50) }} ...</div>
            <v-divider class="my-3"/>
            <span class="price">Цена: {{ product.price }} руб</span>
          </div>
        </v-card-title>
      </v-card>
    </v-flex> 
  </v-layout>
   </div>
  <!-- /.cart-items -->
  <v-dialog
    v-model="modal.show"
    max-width="70%"
    v-if="modal.show"
  >
    <div class="dialog-item">
        <div class="dialog-title">{{ modal.item.name }}</div>
      <div class="dialog-content">
        <div class="dialog-gallery">
          <v-carousel 
          hide-delimiters
          height = '500'
          >
          <v-carousel-item
            v-for="(item,i) in items"
            :key="i"
            :src="item.src"
          />
          </v-carousel>
        </div>
        <div class="dialog-text">
          <div class="dialog-text__content">
            <div class="dialog-price">Цена {{ modal.item.price }} руб</div>
            <div class="dialog-description">{{ modal.item.description }}</div>
          </div>
          <v-btn 
            class="btn-close" 
            color="warning" 
            dark
            @click="modal.show=false"
          >
            Закрыть
        </v-btn>
        </div>
        </div> 
      </div> 
  </v-dialog>
</div>
</template>

<script>
export default {
  data() {
    return {
      defaultProduct: {
        name: '',
        description: '',
        price: 0,
        position: 0
      },
      modal: {
        show: false,
        item: {
          name: '',
          description: '',
          price: 0,
          position: 0
        }
      },
      items: [
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg'
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
          }
      ],
      products: []
    }
  },
  methods: {
    openModal(product) {    
      this.modal.item = Object.assign({}, product)
      this.modal.show = true
    },
    async getProducts() {
      try {
        const response = await this.apps_api.get('http://localhost:8000/api/products/')
        this.products = response.data
      } catch(err) {
        console.log(err)
      }
    }
  },
  async created() {
    await this.getProducts()
  },

}
</script>

<style scoped lang="css">
.title{
  position: relative;
  padding-top: 20px;
  word-break: break-all;
}
.description {
  width: fit-content;
  word-break: break-all;
}
.description {
  width: fit-content;
  word-break: break-all;
}
.item{
  margin: 30px;
  min-width: 200px;
  transition: 300ms;
}
.item:hover{
  transition: 500ms;
  transform: scale(1.07);
}
.cart-item{
  padding-top: 30px;
}
.price{
  font-size: 20px;
  font-weight: 800;
}
/* DIALOG */
.dialog-title{
  font-size: 42px;
  word-break: break-all;
  text-align: center;
  margin-bottom: 20px;
}
.dialog-item{
  background-color: #ffffff;
  height: 600px;
}
.dialog-content{
  display: flex;
  justify-content: space-around;
}
.dialog-gallery{
  width: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.dialog-text{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.dialog-price{
  font-size: 30px;
  margin-bottom: 30px;
}
.dialog-description{
  width: 300px;
  word-break: break-all
}
.btn-close{
  padding: 10px 10px 10px 10px;
}
</style>