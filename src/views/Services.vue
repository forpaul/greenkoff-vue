<template>
  <div class="services"> 
    <div 
    @click="dialog=true"
    class="services-items"
    >
        <v-layout class="services-item" wrap justify-space-between align-center >
          <div class="services-img"><img src="https://cdn.vuetifyjs.com/images/cards/docks.jpg" alt=""></div>
          <div class="services-title"> <h2>{{ title }}</h2> </div>
          <div class="services-content__text">{{ description }}</div>
         <!-- services-item -->
        </v-layout>
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
        <!-- services-items -->
    </div>
    <!-- services -->
  </div>
</template>
<style lang="css">

.services-items{
  margin-top: 150px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  
}
.services-item{
  box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
  min-height: 150px;
  transition: 700ms;
  margin: 20px;
}
.services-item:hover{
  transition: 300ms;
  transform: scale(1.01);
}
.services-title{
  min-width: 200px;
}
.services-img img{
  display: block;
  width: 220px;
  height: 150px;
}
.services-content__text{
  padding: 0 30px;
  max-width: 400px;
  min-width: 350px;
}


</style>
<script>
export default {
data(){
  return{
      title: 'Услуга',
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