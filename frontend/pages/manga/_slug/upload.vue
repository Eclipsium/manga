<template>
  <v-container>
    <client-only>
      <v-card
        class="overflow-hidden"
      >
        <v-toolbar
          flat
          color="success"
        >
          <v-icon left color="white">mdi-message-plus</v-icon>
          <v-toolbar-title class="headline font-weight-regular white--text">
            Add new part for "{{mangaData.english_name}}"
          </v-toolbar-title>
        </v-toolbar>
        <v-card-text>
          <v-container>
            <v-form v-model="valid">
              <v-row>
                <v-col cols="12" md="6">
                  <v-text-field
                    v-model="volume"
                    :rules="digitRules"
                    label="Volume"
                    placeholder="Enter volume"
                  />
                </v-col>
                <v-col cols="12" md="6">
                  <v-file-input
                    :rules="archiveRules"
                    v-model="archive"
                    type="file"
                    small-chips
                    accept=".rar, .7z, .ace, .gz, .tar, .zip"
                    :placeholder="'Support: ' + extensions.join(', ')"
                    prepend-icon="mdi-archive"
                    label="Archive to upload"
                  >
                    <template v-slot:selection="{ text }">
                      <v-chip
                        small
                        label
                        color="primary"
                      >
                        {{ text }}
                      </v-chip>
                    </template>
                  </v-file-input>
                  <v-progress-linear rounded v-if="uploadPercentage" v-model="uploadPercentage"/>
                </v-col>
              </v-row>
            </v-form>
            <v-alert
              :type="alert.type"
              v-if="alert"
            >
              {{alert.message}}
            </v-alert>
            <v-card-actions>
              <v-spacer/>
              <v-btn
                color="primary"
                class="mt-2"
                :disabled="!valid"
                :loading="uploadPercentage > 0 && uploadPercentage !== 100"
                @click="submit"
              >
                <v-icon left>
                  mdi-plus-circle
                </v-icon>
                Upload
              </v-btn>
              <v-spacer/>
            </v-card-actions>
          </v-container>
        </v-card-text>
      </v-card>
    </client-only>
  </v-container>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "addMangaVolume",
    middleware: 'notAuth',
    head() {
      return {
        title: 'Add volume for ' + this.mangaData.english_name,
        meta: [
          {hid: 'home', name: 'description', content: 'Add new volume for ' + this.mangaData.english_name}
        ]
      }
    },
    async asyncData({$axios, params}) {
      // We can use async/await ES6 feature
      try {
        const mangaData = await $axios.$get('/api/v1/manga/' + params.slug + "/");
        return {mangaData}
      } catch (e) {
        console.log(e)
      }
    },
    data() {
      return {
        volume: null,
        valid: true,
        archive: null,
        uploadPercentage: 0,
        extensions: ['rar', '7z', 'ace', 'gz', 'tar', 'zip'],
        digitRules: [
          v => !!v || 'Is required',
          v => /^\d+$/.test(v) || 'Input digit!'
        ],
        archiveRules: [
          v => !!v || 'Is required',
          v => !v || v.size < 250000000 || 'Archive should less than 250 MB! !',
          v => !v || this.extensions.indexOf(v.name.split('.').pop()) !== -1 || 'The archive must contain the correct format!',
        ],
      }
    },
    methods: {
      async submit() {
        this.$store.commit('status/onProcess', true);
        this.$store.commit('status/cleanAlert');
        this.valid = false;
        let router = this.$router;

        this.$axios.setToken('Token ' + this.token);

        const formData = new FormData();
        formData.append('volume', this.volume);
        formData.append('archive', this.archive);
        formData.append('manga', this.mangaData.id);

        let store = this.$store;

        await this.$axios.$post('/api/v1/manga/add/', formData,
          {
            onUploadProgress: function (progressEvent) {
              this.uploadPercentage = parseInt(Math.round((progressEvent.loaded / progressEvent.total) * 100));
            }.bind(this)
          }
        ).then(function () {
          let payload = {
            'type': 'success',
            'message': 'Manga volume has been added!'
          };
          store.commit('status/setAlert', payload);
          setTimeout(function () {
            router.go(-1)
          }, 1000)
        }).catch((res) => {
          let payload = {
            'type': 'error',
            'message': res.response.data[0]
          };
          console.log(res);
          store.commit('status/setAlert', payload);
          this.archive = null
        })
          .finally(() => {
            store.commit('status/onProcess', false);
          })
      }
    },
    mounted() {
      this.$store.commit('status/cleanAlert');
    },
    computed: {
      ...mapGetters({
        token: 'user/getUserToken',
        alert: 'status/getAlert',
        onProcess: 'status/getProcess'
      })
    }
  }
</script>

<style scoped>
</style>
