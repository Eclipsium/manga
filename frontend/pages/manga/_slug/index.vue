<template>
  <v-container fluid>
    <v-row>
      <v-col
        cols="12"
        md="6">
        <v-row class="justify-center">
          <p class="display-1">
            {{mangaData.english_name}}
          </p>
          <p class="subtitle" v-if="mangaData.japan_name">
            {{mangaData.japan_name}}
          </p>
        </v-row>
        <v-row class="justify-center">
          <v-img
            :aspect-ratio="9/16"
            :src="mangaData.poster"
            max-height="500"
            max-width="300"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.9)"
          />
        </v-row>
        <v-row class="justify-center align-center mt-3">
          <span class="title">Rating: </span>
          <v-rating
            v-model="mangaData.rating"
            background-color="orange lighten-3"
            color="orange"
          />
        </v-row>
        <v-row class="justify-center align-center">
          <span>Votes: 152</span>
          <v-tooltip top>
            <template v-slot:activator="{ on }">
              <v-btn small icon v-on="on" class="ml-2" color="error">
                <v-icon>
                  mdi-chart-areaspline-variant
                </v-icon>
              </v-btn>
            </template>
            <span>See all votes</span>
          </v-tooltip>
        </v-row>
        <v-row class="justify-center mt-3">
          <v-btn color="info">
            <v-icon left>mdi-book</v-icon>
            Add new parts
          </v-btn>
        </v-row>
      </v-col>
      <v-col
        cols="12"
        md="6">
        <v-row>
          <p class="title">Description:</p>
          <p>{{mangaData.descriptions}}</p>
        </v-row>
        <!--        <v-row>-->
        <!--          <p class="title">Томов: {{manga.volume}}</p>-->
        <!--        </v-row>-->
        <!--        <v-row>-->
        <!--          <p class="title">Последний выпуск: {{manga.volume}} - {{ manga.part}}</p>-->
        <!--        </v-row>-->
        <!--        <v-row>-->
        <!--          <v-btn color="success" :to="'/read/' + manga.slug +'/'+ manga.volume +'/' + manga.part">-->
        <!--            <v-icon left>mdi-new-box</v-icon>-->
        <!--            Читать последний выпуск-->
        <!--          </v-btn>-->
        <!--        </v-row>-->
        <v-row>
          <p class="title mr-4 align-center">Artists: </p>
          <v-chip
            color="primary"
            class="ma-2 align-center"
            v-for="artist in mangaData.artists" :key="artist.name"
            @click=toArtistPage(artist.slug)
            label
          >
            {{artist.name}}
          </v-chip>
        </v-row>
        <p>{{ mangaData.data}}</p>
        <v-row class="align-center">
          <v-chip-group
            column
          >
            <p class="title mr-4">Categories: </p>
            <v-chip
              v-for="tag in mangaData.categories" :key="tag"
              label
            >
              {{tag}}
            </v-chip>
          </v-chip-group>
        </v-row>
        <v-row>
          <p class="title">List of parts:</p>
        </v-row>
        <v-data-table
          :headers="headers"
          :items="mangaVolumes"
          max-height="350"
          item-key="name"
          hide-default-footer
          class="elevation-1"
          :sort-by="['volume']"
          :sort-desc="[false]"
        >
          <template v-slot:item.user="{ item }">
            <a href="#">{{item.created_by}}</a>
          </template>
          <template v-slot:item.action="{ item }">
            <v-icon
              color="success"
              @click="readMangaItem(item)"
            >
              mdi-book-open-page-variant
            </v-icon>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <v-row class="justify-center fill-height">
      <v-dialog v-model="dialog" fullscreen hide-overlay dark transition="slide-x-reverse-transition">
        <v-card>
          <v-toolbar dark dense flat>
            <v-toolbar-title>{{mangaData.english_name}}</v-toolbar-title>
            <v-spacer/>
            <v-btn icon dark @click="closeDialog()">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-toolbar>
          <v-card-text>
            <v-carousel
              hide-delimiters
              :show-arrows="true"
              show-arrows-on-hover
              :continuous="false"
              height="100%"
              v-model="currentImageIndex"
            >
              <v-carousel-item
                v-for="(item,i) in items"
                :key="i"
              >
                <template v-slot:default>
                  <v-img
                    :src="item.src"
                    @click="toNextImage()"
                    :aspect-ratio="0.7"
                    contain
                    max-height="700"
                  >
                  </v-img>
                </template>
              </v-carousel-item>
            </v-carousel>

          </v-card-text>
        </v-card>
      </v-dialog>
    </v-row>
  </v-container>
</template>

<script>
  import mangaReader from "../../../components/mangaReader";

  export default {
    name: "index",
    components: {
      mangaReader
    },
    async asyncData({$axios, params}) {
      // We can use async/await ES6 feature
      try {
        const mangaData = await $axios.$get('/api/v1/manga/' + params.slug + "/");
        const mangaVolumes = await $axios.$get('/api/v1/manga/' + params.slug + '/volumes/');
        return {mangaData, mangaVolumes}
      } catch (e) {
        console.log('Server error!')
      }

    },
    methods: {
      toNextImage() {
        if (this.currentImageIndex + 1 < this.items.length) {
          this.currentImageIndex++
        } else {
          this.closeDialog()
        }
      },
      readMangaItem(item) {
        this.currentVolume = item.volume;
        this.dialog = true
      },
      toArtistPage(slug) {
        this.$router.push('/artist/' + slug + '/')
      },
      closeDialog() {
        this.dialog = false;
        this.currentVolume = null;
        this.currentImageIndex = null;
      }
    },
    data: () => ({
      dialog: false,
      currentVolume: null,
      currentImageIndex: null,
      items: [
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },
        {
          src: 'https://h22.mangas.rocks/auto/15/39/34/01_p03.jpg?t=1575955621&u=0&h=aSU9JUm3YqGun8OB0P0BBg',
        },

      ],
      headers: [
        {text: 'Manga volume', value: 'volume', align: 'center',},
        {text: 'Uploaded by', value: 'user'},
        {text: 'Upload date', value: 'date'},
        {text: 'Image count', value: 'image_count'},
        {text: 'Actions', value: 'action', sortable: false},
      ],
    }),

  }
</script>

<style scoped>

</style>
