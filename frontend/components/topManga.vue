<template>
  <div>
    <v-card
      class="mx-auto"
      flat
    >
      <v-card-text class="title text-center my-4">Популярная манга</v-card-text>
      <v-tabs
        v-model="tab"
        background-color="transparent"
        color="basil"
        grow
      >
        <v-tab
          v-for="item in items"
          :key="item"
        >
          {{ item }}
        </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab">
        <v-tab-item
        >
          <v-container>
            <v-row class="fill-height">
              <v-col
                v-for="card in cards"
                :key="card.title"
                cols="12"
                lg="4"
                md="6"
                sm="12"
              >
                <v-hover v-slot:default="{ hover }">
                  <v-card :elevation="hover ? 12 : 2"
                  >
                    <v-img
                      :src="card.src"
                      :aspect-ratio="16/9"
                      class="white--text align-end"
                      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                      height="200px"
                      @click="toMangaPage(card.mangaUrl)"
                    >
                      <v-card-title v-text="card.title"></v-card-title>
                      <v-expand-transition>
                        <div
                          v-if="hover"
                          class="d-flex transition-fast-in-fast-out info darken-4 v-card--reveal display-5 white--text pa-2"
                          style="height: 100%;"
                        >
                          {{card.description}}
                        </div>
                      </v-expand-transition>
                    </v-img>
                    <v-card-subtitle class="pb-0">
                      Обновлено
                      <span class="subtitle-2 green--text">{{card.updated}}</span>
                      пользователем
                      <a :href="card.authorLink" class="subtitle-2">{{card.author}}</a>
                    </v-card-subtitle>
                    <v-card-actions class="pa-4">
                      Рейтинг:
                      <v-rating
                        v-model="card.rating"
                        background-color="orange lighten-3"
                        color="orange"
                        readonly
                        small
                      ></v-rating>
                      <span class="grey--text text--lighten-2 caption">
                  ({{ card.rating }})
               </span>
                      <v-spacer></v-spacer>
                      <v-badge class="mr-5">
                        <template v-slot:badge>5</template>
                        <v-icon color="error">mdi-cards-heart</v-icon>
                      </v-badge>
                    </v-card-actions>
                  </v-card>
                </v-hover>
              </v-col>
            </v-row>
          </v-container>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="info" class="mb-2">Загрузить еще</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-tab-item>
        <v-tab-item>
          За месяц
        </v-tab-item>
        <v-tab-item>
          За неделю
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </div>
</template>

<script>
    export default {
        name: "lastManga",
        data: () => ({
            cards: [
                {
                    title: 'Pre-fab homes',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: '15',
                    src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
                    rating: 4.5,
                    bookmarked: 15
                },
                {
                    title: 'Favorite road trips',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: '15',
                    src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg',
                    rating: 4.5,
                    bookmarked: 15
                },
                {
                    title: 'Favorite road trips',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: '15',
                    src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg',
                    rating: 4.5,
                    bookmarked: 15
                },
                {
                    title: 'Favorite road trips',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: '15',
                    src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg',
                    rating: 4.5,
                    bookmarked: 15
                },
                {
                    title: 'Best airlines',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: '15',
                    src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg',
                    rating: 4.5,
                    bookmarked: 15
                },
                {
                    title: 'Best airlines',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: '15',
                    src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg',
                    rating: 4.5,
                    bookmarked: 15
                },
            ],
            tab: null,
            items: [
                'За все время', 'За месяц', 'За неделю'
            ],
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        }),
        methods: {
            toMangaPage(url) {
                this.$router.push(url)
            }
        }
    }
</script>

<style scoped>
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .5;
    position: absolute;
    width: 100%;
  }
</style>
