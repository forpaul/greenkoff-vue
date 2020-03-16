<template>
  <div class="services"> 
    <div 
    class="services-items"
    >
        <v-layout class="services-item"
         justify-space-between 
         align-center 
         v-for="service in services" :key="service.id"
         @click="openModal(service)"
         >
         
          <div class="services-img"><img src="https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg" alt=""></div>
          <div class="services-title"> <h2>{{ service.name }}</h2> </div>
          <div class="services-content__text">{{ service.description }}</div>
         <!-- services-item -->
        </v-layout>
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
            class="carousel"
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
              <div class="dialog-price">Цена {{ modal.item.price }} руб</div>
              <div class="dialog-description">{{ modal.item.description }}</div>
            </div>
            <v-btn 
          class="btn-close" 
          color="warning" 
          dark
          @click="modal.show=false">
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
<script>
export default {
data(){
  return{
      modal: {
        show: false,
        item: {}
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
      services:[],
      servicesObject:{
        name:'',
        description:'',
        price: 0
      }
  }
},
  methods: {
    openModal(service) {    
      this.modal.item = Object.assign({}, service)
      this.modal.show = true
    },
    async getServices() {
      try {
        const response = await this.apps_api.get('http://127.0.0.1:8000/api/services/')
        this.services = response.data
      } catch(err) {
        console.log(err)
      }
    },
    async postServices(){
      const response = await this.apps_api.post('http://127.0.0.1:8000/api/services/',this.servicesObject)
      await this.getServices();
  }
  },

  async created() {
    await this.getServices()
  }
  
}

</script>
<style scoped lang="css">

.services-items{
  margin-top: 150px;
}
.services-item{
  box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
  min-height: 150px;
  transition: 700ms;
  margin: 50px 30px;
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
  word-break: break-all;
  max-width: 400px;
  min-width: 350px;
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
  word-break: break-all
}
.btn-close{
  padding: 10px 10px 10px 10px;
}
@media (max-width: 850px){
  .services-item{
    margin: 50px auto;
    flex-direction: column;
    align-items: center;
    max-width: 400px;
  }
  .dialog-item{
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .dialog-content{
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .dialog-text{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .dialog-gallery{
    width:100%;
    height: 300px;
  }
}
</style>
