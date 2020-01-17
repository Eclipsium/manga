<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      class="hidden-lg-and-up"
      temporary
      app
    >
      <v-list>
        <div class="ma-2 mb-0 pb-0">
          <v-autocomplete
            v-model="model"
            :items="searchResults"
            :loading="isLoading"
            :search-input.sync="search"
            color="primary"
            item-text="text"
            item-value="value"
            append-icon="mdi-magnify"
            label="Search"
            return-object
            hide-selected
            clearable
            outlined
            dense
            hide-no-data
          >
          </v-autocomplete>
        </div>
        <client-only>
          <v-list-item
            :to="'/profile/'"
            v-if="avatar"
          >
            <v-list-item-avatar size="30">
              <v-img :src="avatar"/>
            </v-list-item-avatar>
            <v-list-item-title>{{nickname}}</v-list-item-title>
          </v-list-item>
        </client-only>
      </v-list>
      <v-list dense class="pt-0">
        <v-list-item
          v-for="(item, i) in loginItems"
          :key="i"
          :to="item.to"
          :color="item.color ? item.color : ''"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title"/>
          </v-list-item-content>
        </v-list-item>
        <client-only>
          <v-list-item
            v-if="$store.state.user.isAuth"
            router
            exact
            @click="logout"
          >
            <v-list-item-action>
              <v-icon color="error">mdi-exit-to-app</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title color="error">Exit</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item
            :to="'/login/'"
            v-if="!$store.state.user.isAuth"
            router
            exact
          >
            <v-list-item-action>
              <v-icon color="primary">mdi-exit-to-app</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title color="primary">Login</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </client-only>
      </v-list>
    </v-navigation-drawer>
    <client-only>
      <v-app-bar
        app
        hide-on-scroll
      >
        <v-app-bar-nav-icon @click="drawer = !drawer" class="hidden-lg-and-up"/>
        <v-toolbar-title v-text="title"/>
        <v-spacer/>
        <v-toolbar-items class="hidden-md-and-down">
          <client-only>
            <v-btn v-for="(item, i) in $store.state.user.isAuth ? loginItems: logoutItems"
                   :key="i"
                   :to="item.to"
                   :color="item.color ? item.color : ''"
                   class="mx-1"
                   router
                   text
                   exact
            >
              <v-icon left>{{item.icon}}</v-icon>
              {{item.title}}
            </v-btn>
          </client-only>
        </v-toolbar-items>
        <v-toolbar-items class="hidden-md-and-down align-end mx-1 mt-7">
          <v-autocomplete
            v-model="model"
            :items="searchResults"
            :loading="isLoading"
            :search-input.sync="search"
            color="primary"
            placeholder="Start typing to Search"
            item-text="text"
            item-value="value"
            append-icon="mdi-magnify"
            label="Search"
            return-object
            hide-selected
            clearable
            outlined
            dense
            hide-no-data
          >
            <template v-slot:{item}>
              <v-btn color="primary">
                {{item}}
              </v-btn>
              <v-icon right>mdi-magnify</v-icon>
            </template>
          </v-autocomplete>
        </v-toolbar-items>
        <v-spacer/>
        <client-only>
          <v-toolbar-items>
            <v-btn
              :to="'/login/'"
              v-if="!$store.state.user.isAuth"
              color="primary"
            >
              login
            </v-btn>
          </v-toolbar-items>
          <v-toolbar-items class="hidden-md-and-down" v-if="$store.state.user.isAuth">
            <v-menu offset-y>
              <template v-slot:activator="{ on }">
                <v-btn text v-on="on">
                  <v-list-item>
                    <v-list-item-avatar size="36">
                      <v-img :src="avatar"/>
                    </v-list-item-avatar>
                    <v-list-item-subtitle>{{nickname}}</v-list-item-subtitle>
                    <v-list-item-action>
                      <v-icon>mdi-menu-down</v-icon>
                    </v-list-item-action>
                  </v-list-item>
                </v-btn>
              </template>
              <v-list>
                <v-list-item
                  v-for="(item, i) in profileItems"
                  :key="i"
                  :to="item.to"

                >
                  <v-icon left>{{item.icon}}</v-icon>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
                <v-divider/>
                <v-list-item @click="logout" v-if="$store.state.user.isAuth">
                  <v-icon left color="error">mdi-exit-to-app</v-icon>
                  <v-list-item-title color="error">Exit</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-toolbar-items>
        </client-only>
      </v-app-bar>
    </client-only>
    <v-content>
      <v-container fluid>
        <nuxt/>
      </v-container>
    </v-content>
    <footer-component/>
  </v-app>
</template>

<script>
  import {mapGetters} from 'vuex'
  import footerComponent from '../components/footerComponent'

  export default {
    components: {
      footerComponent,
    },
    data() {
      return {
        isLoading: false,
        model: null,
        search: null,
        results: null,
        searchResults: [],

        drawer: false,
        loginItems: [
          {
            icon: 'mdi-home',
            title: 'Home',
            to: '/',
          },
          {
            icon: 'mdi-chart-bubble',
            title: 'All comics',
            to: '/manga/'
          },
          {
            icon: 'mdi-book-plus',
            title: 'Add comics',
            to: '/add/',
            color: 'success'
          }
        ],
        logoutItems: [
          {
            icon: 'mdi-home',
            title: 'Home',
            to: '/',
          },
          {
            icon: 'mdi-chart-bubble',
            title: 'All comics',
            to: '/manga/'
          },
        ],
        profileItems: [
          {title: 'My profile', to: '/profile/', icon: 'mdi-account'},
        ],
        title: 'Manga-exchange.ru'
      }
    },
    methods: {
      logout() {
        this.$store.dispatch('user/LOGOUT');
        this.$router.push('/')
      }
    },
    watch: {
      async search(val) {
        if (this.isLoading) return;
        if (!this.search) return;

        if (this.search.length > 3) {
          this.isLoading = true;
          await this.$axios.$get('/api/v1/manga/?search=' + this.search)
            .then((response) => {
              if (response.count) {
                let results = [];
                for (let item in response.results) {
                  results.push({'text': response.results[item].english_name, 'value': response.results[item].slug})
                }
                this.searchResults = results;
              }
            }).catch((e) => {

            }).finally(() => {
              setTimeout(() => {
                this.isLoading = false;
              }, 200)
            })
        }
      },
      model() {
        if (this.model) {
          this.$router.push('/manga/' + this.model.value + '/');
          this.searchResults = null;
        }
      }
    },
    computed: {
      ...
        mapGetters({
          avatar: 'user/getUserAvatar',
          nickname: 'user/getUserNickName',
        }),
    }
    ,
  }
</script>
