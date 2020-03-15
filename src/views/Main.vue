<template>
  <div class="main-page">
    <div class="banners--about-div">
      <v-card @click="$router.push('/contacts')">
        <v-img
          id="banners--img"
          :src="banners[1]"
          height="350"
          class="banners-img-class"
        ></v-img>
        <v-card-title class="title">Информация о Greenkoff</v-card-title>
      </v-card>
      <v-layout row wrap>
        <v-flex xs12 md6 lg6>
          <v-card @click="$router.push('/products')">
            <v-img
              id="banners--img"
              :src="banners[2]"
              height="350"
              class="my-2 mr-2 banners-img-class"
            ></v-img>
            <v-card-title class="title">Товары</v-card-title>
          </v-card>
        </v-flex>
        <v-flex xs12 md6 lg6>
          <v-card @click="$router.push('/services')">
            <v-img
              id="banners--img"
              :src="banners[3]"
              height="350"
              class="my-2 banners-img-class"
            ></v-img>
            <v-card-title class="title">Услуги</v-card-title>
          </v-card>
        </v-flex>
      </v-layout>
    </div>

    <v-divider class="mt-3"/>
    <h2 class="my-2">Наши работы</h2>
    <v-divider class="mb-2"/>

    <div class="work-slider mb-5">
      <v-layout row wrap>
        <v-flex
          v-for="n in 9"
          :key="n"
          xs4
          d-flex
        >
          <v-card flat tile class="d-flex my-2" style="cursor: pointer">
            <v-img
              :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
              aspect-ratio="1"
              class="grey lighten-2"
            >
              <template v-slot:placeholder>
                <v-layout
                  fill-height
                  align-center
                  justify-center
                  ma-0
                >
                  <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                </v-layout>
              </template>
            </v-img>
          </v-card>
        </v-flex>
      </v-layout>
    </div>
    <Footer/>
  </div>
</template>
<script>
import Footer from '@/components/Footer.vue'

export default {
  components: {
    Footer,
  },
  data() {
    return {
      banners: {
        1: require('@/assets/aboutus.jpg'),
        2: require('@/assets/products.jpg'),
        3: require('@/assets/services.jpg')
      }
    }
  },
}
</script>
<style lang="css">
.main-page{
  padding: 6px;
}
#banners--img{
  opacity: .5;

}
.banners-img-class{
  transition: 700ms;
}
.banners-img-class:hover{
  opacity: 1 !important;
  cursor: pointer;
  transition: .3s all ease-in-out;
}
</style>


