<template>
  <v-container fluid fill-height>
    <v-row>
      <v-col cols="12" md="4">
        <v-navigation-drawer
          floating
          permanent
          width="800"
        >
          <v-card flat>
            <v-toolbar
              flat
              color="primary"
            >
              <v-icon left color="white">mdi-filter</v-icon>
              <v-toolbar-title class="headline font-weight-regular white--text">
                Manga filters
              </v-toolbar-title>
            </v-toolbar>
            <v-card-text class="text-center">
              <v-subheader class="title">Sort by:</v-subheader>
              <v-radio-group v-model="radioGroup">
                <v-radio
                  v-for="radio in radioParams"
                  :key="radio.value"
                  :label="radio.label"
                  :value="radio.value"
                />
              </v-radio-group>
              <v-subheader class="title">Sort type:</v-subheader>
              <v-switch
                v-model="isDescending"
                :label="isDescending? 'Descending' : 'Ascending'"
              >
              </v-switch>
              <v-btn large @click="submitFilterButton" color="success" class="mb-4">Filter</v-btn>
            </v-card-text>
          </v-card>
        </v-navigation-drawer>
      </v-col>

      <v-col cols="12" md="8">
        <full-list-manga/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import {mapGetters} from 'vuex'
  import fullListManga from "../../components/fullListManga";

  export default {
    name: "index",
    components: {
      fullListManga,
    },
    methods: {
      async submitFilterButton() {
        this.inProcess = true;
        let data = await this.$axios.$get(this.queueParam);
        if (this.radioGroup === 2) {
          if (this.isDescending) {
            this.$store.commit('manga/setMangaCatalog', data.results.reverse());
          } else {
            this.$store.commit('manga/setMangaCatalog', data.results);
          }
        } else {
          this.$store.commit('manga/setMangaCatalog', data.results);
        }
        this.inProcess = false
      },
    },
    async fetch({store, $axios}) {
      let data = await $axios.$get('/api/v1/manga/?ordering=-rating');
      store.commit('manga/setMangaCatalog', data.results)
    },
    computed: {
      queueParam() {
        let searchType;
        let searchQueue;
        if (this.isDescending) {
          searchType = '-'
        } else {
          searchType = ''
        }
        switch (this.radioGroup) {
          case 1:
            searchQueue = '/api/v1/manga/?ordering=' + searchType + 'rating';
            break;
          case 2:
            searchQueue = '/api/v1/manga/last/';
            break;
          case 3:
            searchQueue = '/api/v1/manga/?ordering=' + searchType + 'is_promoted';
            break;
        }
        return searchQueue
      },
      ...mapGetters({
        mangaData: 'manga/getMangaCatalog'
      })
    },
    data: () => ({
      isDescending: true,
      radioParams: [
        {'label': 'Rating', 'value': 1},
        {'label': 'New added', 'value': 2},
        {'label': 'Recommended', 'value': 3},
      ],
      radioGroup: 1,
    }),
  }
</script>

<style scoped>
</style>
