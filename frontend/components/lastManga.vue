<template>
  <v-card
    class="mx-auto"
    flat
  >
    <v-card-text class="title text-center">Последние обновления</v-card-text>
    <v-container>
      <v-row class="fill-height">
        <v-col
          v-for="card in cards"
          :key="card.title"
          cols="12"
          lg="2"
          md="4"
          sm="6"
        >
          <v-hover v-slot:default="{ hover }">
            <v-card :elevation="hover ? 12 : 2"
            >
              <v-img
                :src="card.src"
                :aspect-ratio="0.7"
                max-height="500"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.9)"
                @click="toMangaPage(card.mangaUrl)"
              >
                <v-card-title>{{card.title}}: {{card.volume}}-{{card.part}}</v-card-title>
                <v-expand-transition>
                  <div
                    v-if="hover"
                    class="d-flex transition-fast-in-fast-out info darken-4 v-card--reveal display-5 white--text pa-2"
                    style="height: 100%;"
                  >
                    {{card.description}}
                  </div>
                </v-expand-transition>

                <div class="text-center">
                  <v-rating
                    v-model="card.rating"
                    background-color="orange lighten-3"
                    color="orange"
                    readonly
                    half-increments
                    small
                  ></v-rating>
                </div>
              </v-img>
              <v-card-subtitle>
                Обновлено
                <span class="subtitle-2 green--text">{{card.updated}}</span>
                пользователем
                <a :href="card.authorLink" class="subtitle-2">{{card.author}}</a>
              </v-card-subtitle>
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
  </v-card>
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
                    volume: 15,
                    part: 125,
                    src: 'https://remanga.org/media/manga/tower_of_god/l_head.png',
                    rating: 4.5,
                    bookmarked: 15
                },
                {
                    title: 'Pre-fab homes',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: 15,
                    part: 125,
                    src: 'https://remanga.org/media/manga/tower_of_god/l_head.png',
                    rating: 4.5,
                    bookmarked: 15
                },
                {
                    title: 'Pre-fab homes',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: 15,
                    part: 125,
                    src: 'https://remanga.org/media/manga/tower_of_god/l_head.png',
                    rating: 4.5,
                    bookmarked: 15
                },
                {
                    title: 'Pre-fab homes',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: 15,
                    part: 125,
                    src: 'https://remanga.org/media/manga/tower_of_god/l_head.png',
                    rating: 4.5,
                    bookmarked: 15
                },
                {
                    title: 'Pre-fab homes',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: 15,
                    part: 125,
                    src: 'https://remanga.org/media/manga/tower_of_god/l_head.png',
                    rating: 4.5,
                    bookmarked: 15
                },
                {
                    title: 'Pre-fab homes',
                    description: 'Крутое аниме по мотиву одноименного произведения хадео кадзимы',
                    mangaUrl: '/inspire',
                    author: 'Abiogenesis',
                    authorLink: '/error',
                    updated: '19/11/2019',
                    volume: 15,
                    part: 125,
                    src: 'https://remanga.org/media/manga/tower_of_god/l_head.png',
                    rating: 4.5,
                    bookmarked: 15
                },
            ],
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
