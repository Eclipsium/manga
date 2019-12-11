<template>
  <v-container>
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
              </v-col>
            </v-row>
          </v-form>
          <v-card-actions>
            <v-btn :disabled="!valid">Upload</v-btn>
          </v-card-actions>
        </v-container>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    name: "index",
    async asyncData({$axios, params}) {
      // We can use async/await ES6 feature
      try {
        const mangaData = await $axios.$get('/api/v1/manga/' + params.slug + "/");
        return {mangaData}
      } catch (e) {
        console.log('Server error!')
      }
    },
    data() {
      return {
        volume: null,
        part: null,
        valid: true,
        archive: null,
        extensions: ['rar', '7z','ace' ,'gz', 'tar', 'zip'],
        digitRules: [
          v => !!v || 'Is required',
          v => /^\d+$/.test(v) || 'Input digit!'
        ],
        archiveRules: [
          v => !!v || 'Is required',
          v => !v || v.size < 200000000 || 'Archive should less than 200 MB! !',
          v => !v || this.extensions.indexOf(v.name.split('.').pop()) !== -1 || 'The archive must contain the correct format!',
        ],
      }
    },
    methods: {
    }
  }
</script>

<
style
scoped >

< /style>
