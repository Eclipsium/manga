<template>
    <v-container>
      <v-card>
        <v-card-title>
          Цель этого сайта
        </v-card-title>
        <v-card-text>
          Этот сайт направлен на изучение и взаимодействие с японским языком и культурой через японскую мангу.
          Администратор отвечает только за поддержание и управление сайтом, а загрузка комиксов выполняется только
          пользователями. Если есть какие-либо нарушения авторских прав, пожалуйста, свяжитесь с администратором.
          Администратор ответит по российскому законодательству.
        </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" class="mb-2" href="mailto:admin@manga-exchange.ru">
          <v-icon left>
            mdi-email
          </v-icon>
          Связаться с администрацией
        </v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
      </v-card>
    </v-container>
</template>

<script>
  export default {
    name: "purpose",
    head() {
      return {
        title: 'Purpose of site',
        meta: [
          {hid: 'purpose', name: 'description', content: 'Purpose page of site'}
        ]
      }
    },
  }
</script>

<style scoped>

</style>
