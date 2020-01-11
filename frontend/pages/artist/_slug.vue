<template>
  <div>
    <p class="text-center mb-2 title">All manga with artist {{this.artist}}</p>
    <full-list-manga/>
  </div>
</template>

<script>
  import fullListManga from "../../components/fullListManga";

  export default {
    name: "artists",
    head() {
      return {
        title: this.artist + ' all manga',
        meta: [
          {hid: 'home', name: 'description', content: 'Manga with artist ' + this.artist}
        ]
      }
    },
    async fetch({store, $axios, params, error}) {
      store.commit('manga/clearMangaCatalog');
      let data = await $axios.$get('/api/v1/manga/?artists=' + params.slug);
      if (data.count > 0){
        store.commit('manga/setMangaCatalog', data.results)
      }else {
        error({statusCode: 404})
      }
    },
    components: {
      fullListManga,
    },
    computed: {
      artist(){
        return this.$route.params.slug
      }
    }
  }
</script>

<style scoped>

</style>
