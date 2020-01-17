<template>
  <v-app>
    <v-container
      class="fill-height"
      fluid
    >
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
          lg="4"
          md="6"
          sm="8"
          xs="12"
        >
          <v-card class="elevation-12">
            <v-toolbar
              color="primary"
              dark
              flat
            >
              <v-toolbar-title>
                Login
              </v-toolbar-title>
              <v-spacer/>
              <v-btn icon :to="'/'">
                <v-icon>
                  mdi-home
                </v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <v-form
                ref="form"
                v-model="valid">
                <v-text-field
                  label="Email"
                  v-model="email"
                  :rules="emailRules"
                  prepend-icon="mdi-email"
                  type="text"
                  required
                />

                <v-text-field
                  v-model="password"
                  :rules="passwordRules"
                  label="Password"
                  prepend-icon="mdi-lock"
                  type="password"
                  required
                />
                <div  class="text-right">
                  <nuxt-link :to="'/restore/'" class="font-weight-bold">Forgot password?</nuxt-link>
                </div>
              </v-form>
            </v-card-text>
            <v-card-actions class="mx-4">
              <v-btn :to="'/reg/'" color="primary" class="mb-5">
                <v-icon left>mdi-account-plus</v-icon>
                Create account
              </v-btn>
              <v-spacer/>
              <v-btn
                :disabled="!valid"
                class="mb-5"
                :loading="onAction"
                @click="submit"
                color="success"
              >
                <v-icon left>mdi-login</v-icon>
                Login
              </v-btn>
            </v-card-actions>
<!--            <v-container fluid>-->
<!--              <v-divider/>-->
<!--              <v-row>-->

<!--                <v-col-->
<!--                  cols="12"-->
<!--                  sm="12"-->
<!--                  class="py-2"-->
<!--                  align="center"-->
<!--                >-->

<!--                  <p>Social login</p>-->

<!--                  <v-btn-toggle color="primary">-->
<!--                    <v-btn>-->
<!--                      <v-icon>mdi-vk</v-icon>-->
<!--                    </v-btn>-->

<!--                    <v-btn>-->
<!--                      <v-icon>mdi-facebook</v-icon>-->
<!--                    </v-btn>-->
<!--                  </v-btn-toggle>-->
<!--                </v-col>-->
<!--              </v-row>-->
<!--            </v-container>-->
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
  import {mapMutations, mapGetters} from 'vuex'

  export default {
    name: "login",
    layout: 'blank',
    // middleware: 'auth',
    head() {
      return {
        title: 'Login page',
        meta: [
          {hid: 'login', name: 'description', content: 'Login page for manga-exhange.ru'}
        ]
      }
    },
    data: () => ({
      snackbar: true,
      valid: false,
      password: null,
      passwordRules: [
        v => !!v || 'Input password!',
        v => (v && v.length >= 6) || 'Password must be more 6 symbols!!'
      ],
      email: '',
      emailRules: [
        v => !!v || 'Input email!',
        v => /.+@.+\..+/.test(v) || 'Email is incorrect!'
      ],
    }),
    methods: {
      submit() {
        if (this.$refs.form.validate()) {
          let store = this.$store;
          let router = this.$router;

          store.commit('status/onProcess', true);
          store.commit('status/cleanAlert');

          const params = new URLSearchParams();
          params.append('email', this.email);
          params.append('password', this.password);

          this.$axios.setHeader('Authorization', null);

          this.$axios.post('/api/v1/auth/token/login/', params)
            .catch(function (error) {
              store.commit('status/setAlert', {
                message: error.response.data.non_field_errors[0],
                type: 'error'
              })
            })
            .then(function (response) {
              let token = response.data.auth_token;
              store.commit('user/setToken', token);
              store.dispatch('user/GET_USER_DATA', token);
              store.commit('user/setAuth', true);
              store.commit('status/setAlert', {
                message: 'Success!',
                type: 'success'
              });
              setTimeout(() => router.push('/'), 500)
            });

          store.commit('status/onProcess', false)
        }
      },
    },
    computed: mapGetters({
      onAction: 'status/getProcess',
      isAlert: 'status/getAlert'
    }),
    created() {
      this.$store.commit('status/cleanAlert');
    },
  }
</script>

<style scoped>

</style>
