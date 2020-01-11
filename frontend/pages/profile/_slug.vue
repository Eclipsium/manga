<template>
  <div>
    <p class="text-center mb-2 title">All manga added by user {{this.username}}</p>
    <full-list-manga/>
  </div>
</template>

<script>
  import fullListManga from "../../components/fullListManga";

  export default {
    name: "profile_user",
    components: {
      fullListManga,
    },
    head() {
      return {
        title: 'All manga by user ' + this.username,
        meta: [
          {hid: 'profile', name: 'description', content: 'All manga by user ' + this.username}
        ]
      }
    },
    computed: {
      username() {
        return this.$route.params.slug
      },
    },
    async fetch({store, $axios, params, error}) {
      store.commit('manga/clearMangaCatalog');
      let data = await $axios.$get('/api/v1/manga/?create_by_user=' + params.slug);
      if (data.count > 0) {
        store.commit('manga/setMangaCatalog', data.results)
      } else {
        error({statusCode: 404})
      }
    },
  }
</script>

<style scoped>

</style>
