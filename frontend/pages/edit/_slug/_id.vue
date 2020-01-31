<template>
  <v-container fluid>
    <v-card class="overflow-hidden">
      <v-toolbar
        flat
        color="success"
      >
        <v-toolbar-title color="success">
          <v-btn icon left @click="$router.back()">
            <v-icon color="white">mdi-arrow-left</v-icon>
          </v-btn>
        </v-toolbar-title>
        <v-toolbar-title class="headline font-weight-regular white--text">
          Edit volume for manga {{mangaData.english_name}}
        </v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-simple-table
          fixed-header
          :height="tableHeight"
          :key="renderTable"
        >
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-left">Index</th>
              <th class="text-left">Two-page index</th>
              <th class="text-left">Image</th>
              <th class="text-center">Actions</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in images.results"
                :key="item.id"
            >
              <td>{{ index + 1 }}</td>
              <td>{{ Math.floor(index / 2) + 1 }}</td>
              <td>
                <v-card
                  elevation="2"
                  max-height="100"
                  max-width="100"
                >
                  <v-img
                    :src="item.image"
                    max-height="100"
                    contain
                  />
                </v-card>
              </td>
              <td class="text-center">
                <v-btn
                  v-if="index > 0"
                  @click="moveToTop(index)"
                  color="primary"
                  icon
                  large
                >
                  <v-icon>
                    mdi-arrow-up
                  </v-icon>
                </v-btn>
                <v-btn
                  @click="moveToDown(index)"
                  v-if="index < images.results.length - 1"
                  color="primary"
                  icon
                  large
                >
                  <v-icon>
                    mdi-arrow-down
                  </v-icon>
                </v-btn>

                <v-btn
                  @click="deleteImage(item)"
                  color="error"
                  icon
                  large
                >
                  <v-icon>
                    mdi-delete
                  </v-icon>
                </v-btn>
              </td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card-text>
      <v-card-actions class="my-3">
        <v-spacer/>
        <v-btn color="success" @click="addImageDialog = true">
          <v-icon left>
            mdi-plus
          </v-icon>
          Add image
        </v-btn>
        <v-spacer/>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    name: "editVolume",
    data() {
      return {
        addImageDialog: false,
        renderTable: 1
      }
    },
    head() {
      return {
        title: 'Edit volume for ' + this.mangaData.english_name,
        meta: [
          {hid: 'edit', name: 'description', content: 'Edit volume for ' + this.mangaData.english_name + 'page'}
        ]
      }
    },
    async asyncData({$axios, params, error}) {
      try {
        const images = await $axios.$get('/api/v1/volume/' + params.id + "/images/edit/");
        const mangaData = await $axios.$get('/api/v1/manga/' + params.slug + "/");
        return {images, mangaData}
      } catch (e) {
        error({
          statusCode: 404
        })
      }
    },
    computed: {
      tableHeight() {
        return this.$vuetify.breakpoint.height - 50
      }
    },
    mounted() {
      let token = this.$store.state.user.token;
      if (token) {
        this.$axios.setToken('Token ' + token);
      }
    },
    methods: {
      async deleteImage(item) {
        await this.$axios.$delete('/api/v1/images/' + item.id + '/')
          .then(() => {
            this.images.results = this.images.results.filter(function (obj) {
              return obj.id !== item.id;
            });
          })
      },
      async moveToTop(index) {
        let currentImagePayload = {
          'sort_index': this.images.results[index - 1].sort_index
        };
        let replacedImagePayload = {
          'sort_index': this.images.results[index].sort_index
        };
        await this.$axios.$patch('/api/v1/images/' + this.images.results[index].id + '/', currentImagePayload)
          .then(() => {
            this.$axios.$patch('/api/v1/images/' + this.images.results[index - 1].id + '/', replacedImagePayload)
              .then(() => {
                const temp = this.images.results[index];
                this.images.results[index] = this.images.results[index - 1];
                this.images.results[index - 1] = temp;
                this.renderTable++
              })
          });
      },
      async moveToDown(index) {
        let currentImagePayload = {
          'sort_index': this.images.results[index + 1].sort_index
        };
        let replacedImagePayload = {
          'sort_index': this.images.results[index].sort_index
        };
        await this.$axios.$patch('/api/v1/images/' + this.images.results[index].id + '/', currentImagePayload)
          .then(() => {
            this.$axios.$patch('/api/v1/images/' + this.images.results[index + 1].id + '/', replacedImagePayload)
              .then(() => {
                const temp = this.images.results[index];
                this.images.results[index] = this.images.results[index + 1];
                this.images.results[index + 1] = temp;
                this.renderTable++
              })
          });
      }
    }
  }
</script>

<style scoped>

</style>
