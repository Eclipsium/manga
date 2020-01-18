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
            lg="4"
            md="6"
            sm="8"
            xs="12"
          >
            <v-card class="elevation-12">
              <v-toolbar
                color="success"
                dark
                flat
              >
                <v-toolbar-title>Create account</v-toolbar-title>
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
                  <v-text-field
                    v-model="password2"
                    :rules="[comparePassword]"
                    label="Confirm password"
                    prepend-icon="mdi-lock"
                    type="password"
                    required
                  />

                  <v-text-field
                    v-model="nickname"
                    :rules="nameRules"
                    label="Nickname"
                    prepend-icon="mdi-account"
                    type="text"
                    required
                  />
                  <v-checkbox v-model="checkbox" :rules="checkboxRules">
                    <template v-slot:label>
                      <div>
                        I have read and accept the
                        <v-tooltip bottom>
                          <template v-slot:activator="{ on }">
                            <a
                              target="_blank"
                              href="http://manga-exchange.ru/license//"
                              @click.stop
                              v-on="on"
                            >
                              license agreement
                            </a>
                          </template>
                          Opens in new window
                        </v-tooltip>
                      </div>
                    </template>
                  </v-checkbox>
                </v-form>
              </v-card-text>
              <v-card-actions class="mx-4 ">
                <v-btn :to="'/login/'" color="primary" class="mb-4">
                  <v-icon left>mdi-login</v-icon>
                  Have account?
                </v-btn>
                <v-spacer/>
                <v-btn
                  class="mb-4"
                  :disabled="!valid"
                  :loading="onAction"
                  @click="submit"
                  color="success"
                >
                  <v-icon left>mdi-account-plus</v-icon>
                  Create account
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
  </v-app>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "reg",
    layout: 'blank',
    // middleware: 'auth',
    head() {
      return {
        title: 'Create account',
        meta: [
          {hid: 'reg', name: 'description', content: 'Create new account page'}
        ]
      }
    },
    data: () => ({
      snackbar: true,
      checkbox: false,
      valid: false,
      nickname: null,
      nameRules: [
        v => !!v || 'Field required!',
        v => (v && v.length >= 4) || 'Field must be more 3 symbol!'
      ],
      password: null,
      password2: null,
      passwordRules: [
        v => !!v || 'Password required!',
        v => (v && v.length >= 7) || 'Password must be more 8 symbol!'
      ],
      email: '',
      emailRules: [
        v => !!v || 'Email required!',
        v => /.+@.+\..+/.test(v) || 'Email is incorrect!'
      ],
      checkboxRules: [
        v => !!v || 'Need to accept a license agreement',
      ]
    }),
    methods: {
      async submit() {
        if (this.$refs.form.validate()) {
          let payload = {
            "email": this.email,
            "nickname": this.nickname,
            "password": this.password
          };
          await this.$axios.$post('/api/v1/auth/users/', payload)
            .then((res) => {
              this.$store.commit('status/setAlert', {
                'message': 'Account created!',
                'type': 'success'
              });
              setTimeout(() => {
                  this.$store.commit('status/cleanAlert');
                  this.$router.push('/login/');
                },
                1000)
            })
            .catch((e) => {
              let message;
              if (e.response.data.password)
                message = e.response.data.password[0];
              if (e.response.data.email)
                message = e.response.data.email[0];
              if (e.response.data.nickname)
                message = e.response.data.nickname[0];
              this.$store.commit('status/setAlert', {
                'message': message,
                'type': 'error'
              })
            }).finally(() => {
              setTimeout(() => this.$store.commit('status/cleanAlert'), 2000)
            })

        }
      },
    },
    computed: {
      comparePassword() {
        return this.password !== this.password2 ? 'Passwords do not match!' : true
      },
      ...mapGetters({
        onAction: 'status/getProcess',
        isAlert: 'status/getAlert'
      })
    },
    props: {
      source: String
    },
    mounted(){
      this.$store.commit('status/clearAlert')
    }
  }
</script>

<style scoped>

</style>
