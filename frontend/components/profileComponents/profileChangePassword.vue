<template>
  <v-card
    class="overflow-hidden"
  >
    <v-toolbar
      flat
      color="warning"
    >
      <v-icon left color="white">mdi-lock-alert</v-icon>
      <v-toolbar-title class="headline font-weight-regular white--text">
        Setting password and account
      </v-toolbar-title>
    </v-toolbar>
    <v-card-text class="text-center">
      <v-btn
        disabled
        class="mr-2"
        color="warning"
        dark
        @click.stop="changePasswordDialog = true"
      >
        Change password
      </v-btn>
      <v-dialog
        v-model="changePasswordDialog"
        max-width="600px"

      >
        <v-card>
          <v-card-title class="headline justify-center">Change password</v-card-title>
          <v-card-text>
            <v-form v-model="passwordValid">
              <v-col cols="12" sm="6" class="text-center">
                <v-text-field
                  type="password"
                  label="Old password"
                  :rules="passwordRules"
                  v-model="oldPassword"
                  prepend-icon="mdi-lock-alert"
                  required
                >
                </v-text-field>

                <v-text-field
                  type="password"
                  label="New password"
                  :rules="passwordRules"
                  v-model="newPassword"
                  prepend-icon="mdi-key"
                  required
                >
                </v-text-field>

                <v-text-field
                  type="password"
                  label="Repeat new password"
                  :rules="[comparePassword]"
                  v-model="newPasswordRepeat"
                  prepend-icon="mdi-key"
                  required
                >
                </v-text-field>

              </v-col>
            </v-form>
          </v-card-text>
          <v-card-actions class="pb-4">
            <v-btn
              class="ml-4"
              color="error"
              @click="changePasswordDialog = false"
            >
              cancel
            </v-btn>
            <v-spacer/>
            <v-btn
              class="mr-4"
              color="success"
              @click="changePasswordDialog = false"
              :disabled="!passwordValid"
            >
              Change password
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-btn
        disabled
        class="ml-2"
        color="error"
        dark
        @click.stop="deleteProfileDialog = true"
      >
        Delete account
      </v-btn>
      <v-dialog
        v-model="deleteProfileDialog"
        max-width="600px"
      >
        <v-card>
          <v-card-title class="headline justify-center">Delete account</v-card-title>
          <v-card-text>
            <v-col cols="12" sm="12">
              <span class="subtitle">Вы действительно хотите</span>
              <span class="error--text font-weight-bold text-uppercase">удалить</span>
              <span>свой аккаунт? Все ваши файлы, закладки и настройки будут</span>
              <span class="error--text font-weight-bold text-uppercase">полностью удалены</span>
              <span>без возможности восстановления.</span>
              <p>Удалить аккаунт?</p>
            </v-col>
          </v-card-text>
          <v-card-actions class="pb-4">
            <v-btn
              class="ml-4"
              color="success"
              @click="deleteProfileDialog = false"
            >
              cancel
            </v-btn>
            <v-spacer/>
            <v-btn
              class="mr-4"
              color="error"
              @click="deleteProfileDialog = false"
            >
              Delete
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: "profileChangePassword",
    data() {
      return {
        oldPassword: null,
        newPassword: null,
        newPasswordRepeat: null,
        passwordValid: false,
        changePasswordDialog: false,
        deleteProfileDialog: false,
        passwordRules: [
          v => !!v || 'Input password',
          v => (v && v.length >= 6) || 'Password must be more than 6 symbols'
        ],
      }
    },
    computed: {
      comparePassword() {
        return this.newPassword !== this.newPasswordRepeat ? 'Password must be compare!' : null
      },
    }
  }
</script>

<style scoped>

</style>
