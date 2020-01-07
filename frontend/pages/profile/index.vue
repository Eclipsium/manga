<template>
  <v-container fluid>
    <client-only>
      <v-container>
        <profileMainConfig/>
      </v-container>
      <v-container>
        <profilePhoto/>
      </v-container>
      <v-container>
        <profileChangePassword></profileChangePassword>
      </v-container>
      <v-container>
        <profileBookmark></profileBookmark>
      </v-container>
    </client-only>
  </v-container>
</template>

<script>
  import profileMainConfig from "../../components/profileComponents/profileMainConfig";
  import profilePhoto from "../../components/profileComponents/profilePhoto";
  import profileBookmark from "../../components/profileComponents/profileBookmark";
  import profileChangePassword from "../../components/profileComponents/profileChangePassword";

  export default {
    name: "index",
    components: {
      profileMainConfig,
      profilePhoto,
      profileBookmark,
      profileChangePassword,
    },
    data() {
      return {}
    },

    methods: {},
  }
</script>

<style scoped>

</style>
