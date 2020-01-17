<template>
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
            color="warning"
            dark
            flat
          >
            <v-toolbar-title>
              Restore password
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
            </v-form>
          </v-card-text>
          <v-card-actions class="mx-4">
            <v-spacer/>
            <v-btn
              :disabled="!valid"
              class="mb-5"
              :loading="onAction"
              @click="submit"
              color="success"
            >
              Restore
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "restore",
    head() {
      return {
        title: 'Restore password',
        meta: [
          {hid: 'home', name: 'description', content: 'Password reset page'}
        ]
      }
    },
    data: () => ({
      snackbar: true,
      valid: false,
      email: '',
      emailRules: [
        v => !!v || 'Input email!',
        v => /.+@.+\..+/.test(v) || 'Email is incorrect!'
      ],
    }),
    computed: mapGetters({
      onAction: 'status/getProcess',
      isAlert: 'status/getAlert'
    }),
    created() {
      this.$store.commit('status/cleanAlert');
    },
    methods: {
      async submit() {
        if (this.$refs.form.validate()) {
          await this.$axios.$post('/api/v1/auth/users/reset_password/', {'email': this.email})
            .then(()=>{
              this.$store.commit('status/setAlert', {
                'message': 'We sent an email with a password reset link',
                'type': 'success'
              });
              setTimeout(() => this.$router.push('/'), 2000)
            }).catch((e)=> {
                let message = e.response.data.email[0];
              this.$store.commit('status/setAlert', {
                'message': message,
                'type': 'error'
              })
            })
            .finally(() => {
              setTimeout(() => (
                setTimeout(() => this.$store.commit('status/cleanAlert'), 2000)
              ), 2000)
            })
        }
      }
    }
  }
</script>

<style scoped>

</style>
