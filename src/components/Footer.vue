<template>
  <div>
    <v-footer dark class="font-weight-medium">
      <v-flex text-center xs12>
        {{ new Date().getFullYear() }} — <strong>Greenkoff</strong>
      </v-flex>
    </v-footer>
  </div>    
</template>
<script>
export default {
  data() {
    return {
      links: [
        { id: 1, title: 'Greenkoff', path: '/' },
        { id: 2, title: 'Товары', path: '/products' },
        { id: 3, title: 'Услуги', path: '/services' },
        { id: 4, title: 'О нас', path: '/contacts' },
      ],
    }
  },
}
</script>

