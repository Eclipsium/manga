<template>
  <div>
    <v-container>
      <last-manga></last-manga>
    </v-container>
    <v-container>
      <blog-list></blog-list>
    </v-container>
  </div>
</template>

<script>
    import lastManga from "../components/lastManga";
    import blogList from "../components/blogList";

    export default {
        components: {
            lastManga,
            blogList,
        }
    }
</script>
