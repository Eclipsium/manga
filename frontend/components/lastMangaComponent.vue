<template>
  <v-container fluid>
    <v-card
      class="mx-auto mb-6"
    >
      <v-card-text class="title text-center">{{title}}</v-card-text>
      <v-sheet
        class="mx-auto"
        max-width="100%"
      >
          <v-slide-group show-arrows>
            <v-row
              class="fill-height"
              align="center"
              justify="center"
            >
            <v-slide-item
              v-for="(manga, index) in this.$store.getters['manga/' + dataSource]"
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
                      :width="imageWidth"
                      contain
                      class="white--text align-end"
                      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.9)"
                      @click="toMangaPage(manga.slug)"
                    >
                      <div class="is-promoted" v-if="manga.is_promoted">
                        <v-icon large color="warning">
                          mdi-fire
                        </v-icon>
                      </div>
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
                          background-color="orange lighten-4"
                          color="orange"
                          readonly
                          half-increments
                          small
                        />
                      </div>
                    </v-img>
                  <client-only>
                    <v-card-subtitle v-if="manga.date">
                      Updated
                      <span class="subtitle-2 green--text">{{ manga.date }}</span>
                    </v-card-subtitle>
                  </client-only>
                </v-card>
              </v-hover>
            </v-slide-item>
            </v-row>
          </v-slide-group>
      </v-sheet>
      <v-card-actions align-content="center">
        <v-spacer/>
        <v-btn :to="'/manga/'" color="success" class="mb-3">full list</v-btn>
        <v-spacer/>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "lastMangaComponent",
    props: [
      'title',
      'dataSource'
    ],
    data: () => ({}),
    methods: {
      toMangaPage(url) {
        this.$router.push('/manga/' + url + '/')
      },
    },
    computed: {
      imageWidth() {
        if (!this.isHorizontal) {
          switch (this.$vuetify.breakpoint.name) {
            case 'xs':
              return '150px';
            case 'sm':
              return '250px';
            case 'md':
              return '250px';
            case 'lg':
              return '300px';
            case 'xl':
              return '300px'
          }
        } else {
          switch (this.$vuetify.breakpoint.name) {
            case 'xs':
              return '150px';
            case 'sm':
              return '150px';
            case 'md':
              return '200px';
            case 'lg':
              return '250px';
            case 'xl':
              return '250px'
          }
        }
      },
      isHorizontal() {
        return this.$vuetify.breakpoint.width > this.$vuetify.breakpoint.height
      },
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

  .is-promoted {
    position: absolute;
    left: 80%;
    top: 5%;
  }
</style>
