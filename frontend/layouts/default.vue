<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      class="hidden-lg-and-up"
      temporary
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in loginItems"
          :key="i"
          :to="item.to"
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
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      hide-on-scroll
      dense
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="hidden-lg-and-up"/>
      <v-toolbar-title v-text="title"/>
      <v-spacer/>
      <v-toolbar-items class="hidden-md-and-down">
        <v-btn v-for="(item, i) in loginItems"
               :key="i"
               :to="item.to"
               router
               text
               exact
        >
          <v-icon left>{{item.icon}}</v-icon>

          {{item.title}}
        </v-btn>
      </v-toolbar-items>
      <v-spacer></v-spacer>

      <v-toolbar-items class="hidden-md-and-down" v-if="avatar">
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
            <v-list-item>
              <v-icon left color="error">mdi-exit-to-app</v-icon>
              <v-list-item-title color="error">Exit</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-toolbar-items>
    </v-app-bar>

    <v-content>
      <v-container>
        <nuxt/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    data() {
      return {
        drawer: false,
        loginItems: [
          {
            icon: 'mdi-home',
            title: 'Home',
            to: '/'
          },
          {
            icon: 'mdi-chart-bubble',
            title: 'Catalog',
            to: '/catalog/'
          },
          {
            icon: 'mdi-card-search-outline',
            title: 'Search',
            to: '/search/'
          }
        ],
        profileItems: [
          {title: 'Profile', to: '/profile/', icon: 'mdi-account'},
          {title: 'Bookmarks', to: '/bookmarks/', icon: 'mdi-bookmark'},
        ],
        title: 'Manga-exchange.ru'
      }
    },
    methods: {},
    computed: mapGetters({
      avatar: 'user/getUserAvatar',
      nickname: 'user/getUserNickName',
    }),
  }
</script>
