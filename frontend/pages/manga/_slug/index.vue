<template>
  <v-container fluid>
    <v-row class="fill-height">
      <v-col
        cols="12"
        lg="6">
        <v-row justify="center">
          <p class="display-1">
            {{mangaData.data.attributes.russian_name}}
          </p>
          <p class="subtitle">
            {{mangaData.data.attributes.english_name}}
          </p>
        </v-row>
        <v-row justify="center">
          <v-img
            :aspect-ratio="9/16"
            :src="mangaData.data.attributes.poster"
            max-height="500"
            max-width="300"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.9)"
          />
        </v-row>
        <v-row justify="center" align="center" class="mt-3">
          <span class="title">Рейтинг: </span>
          <v-rating
            v-model="mangaData.data.attributes.rating"
            background-color="orange lighten-3"
            color="orange"
          />
        </v-row>
        <v-row class="justify-center align-center">
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
          <p class="title">Описание:</p>
          <p>{{mangaData.data.attributes.descriptions}}</p>
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
        <v-row class="align-center mt-3">
          <p class="title mr-2">Обновленно: </p>
<!--          <p>{{manga.updated}}</p>-->
<!--          <p class="ml-2">пользователем {{manga.posted}}</p>-->
        </v-row>
        <v-row class="align-center">
          <v-chip-group
            column
          >
            <p class="title mr-4">Жанры: </p>
            <v-chip
              v-for="tag in mangaData.data.attributes.categories" :key="tag"
              label
            >
              {{ CATEGORIES[tag] }}
            </v-chip>
          </v-chip-group>
        </v-row>
        <p>{{mangaData.data.attributes}}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "index",
    async asyncData({$axios, params}) {
      // We can use async/await ES6 feature
      try{
        const mangaData = await $axios.$get('/api/v1/manga/' + params.slug + "/");
        return {mangaData}
      }catch (e) {
        console.log('Server error!')
      }

    },
    computed: mapGetters({
      CATEGORIES: 'manga/getCategories'
    }),
    data: () => ({
    }),

  }
</script>

<style scoped>

</style>
