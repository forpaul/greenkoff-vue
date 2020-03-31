<template>
<div class="product">
  <div class="cart-items">
    <div class="service-add">
        <div class="input-service">
          <div class="input-service__item"><input class="input-services" type="text" placeholder="Введите название товара" v-model="productObject.name"></div>
          <div class="input-service__item"><input class="input-services" type="text" placeholder="Описание товара" v-model="productObject.description"></div>
          <div class="input-service__item"><input class="input-services" type="number" placeholder="Введите цену товара" v-model="productObject.price"></div>
          <div class="input-service__item"><input class="input-services" type="number" placeholder="Введите позицию товара" v-model="productObject.position"></div>
        </div>
        <div class="input-group">
          <div class="input-group__item">Картинка 1<input type="file" @change="uploadImage($event, 1)" id="file-input" accept="image/jpeg, image/png" placeholder=""></div>
          <div class="input-group__item">Картинка 2<input type="file" @change="uploadImage($event, 2)" accept="image/jpeg, image/png" placeholder=""></div>
          <div class="input-group__item">Картинка 3<input type="file" @change="uploadImage($event, 3)" accept="image/jpeg, image/png" placeholder=""></div>
          <div class="input-group__item">Картинка 4<input type="file" @change="uploadImage($event, 4)" accept="image/jpeg, image/png" placeholder=""></div>
        </div>
        <v-btn 
        @click="postProduct()" 
        >Добавить товар
        </v-btn>
    </div>
    <v-layout class="services-item"
         justify-space-between 
         align-center 
         v-for="product in products" :key="product.id"
         >
         
          <div class="services-img"><img 
          class="white--text"
          height="200px"
          :src="product.image1 + '/'" 
          >
          </div>
          <div class="services-title"> <h2>{{ product.name }}</h2> </div>
          <div class="services-content__text">{{ product.description}}</div>
          <span class="price">Цена: {{ product.price }} руб</span>
          <div class="btn-change"><v-btn @click="openModal(product)" >Изменить</v-btn></div>
          <div class="btn-delete"><v-btn
          @click="removeProduct(product)">Удалить</v-btn></div>
         <!-- services-item -->
    </v-layout>
    <v-dialog
        v-model="modal.show"
        max-width="90%"
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
            <div class="dialog-item-input">
            <label>Новая позиция</label>
            <input type="text" class="input-services" v-model="modal.editItem.position">
            </div>
            <div class="input-group">
              <div class="input-group__item">Картинка 1<input type="file" @change="uploadImage($event, 1)" id="file-input" accept="image/jpeg, image/png" placeholder=""></div>
              <div class="input-group__item">Картинка 2<input type="file" @change="uploadImage($event, 2)" accept="image/jpeg, image/png" placeholder=""></div>
              <div class="input-group__item">Картинка 3<input type="file" @change="uploadImage($event, 3)" accept="image/jpeg, image/png" placeholder=""></div>
              <div class="input-group__item">Картинка 4<input type="file" @change="uploadImage($event, 4)" accept="image/jpeg, image/png" placeholder=""></div>
            </div>
            <div class="buttons">
            <v-btn 
            class="btn-close" 
            color="warning" 
            dark
            @click="changeProduct"
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
   </div>
  <!-- /.cart-items -->
</div>
</template>

<script>
export default {
  data() {
    return {
      modal: {
        show: false,
        editItem: {}
      },
      productObject:{
        name:'',
        description:'',
        position:'',
        price: ''
      },
      sendedImages: new FormData(),
      images: [],
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
    uploadImage(event, number_image) {
      this.sendedImages.append(`image${number_image}`, event.target.files[0]); 
      console.log('this.images', this.images)
    },
    async saveImage(product_id) {
      try {
          const response = await this.apps_api.patch(`http://localhost:8000/api/upload_image/${product_id}/`, this.sendedImages, {
            headers: { 'Content-Type' : 'multipart/form-data' }
          })
      } catch(err) {

      }
    },
    openModal(product) {    
      this.modal.editItem = Object.assign({}, product)
      this.modal.show = true
    },
    async getProducts() {
      try {
        const response = await this.apps_api.get('http://localhost:8000/api/products/')
        this.products = response.data
      } catch(err) {
        console.log(err)
      }
    },
    async postProduct(){
      const response = await this.apps_api.post('http://127.0.0.1:8000/api/products/',this.productObject)
      await this.saveImage(response.data.id)
      await this.getProducts()
      this.productObject = {};
    },
    async removeProduct(product)
    {
      if (window.confirm("Удалить " + product.name + "?")) { 
      const response = await this.apps_api.delete(`http://127.0.0.1:8000/api/products/${product.id}/`)
      await this.getProducts();
      }
      
    },
    async changeProduct(){
      const response = await this.apps_api.patch(`http://127.0.0.1:8000/api/products/${this.modal.editItem.id}/`,this.modal.editItem)
      await this.getProducts();
      this.modal.editItem = {};
      this.modal.show = false;
    }
    

},
    async created() {
    await this.getProducts()
    }
}
</script>

<style scoped lang="css">
input:focus{
  outline: none;
}
.dialog-item{
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #fff;
  height: 250px;
}
.buttons{
  margin-top: 20px;
  flex-basis: 100%;
}
.dialog-content{
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}
.dialog-item-input label{
  display: block;
  padding-top: 20px;
}
.input-services{
  padding: 10px;
  width: 200px;
  border: 1px solid gray;
  border-radius: 15px;
}
.input-service{
  display: flex;
  justify-content: space-between;
}
.services-items{
  margin-top: 150px;
  
}
.service-add{
  width: 80%;
  margin: 0 auto;
  padding-top: 30px;
}
.services-item{
  box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
  min-height: 150px;
  transition: 700ms;
  margin: 50px 30px;
}
.services-title{
  min-width: 100px;
  max-width: 200px;
  word-break: break-all;
}
.services-img img{
  display: block;
  width: 220px;
  object-fit: cover;
  height: 150px;
}
.services-content__text{
  padding: 0 30px;
  word-break: break-all;
  max-width: 400px;
  min-width: 350px;
}
.price{
  font-size: 20px;
  font-weight: 800;
}
.input-group{
  margin: 20px 0;
  display: flex;
  justify-content: space-between;
}
.input-group__item{
  text-align: start;
  display: flex;
  flex-direction: column;

}
</style>