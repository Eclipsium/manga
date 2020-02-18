<template>
  <v-container fluid>
    <v-row>
      <v-col
        cols="12"
        md="6">
        <v-row class="justify-center">
          <p class="display-1">
            {{mangaData.english_name}}
            <client-only>

              <v-icon large color="warning" v-if="recommend">
                mdi-fire
              </v-icon>

            </client-only>
          </p>
        </v-row>
        <v-row class="justify-center">
          <v-img
            :aspect-ratio="9/16"
            :src="mangaData.poster"
            max-height="500px"
            max-width="300px"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.9)"
          />
        </v-row>
        <v-row class="justify-center align-center mt-3">
          <client-only>
            <v-rating
              v-model="tempRating"
              :readonly="isVoted || !$store.state.user.isAuth || voted"
              color="yellow darken-3"
              background-color="grey darken-1"
              hover
            />
          </client-only>
          <span class="subtitle">({{mangaData.rating}}) {{votes.count}} votes</span>
        </v-row>
        <client-only>
          <v-row
            v-if="$store.state.user.isAdmin"
            class="justify-center align-center mt-2">
            <v-btn dark color="purple lighten-1" v-if="!recommend" @click="submitRecommend">
              recommend
            </v-btn>
            <v-btn dark color="purple lighten-1" v-if="recommend" @click="submitRecommend">
              not recommend
            </v-btn>
          </v-row>
        </client-only>
      </v-col>
      <v-col
        cols="12"
        md="6">
        <v-container>
          <client-only>
            <v-row v-if="mangaData.descriptions">
              <p class="title">Description:</p>
              <p>{{mangaData.descriptions}}</p>
            </v-row>
            <v-row v-if="mangaData.artists[0]">
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
              :headers="$store.state.user.isAdmin ? admin_headers : user_headers"
              :items="mangaVolumes"
              max-height="350px"
              item-key="name"
              class="elevation-1"
              :sort-by="['volume']"
              :sort-desc="[false]"
            >
              <template v-slot:item.user="{ item }">
                <nuxt-link
                  :to="'/profile/' + item.created_by + '/'"
                  :event="isDeleted(item) ? '' : 'click'"
                  :class="isDeleted(item) ? 'disabled': ''"
                >
                  {{item.created_by ? item.created_by : 'Anonymous' }}
                </nuxt-link>
              </template>
              <template
                v-slot:item.image_count="{item}"
              >
                <v-tooltip bottom v-if="item.image_count % 2 === 1">
                  <template v-slot:activator="{ on }">
                    <div
                      class="orange--text font-weight-bold"
                      v-on="on"
                    >
                      {{item.image_count}}
                    </div>
                  </template>
                  <span>
                  Odd number of pages. You may need to edit
                </span>
                </v-tooltip>
                <div class="green--text font-weight-bold"
                     v-if="item.image_count % 2 === 0 && item.image_count">
                  {{item.image_count}}
                </div>
                <div
                  v-if="!item.image_count">
                  loading...
                </div>
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
                  v-if="item.image_count > 0 && (item.created_by === nickname || $store.state.user.isAdmin)"
                  color="warning"
                  :to="'/edit/'+ mangaData.slug + '/' + item.id + '/'"
                >
                  <v-icon>
                    mdi-content-save-edit
                  </v-icon>
                </v-btn>

                <v-btn
                  icon
                  v-if="$store.state.user.isAdmin || item.created_by === nickname"
                  color="error"
                  @click="deleteDialogOpen(item)"
                >
                  <v-icon>
                    mdi-delete
                  </v-icon>
                </v-btn>
              </template>

            </v-data-table>

            <div class='text-center mt-4'>
              <v-btn
                color="primary"
                :to="'upload/'"
              >
                <v-icon left>
                  mdi-message-plus
                </v-icon>
                upload next volume
              </v-btn>
            </div>
          </client-only>
        </v-container>
      </v-col>
    </v-row>
    <client-only>
      <v-row class="justify-center">
        <comment-component :mangaData="mangaData" :mangaComments="mangaComments"></comment-component>
      </v-row>
    </client-only>
    <v-dialog v-model="readMangaDialog" scrollable fullscreen hide-overlay dark transition="slide-x-reverse-transition">
      <v-card :max-width="$vuetify.breakpoint.width" :max-height="$vuetify.breakpoint.height">
        <v-toolbar dark dense flat>
          <v-toolbar-title>{{mangaData.english_name}}</v-toolbar-title>
          <v-spacer/>
          <v-btn icon dark @click="closeDialog()">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
        <v-card-text>
          <v-carousel
            v-if="volumeImages"
            hide-delimiters
            :show-arrows="true"
            :continuous="false"
            :next-icon="hasPrevArrow? 'mdi-chevron-right': false"
            height="100%"
            v-model="currentImageIndex"
            @change="changeCurrentImage"
          >
            <v-carousel-item
              v-for="(item, index) in volumeImages"
              :key="index"
            >
              <template v-slot:default>
                <div class="d-flex">
                  <v-img
                    :src="getImageFromIndex(index-1)"
                    @click="toNextImage()"
                    v-if="isHorizontal"
                    :aspect-ratio="0.7"
                    :max-height="imageHeight"
                    contain
                    :position="getPosition(index-1)"
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
                </div>
              </template>
            </v-carousel-item>
          </v-carousel>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-dialog
      v-model="deleteMangaDialog"
      width="500"
    >
      <v-card>
        <v-card-title
          primary-title
        >
          Delete volume
        </v-card-title>
        <v-card-text>
          Do you seriously want to delete volume {{this.volumeToDelete.volume}} for {{this.mangaData.english_name}}?
        </v-card-text>

        <v-divider/>
        <v-card-actions>
          <v-btn
            color="success"
            text
            @click="deleteMangaDialog = false"
          >
            Cancel
          </v-btn>
          <v-spacer/>
          <v-btn
            color="error"
            text
            @click="deleteManga(volumeToDelete)"
          >
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
  import {mapGetters} from 'vuex'
  import commentComponent from '~/components/commentComponent'

  export default {
    name: "index",
    components: {
      commentComponent
    },
    async asyncData({$axios, params, error}) {
      try {
        const mangaData = await $axios.$get('/api/v1/manga/' + params.slug + "/");
        const mangaVolumes = await $axios.$get('/api/v1/manga/' + params.slug + '/volumes/');
        const votes = await $axios.$get('/api/v1/votes/?manga__slug=' + params.slug);
        const mangaComments = await $axios.$get('/api/v1/comments/?manga=' + mangaData.id);
        return {mangaData, mangaVolumes, votes, mangaComments}
      } catch (e) {
        error({
          statusCode: 404
        })
      }
    },
    head() {
      return {
        title: this.mangaData.english_name,
        meta: [
          {name: 'description', hid: 'description', content: 'Read and upload volumes for ' + this.mangaData.english_name},
          // Open Graph
          {name: 'og:title', content: this.mangaData.english_name},
          {name: 'og:description', content: 'Read and upload volumes for ' + this.mangaData.english_name},
          {name: 'og:type', content: 'website'},
          {name: 'og:url', content: 'http://manga-exchange.ru' + this.$route.fullPath},
          {name: 'og:image', content: this.mangaData.poster},
          // Twitter Card
          {name: 'twitter:card', content: 'summary'},
          {name: 'twitter:site', content: 'http://manga-exchange.ru' + this.$route.fullPath},
          {name: 'twitter:title', content: this.mangaData.english_name},
          {name: 'twitter:description', content: 'Read and upload volumes for ' + this.mangaData.english_name},
          {name: 'twitter:image', content: this.mangaData.poster},
          {name: 'twitter:image:alt', content: this.mangaData.english_name}
        ]
      }
    },
    mounted() {
      if (this.token) {
        this.$axios.setToken('Token ' + this.token);
      }
      this.recommend = this.mangaData.is_promoted;
    },
    watch: {
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
      },
      isHorizontal() {
        if (this.isEven) {
          if (this.volumeImages.length > this.currentImageIndex) {
            this.currentImageIndex = Math.floor(this.currentImageIndex / 2) * 2 + 1;
            this.lastImageIndex = this.currentImageIndex
          }
        } else if (this.volumeImages.length > this.currentImageIndex) {
          this.currentImageIndex = Math.ceil(this.currentImageIndex / 2) * 2;
          this.lastImageIndex = this.currentImageIndex
        }
      },
      readMangaDialog() {
        if (this.readMangaDialog === false) {
          this.lastImageIndex = 0;
          this.currentImageIndex = 0;
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
              return '250px';
            case 'sm':
              return '300px';
            case 'md':
              return '500px';
            case 'lg':
              return '600px';
            case 'xl':
              return '700px'
          }
        }
        return '600px'
      },
      isHorizontal() {
        return this.$vuetify.breakpoint.width > this.$vuetify.breakpoint.height
      },
      //Корректное отображение стрелки вперед
      hasPrevArrow() {
        if (!this.isHorizontal) {
          return (this.volumeImages.length - this.currentImageIndex) > 1
        } else {
          return this.volumeImages.length - this.currentImageIndex > 2;
        }
      },
      isEven() {
        return this.volumeImages.length % 2 === 0;
      },
      ...
        mapGetters({
          token: 'user/getUserToken',
          nickname: 'user/getUserNickName',
          volumeImages: 'image/getVolumeImage'
        })
    },
    methods: {
      //Изменяем индекс при прокрутке в 2х страничном режиме
      changeCurrentImage() {
        if (this.isHorizontal) {
          //Если листаем вперед
          if (this.currentImageIndex > this.lastImageIndex) {
            this.currentImageIndex += 1;
            this.lastImageIndex = this.currentImageIndex;
          }
          if (this.currentImageIndex < this.lastImageIndex) {
            this.currentImageIndex -= 1;
            this.lastImageIndex = this.currentImageIndex;
          }
        }
      },
      deleteDialogOpen(item) {
        this.volumeToDelete = item;
        this.deleteMangaDialog = true
      },
      //Method for switch carousel page with horizontal offset
      getPosition(index) {
        if (!this.isHorizontal) {
          return 'center center'
        } else if (!this.isEven) {
          if (index % 2 === 0) {
            return 'left center'
          } else return 'right center'
        } else {
          if (index % 2 === 0) {
            return 'right center'
          } else return 'left center'
        }
      },
      isDeleted(item) {
        return item.created_by === 'deleted' || item.created_by === null
      },
      submitRecommend() {
        this.recommend = !this.recommend;
        this.$axios.$patch('/api/v1/manga/' + this.mangaData.slug + "/", {'is_promoted': this.recommend})
      },
      toNextImage() {
        if (this.isHorizontal) {
          if (this.currentImageIndex - this.volumeImages.length < 2) {
            this.currentImageIndex -= 2;
            this.lastImageIndex = this.currentImageIndex
          } else {
            this.closeDialog()
          }
        }
        if (!this.isHorizontal) {
          if (this.currentImageIndex - this.volumeImages.length < 1) {
            this.currentImageIndex -= 1;
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
      async readMangaItem(item) {
        await this.$store.dispatch('image/LOAD_VOLUME_IMAGE', item.id);
        this.currentImageIndex = item.image_count - 1;
        this.lastImageIndex = item.image_count - 1;
        this.readMangaDialog = true
      },
      deleteManga(item) {
        this.$axios.$delete('api/v1/volume/' + item.id + '/delete/')
          .then(() => {
            this.mangaVolumes = this.mangaVolumes.filter(function (obj) {
              return obj.id !== item.id;
            });
            this.deleteMangaDialog = false
          }).catch((e) => {
        })
      },
      toArtistPage(artist) {
        this.$router.push('/artist/' + artist + '/')
      },
      closeDialog() {
        this.lastImageIndex = 0;
        this.currentImageIndex = 0;
        this.readMangaDialog = false;
      },
    },
    data: () => ({
      voted: false,
      isBlocked: false,
      lastImageIndex: null,
      recommend: false,
      readMangaDialog: false,
      deleteMangaDialog: false,
      currentImageIndex: null,
      volumeToDelete: {},
      tempRating: 0,
      digitRules: [
        v => !!v || 'Is required',
        v => /^\d+$/.test(v) || 'Input digit!'
      ],
      admin_headers: [
        {text: 'Manga volume', value: 'volume', align: 'center',},
        {text: 'Uploaded by', value: 'user'},
        {text: 'Upload date', value: 'date'},
        {text: 'Image count', value: 'image_count'},
        {text: 'Actions', value: 'action', sortable: false},
      ],
      user_headers: [
        {text: 'Manga volume', value: 'volume', align: 'center',},
        {text: 'Upload date', value: 'date'},
        {text: 'Image count', value: 'image_count'},
        {text: 'Actions', value: 'action', sortable: false},
      ],
    }),

  }
</script>

<style scoped>
  .disabled {
    color: lightgrey;
    pointer-events: none
  }
</style>
