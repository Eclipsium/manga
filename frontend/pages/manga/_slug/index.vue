<template>
  <v-container fluid>
    <v-row>
      <v-col
        cols="12"
        md="6">
        <v-row class="justify-center">
          <p class="display-1">
            {{mangaData.english_name}}
            <v-icon large color="warning" v-if="recommend">
              mdi-fire
            </v-icon>
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
          <v-rating
            v-model="tempRating"
            :readonly="isVoted || !$store.state.user.isAuth || voted"
            color="yellow darken-3"
            background-color="grey darken-1"
            hover
          />
          <span class="subtitle">({{mangaData.rating}}) {{votes.count}} votes</span>
        </v-row>
        <v-row
          v-if="$store.state.user.isAdmin"
          class="justify-center align-center mt-2">
          <v-btn dark color="purple lighten-1" v-if="!recommend" @click="submitRecommend">
            recommend
          </v-btn>
          <v-btn dark color="purple lighten-1"  v-if="recommend" @click="submitRecommend">
            not recommend
          </v-btn>
        </v-row>
      </v-col>
      <v-col
        cols=" 12
        "
        md="6">
        <v-row>
          <p class="title">Description:</p>
          <p>{{mangaData.descriptions}}</p>
        </v-row>
        <v-row v-if="this.mangaData.artists[0]">
          <p class="title mr-4 align-center">Artists: </p>
          <v-chip
            color="primary"
            class="ma-2 align-center"
            v-for="artist in this.mangaData.artists[0].split(',')" :key="artist"
            @click=toArtistPage(artist)
            label
          >
            {{artist}}
          </v-chip>
        </v-row>
        <v-row>
          <p class="title">List of parts:</p>
        </v-row>
        <v-data-table
          :headers="headers"
          :items="mangaVolumes"
          max-height="350"
          item-key="name"
          class="elevation-1"
          :sort-by="['volume']"
          :sort-desc="[false]"
        >
          <template v-slot:item.user="{ item }">
            <nuxt-link :to="'/profile/'+ item.created_by + '/'">{{item.created_by}}</nuxt-link>
          </template>
          <template v-slot:item.action="{ item }">
            <v-btn
              icon
              v-if="item.image_count"
              color="success"
              @click="readMangaItem(item)"
            >
              <v-icon
              >
                mdi-book-open-page-variant
              </v-icon>
            </v-btn>
            <v-btn
              icon
              v-if="!item.image_count"
              color="warning"
              loading
            >
            </v-btn>
            <v-btn
              icon
              v-if="$store.state.user.isAdmin"
              color="error"
              @click="deleteManga(item)"
            >
              <v-icon
              >
                mdi-delete
              </v-icon>
            </v-btn>
          </template>
        </v-data-table>
        <div class='text-center mt-4'>
          <v-btn
            v-if="$store.state.user.isAuth"
            color="primary"
            :to="'upload/'"
          >
            Add manga volume
          </v-btn>
        </div>
      </v-col>
    </v-row>
    <v-row
      class="fill-height"
    >
      <v-dialog v-model="readMangaDialog" fullscreen hide-overlay dark transition="slide-x-reverse-transition">
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
                v-for="(item, index) in volumeImages"
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
                      <template v-slot:placeholder>
                        <v-row
                          class="fill-height ma-0"
                          align="center"
                          justify="center"
                        >
                          <v-progress-circular indeterminate color="grey lighten-5"/>
                        </v-row>
                      </template>
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
                      <template v-slot:placeholder>
                        <v-row
                          class="fill-height ma-0"
                          align="center"
                          justify="center"
                        >
                          <v-progress-circular indeterminate color="grey lighten-5"/>
                        </v-row>
                      </template>
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
  import {mapGetters} from 'vuex'

  export default {
    name: "index",
    async asyncData({$axios, params, error}) {
      try {
        const mangaData = await $axios.$get('/api/v1/manga/' + params.slug + "/");
        const mangaVolumes = await $axios.$get('/api/v1/manga/' + params.slug + '/volumes/');
        const votes = await $axios.$get('/api/v1/votes/?manga__slug=' + params.slug);
        return {mangaData, mangaVolumes, votes}
      } catch (e) {
        error({
          statusCode: 404})
      }
    },
    head() {
      return {
        title: this.mangaData.english_name,
        meta: [
          {hid: 'home', name: 'description', content: 'Read and add volumes for ' + this.mangaData.english_name}
        ]
      }
    },
    mounted() {
      if(this.token){
        this.$axios.setToken('Token ' + this.token);
      }
      this.recommend = this.mangaData.is_promoted;
    },
    watch: {
      //Округляем индекс при прокрутке в 2х страничном режиме
      currentImageIndex() {
        if (this.isHorizontal) {
          this.currentImageIndex = Math.floor(this.currentImageIndex / 2) * 2
        }
      },
      //Update rating value
      tempRating() {
        let payload = {
          'manga': this.mangaData.id,
          'vote_int': this.tempRating
        };
        if (this.tempRating !== 0 && !this.isVoted && this.token && !this.voted) {
          this.$axios.$post('/api/v1/votes/', payload);
          this.voted = true
        }
      }
    },
    computed: {
      isVoted() {
        for (let index in this.votes.results) {
          if (this.votes.results[index].user === this.nickname) {
            this.tempRating = this.votes.results[index].vote_int;
            return true
          }
        }
        return false
      },
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
        if (this.isHorizontal && this.volumeImages.length - this.currentImageIndex > 2) {
          return true
        } else return !this.isHorizontal && this.volumeImages.length - this.currentImageIndex >= 1;
      },
      ...mapGetters({
        token: 'user/getUserToken',
        nickname: 'user/getUserNickName',
        volumeImages: 'image/getVolumeImage'
      })
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
      submitRecommend(){
        this.recommend = !this.recommend;
        this.$axios.$patch('/api/v1/manga/' + this.mangaData.slug + "/", {'is_promoted': this.recommend})
      },
      toNextImage() {
        if (this.isHorizontal) {
          if (this.volumeImages.length - this.currentImageIndex > 2) {
            this.currentImageIndex += 2;
          } else {
            this.closeDialog()
          }
        }
        if (!this.isHorizontal) {
          if (this.volumeImages.length - this.currentImageIndex > 1) {
            this.currentImageIndex += 1;
          } else {
            this.closeDialog()
          }
        }
      },
      getImageFromIndex(index) {
        try {
          return this.volumeImages[index]
        } catch (TypeError) {
          return ''
        }
      },
      readMangaItem(item) {
        this.$store.dispatch('image/LOAD_VOLUME_IMAGE', item.id);
        this.readMangaDialog = true
      },
      deleteManga(item) {
        this.$store.dispatch('image/LOAD_VOLUME_IMAGE', item.id);
        this.readMangaDialog = true
      },
      toArtistPage(artist) {
        this.$router.push('/artist/' + artist + '/')
      },
      closeDialog() {
        this.readMangaDialog = false;
        this.currentVolume = null;
        this.currentImageIndex = null;
      },
    }
    ,
    data: () => ({
      voted: false,
      recommend: false,
      readMangaDialog: false,
      addMangaDialog: false,
      currentVolume: null,
      currentImageIndex: null,
      tempRating: 0,
      digitRules: [
        v => !!v || 'Is required',
        v => /^\d+$/.test(v) || 'Input digit!'
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
