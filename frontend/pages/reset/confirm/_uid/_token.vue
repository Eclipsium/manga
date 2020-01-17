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
              color="primary"
              dark
              flat
            >
              <v-toolbar-title>
                Reset password
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
              </v-form>
            </v-card-text>
            <v-card-actions class="mx-4 ">
              <v-spacer/>
              <v-btn
                class="mb-4"
                :disabled="!valid"
                :loading="onAction"
                @click="submit"
                color="success"
              >
                <v-icon left>mdi-account-plus</v-icon>
                Change password
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
    name: "passwordReset",
    layout: 'blank',
    mounted() {
      this.$store.commit('status/cleanAlert');
    },
    head() {
      return {
        title: 'Password reset',
        meta: [
          {hid: 'home', name: 'description', content: 'Password reset page'}
        ]
      }
    },
    data: () => ({
      snackbar: true,
      valid: false,
      password: null,
      password2: null,
      passwordRules: [
        v => !!v || 'Password required!',
        v => (v && v.length >= 8) || 'Password must be more 8 symbol!'
      ],
    }),
    computed: {
      comparePassword() {
        return this.password !== this.password2 ? 'Passwords do not match!' : true
      },
      ...mapGetters({
        onAction: 'status/getProcess',
        isAlert: 'status/getAlert'
      })
    },
    methods: {
      async submit() {
        if (this.$refs.form.validate()) {
          let payload = {
            "uid": this.$route.params['uid'],
            "token": this.$route.params['token'],
            "new_password": this.password
          };
          await this.$axios.$post('/api/v1/auth/users/reset_password_confirm/', payload)
            .then((res) => {
              this.$store.commit('status/setAlert', {
                'message': 'Password changed!',
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
              if (e.response.data.new_password)
                message = e.response.data.new_password[0];
              if (e.response.data.token)
                message = e.response.data.token[0];
              if (e.response.data.uid)
                message = e.response.data.uid[0];
              this.$store.commit('status/setAlert', {
                'message': message,
                'type': 'error'
              })
            }).finally(() => {
              setTimeout(() => this.$store.commit('status/cleanAlert'), 2000)
            })

        }
      },
      mounted() {
        this.$store.commit('status/clearAlert')
      }
    },
    // validate ({ params }) {
    //   // Must be a number
    //   return /^\w+$/.test(params.uid) && /^\w+$/.test(params.token)
    // }
  }
</script>

<style scoped>

</style>
