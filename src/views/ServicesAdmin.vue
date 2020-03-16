<template>
  <div class="services"> 
    <div 
    class="services-items"
    >
    <div class="service-add">
        <input class="input-services" type="text" placeholder="Введите название услуги" v-model="servicesObject.name">
        <input class="input-services" type="text" placeholder="Описание услуги" v-model="servicesObject.description">
        <input class="input-services" type="number" placeholder="Введите цену услуги" v-model="servicesObject.price">
        <input type="file" placeholder="">
        <v-btn @click="postServices()">Добавить услугу</v-btn>
    </div>
        <v-layout class="services-item"
         justify-space-between 
         align-center 
         v-for="service in services" :key="service.id"
         >
         
          <div class="services-img"><img src="https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg" alt=""></div>
          <div class="services-title"> <h2>{{ service.name }}</h2> </div>
          <div class="services-content__text">{{ service.description }}</div>
          <div class="btn-change"><v-btn
          @click="openModal(service)">Изменить</v-btn></div>
          <div class="btn-delete"><v-btn
          @click="removeService(service)">Удалить</v-btn></div>
         <!-- services-item -->
        </v-layout>
        <v-dialog
        v-model="modal.show"
        max-width="70%"
        v-if="modal.show"
          >
        <div class="dialog-item">
          <div class="dialog-content">
            <div class="dialog-item-input">
            <label>Новое название</label>
            <input id="name" type="text" class="input-services" v-model="modal.editItem.name">
            </div>
            <div class="dialog-item-input">
            <label>Новое описание</label>
            <input type="text" class="input-services" v-model="modal.editItem.description">
            </div>
            <div class="dialog-item-input">
            <label>Новая цена</label>
            <input type="text" class="input-services" v-model="modal.editItem.price">
            </div>
            <div class="buttons">
            <v-btn 
            class="btn-close" 
            color="warning" 
            dark
            @click="changeServices"
            >
               Изменить
            </v-btn>
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
        editItem: {}
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
      this.modal.editItem = Object.assign({}, service)
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
      this.servicesObject = {};
    },
    async changeServices(){
      const response = await this.apps_api.patch(`http://127.0.0.1:8000/api/services/${this.modal.editItem.id}/`,this.modal.editItem)
      await this.getServices();
      this.modal.editItem = {};
      this.modal.show = false;
    },
    async removeService(service)
    {
      if (window.confirm("Удалить " + service.name + "?")) { 
       const response = await this.apps_api.delete(`http://127.0.0.1:8000/api/services/${service.id}/`)
       await this.getServices();
      }
    }
  },

  async created() {
    await this.getServices()
  }
  
}

</script>
<style scoped lang="css">
.dialog-item{
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #fff;
  height: 200px;
}
.buttons{
  margin-top: 20px;
  flex-basis: 100%;
}
.dialog-content{
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
.dialog-item-input label{
  display: block;
}
.service-add{
  padding-top: 30px;
}
.input-services{
  padding: 10px;
  width: 200px;
  border: 1px solid gray;
  border-radius: 15px;
  margin-right: 20px;
}
.services-item{
  box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
  min-height: 150px;
  transition: 700ms;
  margin: 50px 30px;
}
.services-title{
  min-width: 200px;
  word-break: break-all;
}
.services-img img{
  display: block;
  width: 220px;
  height: 150px;
}
.services-content__text{
  text-align: center;
  word-break: break-all;
  padding: 0 30px;
  max-width: 400px;
  min-width: 350px;
}
@media (max-width: 850px){
  .services-item{
    margin: 50px auto;
    flex-direction: column;
    align-items: center;
    max-width: 400px;
  }
}
</style>
