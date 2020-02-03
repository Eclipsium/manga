<template>
  <v-card
    class="overflow-hidden"
  >
<!--    <v-toolbar-->
<!--      flat-->
<!--      color="primary"-->
<!--    >-->
<!--      <v-icon left color="white">mdi-book-plus</v-icon>-->
<!--      <v-toolbar-title class="headline font-weight-regular white&#45;&#45;text">-->
<!--        Add new Comic-->
<!--      </v-toolbar-title>-->
<!--    </v-toolbar>-->
    <v-card-text class="text-center">
      <v-container>
        <v-form v-model="isValid">
          <v-row>
            <v-col cols="12" md="12">
              <v-text-field
                label="Title"
                v-model="engName"
                :rules="nameRules"
                :disabled="isComplete"
                outlined
              />
            </v-col>
            <v-col cols="12" md="12">
              <v-textarea
                v-model="descriptions"
                :disabled="isComplete"
                outlined
                label="Descriptions (optional)"
              />
            </v-col>
          </v-row>
          <v-row align="center">
            <v-col cols="12" md="3">
              <v-card
                flat
              >
                <v-img
                  :aspect-ratio="9/16"
                  max-height="300"
                  contain
                  :src="imagePreview" v-if="showPreview"
                >
                </v-img>
              </v-card>
              <v-card
                v-if="!showPreview"
                onclick="document.getElementById('imageForm').click()"
                flat
                height="300"
                color="grey lighten-3"
                class="d-flex align-center justify-center clickable"
              >
                <v-icon notranslate style="font-size: 64px;">mdi-image</v-icon>
                <v-subheader>Image preview</v-subheader>
              </v-card>
            </v-col>
            <v-col cols="12" md="9">
              <v-file-input
                @change="handleFileUpload($event)"
                :rules="imageRules"
                :disabled="isComplete"
                type="file"
                ref="imageForm"
                id="imageForm"
                outlined
                accept="image/png, image/jpeg, image/bmp"
                placeholder="Pick manga poster"
                prepend-icon="mdi-camera"
                label="Manga poster"
              />
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
              <v-combobox
                v-model="model"
                :filter="filter"
                :hide-no-data="!search"
                :items="items"
                :search-input.sync="search"
                :disabled="isComplete"
                :rules="artistsRules"
                hide-selected
                label="Artists"
                multiple
                outlined
                small-chips
                clearable
              >
                <template v-slot:no-data>
                  <v-list-item>
                    <span class="subheading">For create</span>
                    <v-chip
                      :color="`${colors[nonce - 1]} lighten-3`"
                      label
                      small
                    >
                      {{ search }}
                    </v-chip>
                    <span>press Enter</span>
                  </v-list-item>
                </template>
                <template v-slot:selection="{ attrs, item, parent, selected }">
                  <v-chip
                    v-if="item === Object(item)"
                    v-bind="attrs"
                    :color="`${item.color} lighten-3`"
                    :input-value="selected"
                    label
                    small
                  >
                    <span class="pr-2">
                      {{ item.text }}
                    </span>
                    <v-icon
                      small
                      @click="parent.selectItem(item)"
                    >mdi-close
                    </v-icon>
                  </v-chip>
                </template>
              </v-combobox>
            </v-col>
          </v-row>
        </v-form>

        <v-btn
          large
          color="primary"
          :disabled="!model.length > 0 || !isValid"
          :loading="isLoading"
          @click="submit"
        >
          <v-icon left>
            mdi-book-plus
          </v-icon>
          Add
        </v-btn>
        <v-snackbar
          v-model="isComplete"
          :color="!mangaMessage ? 'success' : 'error'"
          multi-line
        >
          <p class="text-center">
            {{!mangaMessage ? 'Comic created!' : mangaMessage }}
          </p>
          <v-btn
            v-if="!mangaMessage"
            color="success"
            text
            @click="toMangaPage()"
          >
            To manga page
          </v-btn>
        </v-snackbar>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "addNewMangaComponent",
    data: () => ({
      text: '',
      isValid: true,
      isLoading: false,
      engName: '',
      descriptions: '',
      imageRules: [
        v => !!v || 'Is required',
        v => !v || v.size < 4000000 || 'Poster should less than 4 MB! !',
      ],
      nameRules: [
        v => !!v || 'Is required!',
        v => (v && v.length <= 50) || 'Field must be 20 characters or less.',
        v => (v && v.length > 4) || 'Field must be more then 4 characters.',
      ],
      artistsRules: [
        v => !!v || 'Is required!',
      ],
      activator: null,
      attach: null,
      colors: ['green', 'purple', 'indigo', 'cyan', 'teal', 'orange'],
      index: -1,
      items: [
        {header: 'Select an option or create one'},
      ],
      nonce: 1,
      model: [],
      x: 0,
      search: null,
      y: 0,
      file: '',
      showPreview: false,
      imagePreview: '',
      isComplete: false,
    }),
    methods: {
      toMangaPage() {
        this.$router.push({path: `/manga/${this.mangaSlug}`})
      },
      submit() {
        this.isLoading = true;
        this.$store.commit('manga/setMangaMessage', '');
        let artists = [];
        for (let index in this.model) {
          artists.push(this.model[index]['text'])
        }
        let payload = {
          'english_name': this.engName,
          'japan_name': this.jpnName,
          'descriptions': this.descriptions,
          'poster': this.file,
          'artists': artists,
        };
        this.$axios.setToken('Token ' + this.token);
        this.$store.dispatch('manga/SUBMIT_MANGA_ADD_FORM', payload);
        this.isComplete = true;
        this.isLoading = false;
        setTimeout(() => {
          this.$router.push('/manga/' + this.mangaSlug + '/upload/')
        }, 2000);
      },
      filter(item, queryText, itemText) {
        if (item.header) return false;

        const hasValue = val => val != null ? val : '';

        const text = hasValue(itemText);
        const query = hasValue(queryText);

        return text.toString()
          .toLowerCase()
          .indexOf(query.toString().toLowerCase()) > -1
      },
      handleFileUpload(file) {
        /*
          Set the local file variable to what the user has selected.
        */
        this.file = file;

        /*
          Initialize a File Reader object
        */
        let reader = new FileReader();

        /*
          Add an event listener to the reader that when the file
          has been loaded, we flag the show preview as true and set the
          image to be what was read from the reader.
        */
        reader.addEventListener("load", function () {
          this.showPreview = true;
          this.imagePreview = reader.result;
        }.bind(this), false);

        /*
          Check to see if the file is not empty.
        */
        if (this.file) {
          /*
            Ensure the file is an image file.
          */
          if (/\.(jpe?g|png|gif)$/i.test(this.file.name)) {
            /*
              Fire the readAsDataURL method which will read the file in and
              upon completion fire a 'load' event which we will listen to and
              display the image in the preview.
            */
            reader.readAsDataURL(this.file);
          }
        }
      }
    }
    ,
    computed: {
      ...
        mapGetters({
          token: 'user/getUserToken',
          mangaSlug: 'manga/getSlugOfAddManga',
          mangaMessage: 'manga/getMangaMessage'
        })
    }
    ,
    watch: {
      model(val, prev) {
        if (val.length === prev.length) return;

        this.model = val.map(v => {
          if (typeof v === 'string') {
            v = {
              text: v,
              color: this.colors[this.nonce - 1],
            };

            this.items.push(v);

            this.nonce++
          }

          return v
        })
      },
    },
  }
</script>

<style scoped>

</style>
