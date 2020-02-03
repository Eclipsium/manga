<template>
  <v-container>
    <v-card>
      <v-tabs
        v-model="tab"
        background-color="success"
        centered
        dark
        icons-and-text
      >
        <v-tabs-slider></v-tabs-slider>

        <v-tab href="#tab-1">
          Upload next volume
          <v-icon>mdi-page-next-outline</v-icon>
        </v-tab>
        <v-tab href="#tab-2">
          upload the new comic series
          <v-icon>mdi-book-plus</v-icon>
        </v-tab>


      </v-tabs>

      <v-tabs-items v-model="tab">
        <v-tab-item
          :value="'tab-1'"
        >
          <v-card flat>
            <v-card-text>
              <v-row>
                <v-col cols="12" md="6">
                  <v-autocomplete
                    v-model="model"
                    :items="searchResults"
                    :loading="isLoading"
                    :search-input.sync="search"
                    color="primary"
                    placeholder="Start typing to Search"
                    item-text="text"
                    item-value="value"
                    append-icon="mdi-magnify"
                    label="Search"
                    return-object
                    hide-selected
                    clearable
                    outlined
                    dense
                    :hide-no-data="hideNoData"
                  >
                    <template v-slot:{item}>
                      <v-btn color="primary">
                        {{item}}
                      </v-btn>
                      <v-icon right>mdi-magnify</v-icon>
                    </template>
                    <template v-slot:no-data>
                      <v-card flat>
                        <v-subheader>
                          Comic with this name not found. Want to add?
                          <v-btn color="success" class="ml-2" @click='toTab2'>ADD</v-btn>
                        </v-subheader>
                      </v-card>
                    </template>
                  </v-autocomplete>
                </v-col>
                <v-col
                  cols="12" md="6"
                >
                  <v-alert
                    text
                    type="success"
                    dense
                  >
                    Use the search to upload volume to an existing manga
                  </v-alert>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-tab-item>

        <v-tab-item
          :value="'tab-2'"
        >
          <v-card flat>
            <add-new-manga-component></add-new-manga-component>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>

  </v-container>
</template>

<script>
  import addNewMangaComponent from '../../components/addNewMangaComponent'

  export default {
    name: "index",
    components: {
      addNewMangaComponent,
    },
    // middleware: 'notAuth',
    head() {
      return {
        title: 'Add new manga',
        meta: [
          {hid: 'home', name: 'description', content: 'Add new comic page'}
        ]
      }
    },
    data: () => ({
      isLoading: false,
      model: null,
      search: null,
      results: null,
      hideNoData: false,
      searchResults: [],
      tab: null,
    }),
    methods: {
      toTab2() {
        this.hideNoData = true;
        this.tab = 'tab-2';
      }
    },
    watch: {
      async search(val) {
        if (this.isLoading) return;
        if (!this.search) return;

        if (this.search.length > 1) {
          this.isLoading = true;
          await this.$axios.$get('/api/v1/manga/?search=' + this.search)
            .then((response) => {
              if (response.count) {
                let results = [];
                for (let item in response.results) {
                  results.push({'text': response.results[item].english_name, 'value': response.results[item].slug})
                }
                this.searchResults = results;
              }
            }).catch((e) => {

            }).finally(() => {
              setTimeout(() => {
                this.isLoading = false;
                this.hideNoData = false;
              }, 200)
            })
        }
      },
      model() {
        if (this.model) {
          this.$router.push('/manga/' + this.model.value + '/upload/');
          this.searchResults = null;
        }
      },
    },
  }
</script>

<style scoped>
  .clickable {
    cursor: pointer;
  }
</style>
