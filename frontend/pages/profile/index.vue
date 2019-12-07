<template>
  <v-container fluid>
    <v-container>
      <profileMainConfig/>
    </v-container>
    <v-container>
      <profilePhoto/>
    </v-container>
    <v-container>
      <profileBookmark></profileBookmark>
    </v-container>
  </v-container>
</template>

<script>
  import profileMainConfig from "../../components/profileComponents/profileMainConfig";
  import profilePhoto from "../../components/profileComponents/profilePhoto";
  import profileBookmark from "../../components/profileComponents/profileBookmark";

  export default {
    name: "index",
    components: {
      profileMainConfig,
      profilePhoto,
      profileBookmark
    },
    data() {
      return {}
    },

    methods: {},
  }
</script>

<style scoped>

</style>
