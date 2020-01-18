<template>
  <v-card
    class="overflow-hidden"
  >
    <v-toolbar
      flat
      color="primary"
    >
      <v-icon left color="white">mdi-account</v-icon>
      <v-toolbar-title class="headline font-weight-regular white--text">Profile settings
      </v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-row class="text-center">
        <v-col cols="12" md="6">
          <v-form v-model="nickNameValid">
            <v-text-field
              :disabled="!changeNickName"
              counter="20"
              label="Nickname"
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
        <v-col cols="12" md="6">
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
              disabled
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
        v-if="isAlert"
        v-model="snackbar"
        :color="isAlert.type"
        :timeout="0"
      >
        {{ isAlert.message }}
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
      this.fullNameForChange = this.fullName;
      this.$store.commit('status/cleanAlert')
    },
    data() {
      return {
        hasSaved: false,
        snackbar: true,
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
        imageRules: [
          v => !!v || 'Is required',
          v => !v || v.size < 2000000 || 'Avatars should less than 2 MB! !',
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
        token: 'user/getUserToken',
        avatar: 'user/getUserAvatar',
        id: 'user/getUserId',
        onAction: 'status/getProcess',
        isAlert: 'status/getAlert'
      }),
    },
    methods: {
      async submitNickName() {
        this.$store.commit('status/cleanAlert');
        if(this.nickNameForChange === this.nickname){
          this.changeNickName = false;
          return
        }
        try {
          const data = await this.$axios.$put('/api/v1/auth/users/' + this.id + '/',
            {
              nickname: this.nickNameForChange,
              email: this.emailForChange,
            });
          this.$store.commit('user/setUserNickName', this.nickNameForChange);
          this.$store.commit('status/setAlert', {
            'message': 'Nickname change success',
            'type': 'success'
          })
        } catch (e) {
          this.$store.commit('status/setAlert', {
            'message' :e.response.data.nickname[0],
            'type': 'error',
          })
          this.nickNameForChange = this.nickname
        }
        this.changeNickName = false;
        this.changeEmail = false;
        setTimeout( ()=> (
          this.$store.commit('status/cleanAlert')
        ),2000)
      }
    },
  }
</script>
<style scoped>

</style>
