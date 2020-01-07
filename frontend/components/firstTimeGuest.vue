<template>
  <div>
    <v-bottom-sheet v-model="sheet" >
      <v-sheet>
        <v-card tile>
          <v-card-text class="text-center font-weight-bold">
            <span>We use cookies to enhance your experience.
              By continuing to visit this site you agree to our use of cookies.
            </span>
            <a href="https://en.wikipedia.org/wiki/HTTP_cookie" color="warning">More info</a>
            <v-btn
              color="warning"
              class="ml-4"
              @click="closeButton"
            >Got it!
            </v-btn>
          </v-card-text>
        </v-card>
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
  export default {
    name: "firstTimeGuest",
    data: () => ({
      sheet: true,
    }),
    methods: {
      closeButton() {
        this.$store.commit('user/seeFirstMessage');
        this.sheet = false
      }
    },
    watch: {
      sheet() {
        if (this.sheet === false) {
          this.$store.commit('user/seeFirstMessage')
        }
      }
    }
  }
</script>

<style scoped>

</style>
