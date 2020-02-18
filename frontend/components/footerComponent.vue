<template>
  <v-footer
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        href="mailto:abiogenesis70ru@gmail.com"
        color="primary"
        text
        class="mt-2"
      >
        <v-icon left>
          mdi-android-debug-bridge
        </v-icon>
        Find bug?
      </v-btn>

      <v-btn
       :to="'/purpose/'"
        color="primary"
        text
        class="mt-2"
      >
        <v-icon left>
          mdi-license
        </v-icon>
        The purpose of this site
      </v-btn>


      <v-col
        class="py-4 text-center"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Manga-exchange.ru</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
  export default {
    name: "footerComponent",
    data: () => ({}),
  }
</script>

<style scoped>

</style>
