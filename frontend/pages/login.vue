<template>

  <v-app>
    <v-container
      class="fill-height"
      fluid
    >
      <v-snackbar
        v-if="isAlert"
        v-model="snackbar"
        :color="isAlert.type"
        :timeout="0"
      >
        {{ isAlert.message }}
      </v-snackbar>
      <v-row
        align="center"
        justify="center"
      >
        <v-col
          cols="12"
          sm="6"
          md="3"
        >
          <v-card class="elevation-12">
            <v-toolbar
              color="primary"
              dark
              flat
            >
              <v-toolbar-title>Авторизация на сайте</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-form
                ref="form"
                v-model="valid">
                <v-text-field
                  label="Почта"
                  v-model="email"
                  :rules="emailRules"
                  prepend-icon="mdi-email"
                  type="text"
                  required
                />

                <v-text-field
                  v-model="password"
                  :rules="passwordRules"
                  label="Пароль"
                  prepend-icon="mdi-lock"
                  type="password"
                  required
                />
              </v-form>
            </v-card-text>
            <v-card-actions class="mx-4">
              <v-btn color="primary">
                <v-icon left>mdi-account-plus</v-icon>
                Нет аккаунта?
              </v-btn>
              <v-spacer/>
              <v-btn
                :disabled="!valid"
                :loading="onAction"
                @click="submit"
                color="success"
              >
                <v-icon left>mdi-login</v-icon>
                Войти
              </v-btn>
            </v-card-actions>
            <v-container fluid>
              <v-divider/>
              <v-row>

                <v-col
                  cols="12"
                  sm="12"
                  class="py-2"
                  align="center"
                >

                  <p>Войти через социальные сети</p>

                  <v-btn-toggle color="primary">
                    <v-btn>
                      <v-icon>mdi-vk</v-icon>
                    </v-btn>

                    <v-btn>
                      <v-icon>mdi-facebook</v-icon>
                    </v-btn>
                  </v-btn-toggle>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
  import { mapMutations, mapGetters } from 'vuex'
  const Cookie = process.client ? require('js-cookie') : undefined

  export default {
    name: "login",
    layout: 'blank',
    data: () => ({
      snackbar: true,
      text: 'Hello, I\'m a snackbar',
      valid: false,
      password: null,
      passwordRules: [
        v => !!v || 'Введите пароль',
        v => (v && v.length >= 6) || 'Пароль должен быть больше 6 символов!'
      ],
      email: 'abiogenesis70ru@gmail.com',
      emailRules: [
        v => !!v || 'Введите почту!',
        v => /.+@.+\..+/.test(v) || 'Почта введена не правильно!'
      ],
    }),
    methods: {
      submit() {
        if (this.$refs.form.validate()) {
          let store = this.$store;
          let router = this.$router;
          let axios = this.$axios;

          store.commit('status/onProcess', true);
          store.commit('status/cleanAlert');

          const params = new URLSearchParams();
          params.append('email', this.email);
          params.append('password', this.password);

          this.$axios.post('/api/v1/auth/token/login/', params)
            .then(function (response) {
              let token = response.data.data.id;
              store.commit('user/setToken', token);
              Cookie.set('token', token);
              // axios.setToken('Token: ' + response.data.data.id);
              store.commit('user/setAuth', true);
              store.commit('status/setAlert', {
                message: 'Вы успешно вошли!',
                type: 'success'
              });
              setTimeout(() => router.push('/'), 500)
            })
            .catch(function (error) {
              if (error.request) {
                store.commit('status/setAlert', {
                  message: error.response.data.errors[0].detail,
                  type: 'error'
                })
              }
            });
          store.commit('status/onProcess', false)
        }
      },
      to_req() {
        this.$router.push({path: '/reg/'})
      }
    },
    computed: mapGetters({
      onAction: 'status/getProcess',
      isAlert: 'status/getAlert'
    }),
    props: {
      source: String
    }
  }
</script>

<style scoped>

</style>
