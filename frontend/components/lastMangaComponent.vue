<template>
    <v-card
      class="mx-auto"
      flat
    >
      <v-card-text class="title text-center">Last update</v-card-text>
      <v-container>
        <v-row class="fill-height">
          <v-sheet
            class="mx-auto"
            max-width="100%"
          >
            <v-slide-group class="d-flex" show-arrows>
              <v-slide-item
                v-for="(manga, index) in lastMangaData.slice(0,10).reverse()"
                :key="index"
                elevation="10"
              >
                <v-hover v-slot:default="{ hover }">
                  <v-card flat
                          shaped
                          :elevation="hover ? 8 : 0 "
                          class="mb-4 mx-2"
                  >
                    <v-img
                      :aspect-ratio="0.7"
                      :src="manga.poster"
                      width="300"
                      class="white--text align-end"
                      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.9)"
                      @click="toMangaPage(manga.slug)"
                    >
                      <v-card-title>{{manga.english_name}}-{{manga.volume}}</v-card-title>
                      <v-expand-transition>
                        <div
                          v-if="hover"
                          class="d-flex transition-fast-in-fast-out info darken-4 v-card--reveal subtitle-2 white--text pa-2"
                          style="height: 100%;"
                        >
                          <p style="width: 250px">
                            {{manga.descriptions}}
                          </p>
                        </div>
                      </v-expand-transition>

                      <div class="text-center">
                        <v-rating
                          v-model="manga.rating"
                          background-color="orange lighten-3"
                          color="orange"
                          readonly
                          half-increments
                          small
                        />
                      </div>
                    </v-img>
                    <v-card-subtitle>
                      Updated
                      <span class="subtitle-2 green--text">{{ manga.date }}</span>
                    </v-card-subtitle>
                  </v-card>
                </v-hover>
              </v-slide-item>
            </v-slide-group>
          </v-sheet>
        </v-row>
      </v-container>
      <v-card-actions align-content="center">
        <v-spacer/>
        <v-btn :to="'/manga/'" color="success" class="mb-3">full list</v-btn>
        <v-spacer/>
      </v-card-actions>
    </v-card>
</template>

<script>
  import {mapGetters} from 'vuex'
  export default {
    name: "lastMangaComponent",
    data: () => ({}),
    methods: {
      toMangaPage(url) {
        this.$router.push('/manga/' + url + '/')
      },
    },
    computed: {
      ...mapGetters({
        lastMangaData: 'manga/getLastManga',
      })
    },
  }
</script>

<style scoped>
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .7;
    position: absolute;
    width: 100%;
  }
</style>
