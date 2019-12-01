<template>
  <v-container fluid>
    <v-row class="fill-height">
      <v-col
        cols="12"
        lg="6">
        <v-row justify="center">
          <p class="display-1">
            {{manga.title}}
          </p>
        </v-row>
        <v-row justify="center">
          <v-img
            :aspect-ratio="9/16"
            :src="manga.src"
            max-height="500"
            max-width="300"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.9)"
          ></v-img>
        </v-row>
        <v-row justify="center" align="center" class="mt-3">
          <span class="title">Рейтинг: </span>
          <v-rating
            v-model="manga.rating"
            background-color="orange lighten-3"
            color="orange"
          ></v-rating>
        </v-row>
        <v-row justify="center" align="center">
          <span>Голосов: 152</span>
          <v-tooltip top>
            <template v-slot:activator="{ on }">
              <v-btn small icon v-on="on" class="ml-2" color="error">
                <v-icon>
                  mdi-chart-areaspline-variant
                </v-icon>
              </v-btn>
            </template>
            <span>Посмотреть голоса</span>
          </v-tooltip>
        </v-row>
        <v-row justify="center" class="mt-3">

          <v-btn color="info">
            <v-icon left>mdi-book</v-icon>
            Читать с начала
          </v-btn>
        </v-row>
      </v-col>
      <v-col
        cols="12"
        lg="6">
        <v-row>
          <p class="title">Описание: </p>
          <p>{{manga.description}}</p>
        </v-row>
        <v-row>
          <p class="title">Томов: {{manga.volume}}</p>
        </v-row>
        <v-row>
          <p class="title">Последний выпуск: {{manga.volume}} - {{ manga.part}}</p>
        </v-row>
        <v-row>
          <v-btn color="success" :to="'/read/' + manga.slug +'/'+ manga.volume +'/' + manga.part">
            <v-icon left>mdi-new-box</v-icon>
            Читать последний выпуск
          </v-btn>
        </v-row>
        <v-row align="center mt-3">
          <p class="title mr-2">Обновленно: </p>
          <p>{{manga.updated}}</p>
          <p class="ml-2">пользователем {{manga.posted}}</p>
        </v-row>
        <v-row align="center">
          <v-chip-group
            column
          >
            <p class="title mr-4">Жанры: </p>
            <v-chip
              v-for="tag in manga.categories" :key="tag"
              label
            >
              {{ tag }}
            </v-chip>
          </v-chip-group>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
    export default {
        name: "index",
        mounted() {
            this.slug = this.$route.params.slug
        },
        data: () => ({
            slug: null,
            manga: {
                title: 'Pre-fab homes asdasd zxcasd',
                description: 'Танджиро - старший сын в семье, потерявшей кормильца. Однажды он уходит в другой город, ' +
                    'чтобы продать древесный уголь, но в конце концов остаётся на ночь в чужом доме, вместо того, ' +
                    'чтобы идти домой. А всё из-за слухов о демоне, который разгуливает в горах под покровом темноты. ' +
                    'Утром парень вернётся домой живым и невредимым... Но его ждут ужасные известия.',
                slug: 'homes',
                categories: ['Ужасы', 'Триллер', 'Театр'],
                posted: 'Abiogenesis',
                author: "Harakiri",
                drawer: 'Harasiri',
                translation: 'Syjabara',
                year: 2019,
                authorLink: '/error',
                updated: '19/11/2019',
                volume: 15,
                part: 125,
                src: 'https://remanga.org/media/manga/tower_of_god/l_head.png',
                rating: 4.5,
                bookmarked: 15
            },
        }),

    }
</script>

<style scoped>

</style>
