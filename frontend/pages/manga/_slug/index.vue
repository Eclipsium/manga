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
          <v-btn color="info" @click="toAddPage()">
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
    <v-row
      class="fill-height"
    >
      <v-dialog v-model="dialog" fullscreen hide-overlay dark transition="slide-x-reverse-transition">
        <v-card>
          <v-toolbar dark dense flat>
            <v-toolbar-title>{{mangaData.english_name}}</v-toolbar-title>
            <v-spacer/>
            <v-btn icon dark @click="closeDialog()">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-toolbar>
          <v-card-text height="100%">
            <v-carousel
              hide-delimiters
              :show-arrows="true"
              show-arrows-on-hover
              :continuous="false"
              :next-icon="hasNextArrow? 'mdi-chevron-right': false"
              height="100%"
              v-model="currentImageIndex"
            >
              <v-carousel-item
                v-for="(item, index) in items"
                :key="index"
              >
                <template v-slot:default>
                  <div class="d-flex">
                    <v-img
                      :src="getImageFromIndex(index)"
                      @click="toNextImage()"
                      :aspect-ratio="0.7"
                      :max-height="imageHeight"
                      contain
                      :position="getPosition(index)"
                    >
                    </v-img>
                    <v-img
                      :src="getImageFromIndex(index+1)"
                      v-if="isHorizontal"
                      @click="toNextImage()"
                      :aspect-ratio="0.7"
                      :max-height="imageHeight"
                      contain
                      :position="getPosition(index+1)"
                    >
                    </v-img>
                  </div>
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
      try {
        const mangaData = await $axios.$get('/api/v1/manga/' + params.slug + "/");
        const mangaVolumes = await $axios.$get('/api/v1/manga/' + params.slug + '/volumes/');
        return {mangaData, mangaVolumes}
      } catch (e) {
        console.log('Server error!')
      }
    },
    watch: {
      //Округляем индекс при прокрутке в 2х страничном режиме
      currentImageIndex() {
        if (this.isHorizontal) {
          this.currentImageIndex = Math.floor(this.currentImageIndex / 2) * 2
        }
      }
    },
    computed: {
      //Динамически меняем размер картинки
      imageHeight() {
        if (this.isHorizontal) {
          switch (this.$vuetify.breakpoint.name) {
            case 'xs':
              return '270px';
            case 'sm':
              return '320px';
            case 'md':
              return '500px';
            case 'lg':
              return '700px';
            case 'xl':
              return '800px'
          }
        }
        return '700px'
      },
      isHorizontal() {
        return this.$vuetify.breakpoint.width > this.$vuetify.breakpoint.height
      },
      //Корректное отображение стрелки вперед
      hasNextArrow() {
        if (this.isHorizontal && this.items.length - this.currentImageIndex > 2) {
          return true
        } else return !this.isHorizontal && this.items.length - this.currentImageIndex >= 1;
      },
    },
    methods: {
      //Method for switch carousel page with horizontal offset
      getPosition(index) {
        if (!this.isHorizontal) {
          return 'center center'
        } else if (index % 2 === 0) {
          return 'right center'
        } else if (index % 2 === 1) {
          return 'left center'
        }
      },
      toNextImage() {
        if (this.isHorizontal) {
          if (this.items.length - this.currentImageIndex > 2) {
            this.currentImageIndex += 2;
          } else {
            this.closeDialog()
          }
        }
        if (!this.isHorizontal) {
          if (this.items.length - this.currentImageIndex > 1) {
            this.currentImageIndex += 1;
          } else {
            this.closeDialog()
          }
        }
      },
      getImageFromIndex(index) {
        try {
          return this.items[index].src
        } catch (TypeError) {
          return undefined
        }
      },
      toAddPage() {
        this.$router.push('add/')
      }
      ,
      readMangaItem(item) {
        this.currentVolume = item.volume;
        this.dialog = true
      }
      ,
      toArtistPage(slug) {
        this.$router.push('/artist/' + slug + '/')
      }
      ,
      closeDialog() {
        this.dialog = false;
        this.currentVolume = null;
        this.currentImageIndex = null;
      }
    }
    ,
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
          src: 'https://static.readmanga.me/uploads/pics/01/36/510_o.jpg',
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
