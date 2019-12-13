<template>
  <v-container fluid fill-height>
    <v-row>
      <v-col cols="12" md="4">
        <v-navigation-drawer
          floating
          permanent
          width="800"
        >
          <v-card>
            <v-toolbar
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
              <v-btn large color="success" class="mb-4">Filter</v-btn>
              <v-divider/>

            </v-card-text>
          </v-card>
        </v-navigation-drawer>
      </v-col>

      <v-col cols="12" md="8">
        <v-card>
          <v-toolbar
            flat
            color="success"
          >
            <v-icon left color="white">mdi-settings</v-icon>
            <v-toolbar-title class="headline font-weight-regular white--text">
              Results
            </v-toolbar-title>
          </v-toolbar>

        </v-card>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: "index",
    data: () => ({
      isDescending: true,
      radioParams: [
        {'label': 'Rating', 'value': '1'},
        {'label': 'New added', 'value': '2'},
        {'label': 'Recommended', 'value': '3'},
      ],
      radioGroup: 0,
    })
  }
</script>

<style scoped>

</style>
