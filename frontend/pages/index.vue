<template>
  <div>
      <last-manga-component title="Last update volume" dataSource="getLastManga"/>
      <last-manga-component title="Recommended manga" dataSource="getTopManga"/>
      <client-only>
        <first-time-guest v-if="firstTime"/>
      </client-only>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  import lastMangaComponent from "../components/lastMangaComponent";
  import firstTimeGuest from "../components/firstTimeGuest";

  export default {
    async fetch({store, $axios}) {
      let lastMangaData = await $axios.$get('api/v1/manga/last/');
      let topMangaData = await $axios.$get('api/v1/manga/?is_promoted=true');
      store.commit('manga/setLastManga', lastMangaData.results.slice(0, 10).reverse());
      store.commit('manga/setTopManga', topMangaData.results.slice(0, 10))
    },
    head() {
      return {
        title: 'Home page',
        meta: [
          {hid: 'home', name: 'description', content: 'Exchange and read manga online'}
        ]
      }
    },
    components: {
      lastMangaComponent,
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
