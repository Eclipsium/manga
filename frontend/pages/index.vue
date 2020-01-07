<template>
  <div>
    <last-manga-component/>
    <blog-list/>
    <first-time-guest v-if="firstTime"/>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  import lastMangaComponent from "../components/lastMangaComponent";
  import blogList from "../components/blogList";
  import firstTimeGuest from "../components/firstTimeGuest";

  export default {
    async fetch({store, $axios}) {
      let lastMangaData = await $axios.$get('api/v1/manga/last/');
      store.commit('manga/setLastManga', lastMangaData.results)
    },
    components: {
      lastMangaComponent,
      blogList,
      firstTimeGuest
    },
    data: () => ({}),
    computed: {
      ...mapGetters({
        firstTime: 'user/getIsFirstTime',
      })
    }
  }
</script>
