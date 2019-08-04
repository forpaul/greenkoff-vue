<template>
	<div>
	  <v-toolbar
		fixed
	    dark
	    scroll-off-screen
	    scroll-target="#scrolling-techniques"
	  >
	    <v-toolbar-title>Greenkoff - столярная мастерская №1</v-toolbar-title>
	    <v-spacer></v-spacer>
			<v-toolbar-items>
	      <v-btn flat @click="$router.push('/')">Greenkoff</v-btn>
	      <v-btn flat @click="$router.push('/products')">Товары</v-btn>
	      <v-btn flat @click="$router.push('/services')">Услуги</v-btn>
	      <v-btn flat @click="$router.push('/contacts')">Контакты</v-btn>
	  	</v-toolbar-items>    
	  </v-toolbar>
	</div>
</template>
<script>
export default {
  data() {
    return {
      nav_drawer: true,
      items: [
        { title: 'Dashboard', icon: '' },
        { title: 'Photos', icon: '' },
        { title: 'About', icon: '' },
      ],
    }
  },
}
</script>
