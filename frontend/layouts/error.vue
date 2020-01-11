<template>
  <v-app dark>
    <v-row class="justify-center">
      <v-col cols="12" md="4">
        <v-card>
          <v-card-title>
            <h1 v-if="error.statusCode === 404">
              {{ pageNotFound.title }}
            </h1>
            <h1 v-else>
              {{ otherError.title }}
            </h1>
          </v-card-title>
          <v-card-text>
            <h1 v-if="error.statusCode === 404">
              {{ pageNotFound.text }}
            </h1>
            <h1 v-else>
              {{ otherError.text }}
            </h1>
          </v-card-text>
          <v-card-actions>
            <v-btn :to="'/'" color="primary" class="mb-4">
              To main page
            </v-btn>
            <v-spacer/>
            <v-btn @click="writeDeveloper" color="primary" v-if="error.statusCode !== 404" class="mb-4">
              Email Developer
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
  export default {
    layout: 'empty',
    props: {
      message: {
        type: String,
        default: null
      },
      error: {
        type: Object,
        default: null
      }
    },
    head() {
      const title =
        this.error.statusCode === 404 ? this.pageNotFound.title : this.otherError.title
      return {
        title
      }
    },
    data() {
      return {
        pageNotFound: {
          'title': 'Page Not Found 404',
          'text': 'Try to return to the main page.'
        },
        otherError: {
          'title': 'An error occurred',
          'text': 'If this happens again, write to the developer'
        }
      }
    },
    methods: {
      writeDeveloper() {
        window.open('mailto:abiogenesis70ru@gmail.com', '_blank');
      }
    }
  }
</script>

<style scoped>
  h1 {
    font-size: 20px;
  }
</style>
