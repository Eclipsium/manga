<template>
  <v-card
    class="overflow-hidden"
  >
    <v-toolbar
      flat
      color="primary"
    >
      <v-icon left color="white">mdi-account</v-icon>
      <v-toolbar-title class="headline font-weight-regular white--text">Настройки профиля
      </v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-row class="text-center">
        <v-col cols="12" md="4">
          <v-form v-model="nickNameValid">
            <v-text-field
              :disabled="!changeNickName"
              counter="20"
              label="Ник"
              v-model="nickNameForChange"
              :value="nickname"
              :rules="nameRules"
              prepend-icon="mdi-account"
            >
            </v-text-field>
            <v-btn
              color="primary darken-1"
              v-if="!changeNickName"
              @click="changeNickName=!changeNickName"
            >
              Change nickname
            </v-btn>
            <v-btn
              color="success"
              v-if="changeNickName"
              :disabled="!nickNameValid"
              @click="submitNickName"
            >
              Save
            </v-btn>
          </v-form>
        </v-col>

        <v-col cols="12" md="4">
          <v-form v-model="fullNameValid">
            <v-text-field
              :disabled="!changeFullName"
              label="Полное имя"
              counter="20"
              :rules="nameRules"
              v-model="fullNameForChange"
              prepend-icon="mdi-account-circle"
            >
            </v-text-field>
            <v-btn
              color="primary darken-1"
              v-if="!changeFullName"
              @click="changeFullName=!changeFullName"
            >
              Change full name
            </v-btn>
            <v-btn
              color="success"
              :disabled="!fullNameValid"
              v-if="changeFullName"
              @click="submitNickName()"
            >
              Save
            </v-btn>
          </v-form>
        </v-col>
        <v-col cols="12" md="4">
          <v-form
            v-model="emailValid"
          >
            <v-text-field
              :disabled="!changeEmail"
              :rules="emailRules"
              label="Email"
              v-model="emailForChange"
              prepend-icon="mdi-email"
            >
            </v-text-field>
            <v-btn
              color="primary darken-1"
              v-if="!changeEmail"
              @click="changeEmail=!changeEmail"
            >
              Change email
            </v-btn>
            <v-btn
              color="success"
              :disabled="!emailValid"
              v-if="changeEmail"
              @click="changeEmail=!changeEmail"
            >
              Save
            </v-btn>
          </v-form>
        </v-col>
      </v-row>
      <v-snackbar
        v-model="hasSaved"
        :timeout="2000"
        absolute
        bottom
        left
      >
        Your profile has been updated
      </v-snackbar>

    </v-card-text>
  </v-card>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "profileMainConfig",
    mounted() {
      this.$axios.setToken('Token ' + this.token);
      this.nickNameForChange = this.nickname;
      this.emailForChange = this.email;
      this.fullNameForChange = this.fullName
    },
    data() {
      return {
        hasSaved: false,
        isEditing: null,
        changeNickName: false,
        nickNameForChange: null,
        changeEmail: false,
        emailForChange: null,
        changeFullName: false,
        fullNameForChange: null,
        emailValid: true,
        nickNameValid: true,
        fullNameValid: true,
        nameRules: [
          v => !!v || 'Is required!',
          v => (v && v.length <= 20) || 'Field must be 20 characters or less.',
          v => (v && v.length > 5) || 'Field must be more then 5 characters.',
          v => /^(?!\d)(?:(?![@#])[a-zA-Zа-яА-Я\d ])+$/.test(v) ||
            'The field cannot contain special characters and begins with a digit'
        ],
        emailRules: [
          v => !!v || 'Введите почту!',
          v => /.+@.+\..+/.test(v) || 'Email is invalid!'
        ],
      }
    },
    computed: {
      comparePassword() {
        return this.newPassword !== this.newPasswordRepeat ? 'Passwords are not equal!' : null
      },
      ...mapGetters({
        nickname: 'user/getUserNickName',
        email: 'user/getUserEmail',
        fullName: 'user/getUserFullName',
        token: 'user/getUserToken',
      }),
    },
    methods: {
      async submitNickName() {
        try{
          const data = await this.$axios.$put('http://localhost:8000/api/v1/profile/' + this.nickname + '/',
            {
              nickname: this.nickNameForChange,
              email: this.emailForChange,
              full_name: this.fullNameForChange,
            });
          this.$store.commit('user/setUserNickName', this.nickNameForChange);
          this.$store.commit('user/setUserEmail', this.emailForChange);
          this.$store.commit('user/setUserFullName', this.fullNameForChange);
        }catch (e) {
          console.log(e)
        }
        this.changeNickName = false;
        this.changeFullName = false;
        this.changeEmail = false;
      }
    },
  }
</script>
setUserNickName(state, nickname){
state.nickname = nickname
},
setUserEmail(state, email){
state.email = email
},
setUserFullName(state, fullName){
state.fullName = fullName
},
<style scoped>

</style>
