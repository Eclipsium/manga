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
          <v-text-field
            :disabled="!changeNickName"
            label="Имя"
            :value="nickname"
            prepend-icon="mdi-account"
          >
          </v-text-field>
          <v-btn
            color="primary darken-1"
            v-if="!changeNickName"
            @click="changeNickName=!changeNickName"
          >
            Изменить ник
          </v-btn>
          <v-btn
            color="success"
            v-if="changeNickName"
            @click="changeNickName=!changeNickName"
          >
            Сохранить
          </v-btn>
        </v-col>

        <v-col cols="12" md="4">
          <v-form
            v-model="emailValid"
          >
            <v-text-field
              :disabled="!changeEmail"
              :rules="emailRules"
              label="Почта"
              :value="email"
              prepend-icon="mdi-email"
            >
            </v-text-field>
            <v-btn
              color="primary darken-1"
              v-if="!changeEmail"
              @click="changeEmail=!changeEmail"
            >
              Изменить почту
            </v-btn>
            <v-btn
              color="success"
              :disabled="!emailValid"
              v-if="changeEmail"
              @click="changeEmail=!changeEmail"
            >
              Сохранить
            </v-btn>
          </v-form>
        </v-col>
        <!--        Модульное окно смены пароля-->
        <v-col cols="12" md="4" class="align-center">
          <v-btn
            class="mt-2"
            color="warning"
            dark
            @click.stop="changePasswordDialog = true"
          >
            Изменить пароль
          </v-btn>
          <v-dialog
            v-model="changePasswordDialog"
            max-width="600px"

          >
            <v-card>
              <v-card-title class="headline justify-center">Изменение пароля</v-card-title>
              <v-card-text>
                <v-form v-model="passwordValid">
                  <v-col cols="12" sm="12" class="text-center">
                    <v-text-field
                      type="password"
                      label="Старый пароль"
                      :rules="passwordRules"
                      v-model="oldPassword"
                      prepend-icon="mdi-lock-alert"
                      required
                    >
                    </v-text-field>

                    <v-text-field
                      type="password"
                      label="Новый пароль"
                      :rules="passwordRules"
                      v-model="newPassword"
                      prepend-icon="mdi-key"
                      required
                    >
                    </v-text-field>

                    <v-text-field
                      type="password"
                      label="Повторить новый пароль"
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
                  Отмена
                </v-btn>
                <v-spacer/>
                <v-btn
                  class="mr-4"
                  color="success"
                  @click="changePasswordDialog = false"
                  :disabled="!passwordValid"
                >
                  Изменить пароль
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <br>
          <v-btn
            class="mt-4"
            color="error"
            dark
            @click.stop="deleteProfileDialog = true"
          >
            Удалить аккаунт
          </v-btn>
          <v-dialog
            v-model="deleteProfileDialog"
            max-width="600px"
          >
            <v-card>
              <v-card-title class="headline justify-center">Удаление аккаунта</v-card-title>
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
                  Отмена
                </v-btn>
                <v-spacer/>
                <v-btn
                  class="mr-4"
                  color="error"
                  @click="deleteProfileDialog = false"
                >
                  Удалить
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
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
    data() {
      return {
        hasSaved: false,
        isEditing: null,
        model: null,
        changeNickName: false,
        changeEmail: false,
        emailValid: true,
        oldPassword: null,
        newPassword: null,
        newPasswordRepeat: null,
        passwordValid: false,
        changePasswordDialog: false,
        deleteProfileDialog: false,
        emailRules: [
          v => !!v || 'Введите почту!',
          v => /.+@.+\..+/.test(v) || 'Почта введена не правильно!'
        ],
        passwordRules: [
          v => !!v || 'Введите пароль',
          v => (v && v.length >= 6) || 'Пароль должен быть больше 6 символов!'
        ],

        states: [
          {name: 'Florida', abbr: 'FL', id: 1},
          {name: 'Georgia', abbr: 'GA', id: 2},
          {name: 'Nebraska', abbr: 'NE', id: 3},
          {name: 'California', abbr: 'CA', id: 4},
          {name: 'New York', abbr: 'NY', id: 5},
        ],
      }
    },
    computed: {
      comparePassword() {
        return this.newPassword !== this.newPasswordRepeat ? 'Пароли не совпадают!' : null
      },
      ...mapGetters({
                   nickname: 'user/getUserNickName',
                   email: 'user/getUserEmail',
                 }),
    },
    methods: {
    },
  }
</script>

<style scoped>

</style>
