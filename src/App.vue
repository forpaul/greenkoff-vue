<template>
  <div id="app">
    <Navigation/>
    <router-view/>
  </div>
</template>

<script>
import Navigation from '@/components/Navigation.vue'

export default {
  name: 'app',
  components: {
    Navigation
  },
  created() {
    console.log('pidr')
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
