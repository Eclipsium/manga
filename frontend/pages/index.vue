<template>
  <div>
    <v-container>
      <last-manga-component :last-manga-data="lastMangaData"/>
    </v-container>
    <v-container>
      <blog-list/>
    </v-container>
  </div>
</template>

<script>
  import lastMangaComponent from "../components/lastMangaComponent";
  import blogList from "../components/blogList";

  export default {
    async asyncData({$axios}) {
      try {
        const lastMangaData = await $axios.$get('api/v1/manga/last/');
        const topMangaData = await $axios.$get('api/v1/manga/recommend/');
        return {lastMangaData, topMangaData}
      }catch (e) {
        console.log('I am a fat bug');
        console.log(e)
      }
    },
    components: {
      lastMangaComponent,
      blogList,
    },
  }
</script>
