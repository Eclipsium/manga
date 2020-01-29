<template>
  <v-container>
    <v-card flat>
      <v-toolbar
        flat
        color="success"
      >
        <v-icon left color="white">mdi-settings</v-icon>
        <v-toolbar-title class="headline font-weight-regular white--text" href="#results" id="results">
          Results
        </v-toolbar-title>
      </v-toolbar>
      <v-row>
        <v-col v-if="inProcess"
               cols="12"
               md="12"
        >
          <v-sheet
            class="px-3 pt-3 pb-3"
          >
            <v-skeleton-loader
              color="grey lighten-2"
              class="mx-auto"
              type="image"
              width="100%"
            />
          </v-sheet>
        </v-col>

        <v-col
          v-for="(manga, index) in mangaData.slice((page-1)*24, page*24)"
          :key="index"
          v-if=!inProcess
          elevation="0"
          cols="12"
          lg="2"
          md="3"
          sm="4"
          xs="6"
          class="mx-0"
        >
          <v-hover v-slot:default="{ hover }">
            <v-card flat
                    :elevation="hover ? 12 : 0 "
                    class="mb-5 mx-2"
            >
              <v-tooltip bottom max-width="200">
                <template v-slot:activator="{ on }">
                  <v-img
                    :aspect-ratio="0.7"
                    :src="manga.poster"
                    v-on="on"
                    height="150"
                    class="white--text align-end"
                    gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.9)"
                    @click="toMangaPage(manga.slug)"
                  >
                    <v-card-subtitle class="white--text">{{manga.english_name}}</v-card-subtitle>
                    <v-card-text class="text-center d-flex justify-center">
                            <span>
                              <v-icon
                                color="orange"
                              >
                                mdi-star
                              </v-icon>
                               {{manga.rating}}</span>
                      <v-spacer/>
                      <v-tooltip top v-if="manga.is_promoted">
                        <template v-slot:activator="{ on }">
                          <div v-on="on">
                            <v-icon color="success lighten-2">mdi-fire</v-icon>
                          </div>
                        </template>
                        <span>Recommended</span>
                      </v-tooltip>
                    </v-card-text>
                  </v-img>
                </template>
                <span v-if="manga.descriptions">{{manga.descriptions}}</span>
                <span v-else>No description</span>
              </v-tooltip>
            </v-card>
          </v-hover>
        </v-col>
      </v-row>
      <div class="text-center">
        <v-pagination
          v-model="page"
          color="primary"
          :length="pageLength"
          class="mb-4"
        />
      </div>
    </v-card>
  </v-container>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "fullListManga",
    data: () => ({
      page: 1,
      inProcess: false,
    }),
    computed: {
      pageLength() {
        return Math.floor(this.mangaData.length / 24) + 1
      },
      ...mapGetters({
        mangaData: 'manga/getMangaCatalog'
      })
    },
    methods: {
      toMangaPage(url) {
        this.$router.push('/manga/' + url + '/')
      },
    },
    watch: {
      page() {
        this.$vuetify.goTo('#results', {
          duration: 300,
          offset: 100,
          easing: 'easeInOutCubic',
        })
      }
    }
  }
</script>

<style scoped>

</style>
