<template>
  <v-container>
    <v-row justify="center">
      <v-col
        cols="12"
        lg="6"
        md="8"
        sm="12"
        v-if="mangaComments.count"
      >
        <v-card
          v-for="item in reversedComments.slice((page-1)*10, page*10)"
          :key="item.id"
        >
          <v-card-title
            class="body-2"
          >
            <v-avatar class="mr-2" size="36">
              <img
                :src="item.created_by.avatar"
                :alt="item.created_by.nickname"
              >
            </v-avatar>
            {{item.created_by.nickname}}
            <v-spacer></v-spacer>
            <v-subheader>
              {{ timeExp(item)}} ego
            </v-subheader>
            <v-btn v-if="item.created_by.nickname === nickname || isAdmin"
                   @click="deleteComment(item)"
                   icon small color="error">
              <v-icon small>
                mdi-close
              </v-icon>
            </v-btn>
          </v-card-title>
          <v-card-text class="text-left">
            {{item.comment_text}}
          </v-card-text>
          <v-divider></v-divider>
        </v-card>
      </v-col>
      <v-col cols="12"
             lg="6"
             md="8"
             sm="12"
             v-if="!mangaComments.count"
      >
          <p class="text-center title">
            Comments not found. Be first!
          </p>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col
        cols="12"
        lg="6"
        md="8"
        sm="12"
      >

        <div class="text-center">
          <v-pagination
            v-if="mangaComments.count"
            v-model="page"
            :length="Math.ceil(this.mangaComments.count / 10)"
          ></v-pagination>
        </div>
        <v-container v-if="$store.state.user.isAuth">
          <v-form
            v-model="isValid"
            ref="form"
            lazy-validation
          >
            <v-textarea
              outlined
              label="Leave a comment"
              class="mt-3"
              v-model="commentText"
              :rules="commentRules"
            >
            </v-textarea>
          </v-form>

          <div class="text-center">
            <v-btn color="success" @click="submitComment" :disabled="!isValid || loading">
              <v-icon left>
                mdi-comment
              </v-icon>
              submit
            </v-btn>
          </div>
        </v-container>
        <v-container v-if="!$store.state.user.isAuth">
          <v-subheader class="justify-center text-center">For leave comment you need
            <v-btn :to="'/login/'" small color="success" class="ml-2">
              login
            </v-btn>
          </v-subheader>
        </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "commentComponent",
    props: ['mangaData', 'mangaComments'],
    data() {
      return {
        commentText: '',
        page: 1,
        isValid: true,
        loading: false,
        commentRules: [
          v => !!v || 'Is required!',
          v => (v && v.length > 5) || 'Field must be more then 5 characters.',
          v => (v && v.length < 399) || 'Field must be less then 400 characters.',
        ],
      }
    },
    methods: {
      async submitComment() {
        if (this.$refs.form.validate()) {
          this.loading = true;
          let payload = {
            'manga': this.mangaData.id,
            'comment_text': this.commentText
          };
          await this.$axios.$post('/api/v1/comments/', payload)
            .then((res) => {
              res['created_by'] = {
                'avatar': this.avatar,
                'nickname': this.nickname,
              };
              this.commentText = '';
              this.mangaComments.results.push(res);
              this.mangaComments.count++;
              this.loading = false;
              this.$refs.form.resetValidation()
            })
        }
      },
      async deleteComment(item) {
        await this.$axios.$delete('/api/v1/comments/' + item.id + '/')
          .then(() => {
            this.mangaComments.results = this.mangaComments.results.filter(function (obj) {
              return obj.id !== item.id;
            });
          })
      },
      timeExp(item) {
        let appender = 'days';
        let result = (Date.now() - new Date(item.create_time)) / (1000 * 60 * 60 * 24);
        if (result < 1) {
          result *= 24;
          appender = 'hours';
        }
        if (result < 1) {
          result *= 60;
          appender = 'minutes';
        }
        if (result < 1) {
          result *= 60;
          appender = 'seconds';
        }
        return Math.floor(result) + ' ' + appender
      }
    },
    computed: {
      reversedComments() {
        return this.mangaComments.results.slice(0).reverse();
      },
      ...mapGetters({
        avatar: 'user/getUserAvatar',
        nickname: 'user/getUserNickName',
        isAdmin: 'user/getIsAdmin',
      })
    },
  }
</script>

<style scoped>

</style>
