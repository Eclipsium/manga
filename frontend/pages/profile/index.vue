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
        <profileChangePassword/>
      </v-container>
    </client-only>
  </v-container>
</template>

<script>
  import profileMainConfig from "../../components/profileComponents/profileMainConfig";
  import profilePhoto from "../../components/profileComponents/profilePhoto";
  import profileChangePassword from "../../components/profileComponents/profileChangePassword";

  export default {
    name: "index",
    head() {
      return {
        title: 'Profile settings',
        meta: [
          {hid: 'home', name: 'description', content: 'Change profile for current user'}
        ]
      }
    },
    components: {
      profileMainConfig,
      profilePhoto,
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
