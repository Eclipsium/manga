<template>
  <v-stepper v-model="step" vertical>
    <v-stepper-step editable :complete="step > 1" step="1">
      Выберите существуюшую мангу
      <small>или создайте новую</small>
    </v-stepper-step>

    <v-stepper-content step="1">
      <v-card class="mb-12">
        <v-card-text>
          выбор манги
        </v-card-text>
      </v-card>
      <v-btn color="success" class="mr-2" @click="step = 2">Далее</v-btn>
      <v-btn text>отмена</v-btn>
    </v-stepper-content>

    <v-stepper-step :complete="step > 2" step="2">Выберите том и часть</v-stepper-step>

    <v-stepper-content step="2">
      <v-btn color="success" class="mr-2" @click="step = 3">Далее</v-btn>
      <v-btn text>отмена</v-btn>
    </v-stepper-content>

    <v-stepper-step :complete="step > 3" step="3">Выберите вариант загрузки</v-stepper-step>
    <v-stepper-content step="3">
      <v-tabs
        v-model="tab"
        grow
      >
        <v-tab
          v-for="item in tabItems"
          :key="item.text"
        >
          <v-icon left>{{item.icon}}</v-icon>
          {{ item.text }}
        </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab">
        <v-tab-item
          v-for="item in tabItems"
          :key="item.text"
        >
          <v-card flat>
            <v-card-text>{{ item.text }}</v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
      <v-btn color="success" class="mr-2" @click="step = 4">Далее</v-btn>
      <v-btn text>отмена</v-btn>
    </v-stepper-content>

    <v-stepper-step step="4">View setup instructions</v-stepper-step>
    <v-stepper-content step="4">
      <v-card color="grey lighten-1" class="mb-12" height="200px"></v-card>
      <v-btn color="primary" @click="step = 1">Continue</v-btn>
      <v-btn text>Cancel</v-btn>
    </v-stepper-content>
  </v-stepper>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
        step: 1,
        model: null,
        isLoading: false,
        search: null,
        tab: null,
        tabItems: [
          {'text': 'Вручную', 'icon': 'mdi-hand'},
          {'text': 'Архивом', 'icon': 'mdi-archive'},
          {'text': 'PDF файлом', 'icon': 'mdi-file-pdf-box'},
        ],
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et ' +
          'dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ' +
          'ea commodo consequat.',
        mangas: [
          {
            "type": "Manga",
            "id": "2",
            "attributes": {
              "russian_name": "asdasdasdasd",
              "english_name": "asdasdasdasd"
            }
          },
          {
            "type": "Manga",
            "id": "1",
            "attributes": {
              "russian_name": "Дракон и Феникс",
              "english_name": "Dragon and Phoenix"
            }
          }
        ],
        computed: {},
      }
    },
  }
</script>

<style scoped>

</style>
