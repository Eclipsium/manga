<template>
  <v-card class="overflow-hidden">
    <v-toolbar
      flat
      color="success"
    >
      <v-toolbar-title color="success">
        <v-icon left color="white">mdi-face-profile</v-icon>
      </v-toolbar-title>
      <v-toolbar-title class="headline font-weight-regular white--text">Фото профиля
      </v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-container>
        <v-row class="justify-center text-center align-center">
          <v-col cols="12" sm="3">
            <v-avatar size="128" tile>
              <v-img
                :src="avatar"
                aspect-ratio="1"
                class="grey lighten-2"
                max-width="300"
                max-height="300"
              />
            </v-avatar>
          </v-col>
          <v-col cols="12" sm="6" class="text-left">
            <v-form v-model="imageValid">
            <v-file-input
              :rules="imageRules"
              accept="image/png, image/jpeg, image/bmp"
              placeholder="Выберите свой аватар"
              prepend-icon="mdi-camera"
              label="Аватарка"
            />
            </v-form>
          </v-col>
          <v-col cols="12" sm="3">
            <v-btn :disabled="!imageValid" color="success">Сохранить</v-btn>
          </v-col>
        </v-row>
      </v-container>

    </v-card-text>
  </v-card>

</template>

<script>
  import {mapGetters} from 'vuex'
  export default {
    name: "profilePhoto",
    data() {
      return {
        imageValid: false,
        imageRules: [
          value => !value || value.size < 2000000 || 'Аватарка должна быть меньше 2мб!',
        ],
      }
    },
    computed: mapGetters({
      avatar: 'user/getUserAvatar',
      nickname: 'user/getUserNickName',
    }),
  }
</script>

<style scoped>

</style>
