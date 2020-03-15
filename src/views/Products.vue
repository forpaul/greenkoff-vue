<template>
<div class="product">
  <div class="cart-items">
  <v-layout wrap class="cart-item" justify-center >
    <v-flex xs12 sm2 class="item" >
      <v-card @click="dialog=true">
        <v-img
          class="white--text"
          height="200px"
          src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
        >
          <v-container fill-height fluid>
            <v-layout fill-height>
              <v-flex xs12 align-end flexbox>
                <span class="headline">{{ title }}</span>
              </v-flex>
            </v-layout>
          </v-container>
        </v-img>
        <v-card-title>
          <div>
            <div class="description">{{ description }}</div>
            <v-divider class="my-3"/>
            <span class="price">Цена: {{ price }} руб</span>
          </div>
        </v-card-title>
      </v-card>
    </v-flex> 
  </v-layout>
   </div>
  <!-- /.cart-items -->
    <v-dialog
      v-model="dialog"
      max-width="70%"
    >
      <div class="dialog-item">
        <div class="dialog-title">{{ title }}</div>
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
            ></v-carousel-item>
            </v-carousel>
          </div>
          <div class="dialog-text">
            <div class="dialog-text__content">
              <div class="dialog-price">Цена {{ price }} руб</div>
              <div class="dialog-description">{{ description }}</div>
            </div>
            <v-btn 
          class="btn-close" 
          color="warning" 
          dark
          @click="dialog=false">
              Закрыть
          </v-btn>
          </div>
          
        </div>
      </div>   
    </v-dialog>
</div>
<!-- /.product -->
</template>
<style lang="css">
.title{
  position: relative;
  padding-top: 20px;
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
}
.btn-close{
  padding: 10px 10px 10px 10px;
}
</style>
<script>
export default {
  data(){
    return{
      title: 'Что то там',
      description:'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Velit maiores pariatur veritatis perspiciatis, error fugit dolorem vero. Esse, excepturi, delectus autem nulla expedita doloremque dolores, quo quis aliquam id aspernatur.',
      price:100,
      dialog: false,
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
        ]
    }
    
  }

}
</script>