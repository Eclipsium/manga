import colors from 'vuetify/es5/util/colors'

const axios = require('axios');

// const axiosConfUrl = 'http://localhost:8000';
const axiosConfUrl = 'http://92.63.105.56';


export default {
  mode: 'universal',
  server: {
    host: 'localhost',
    // host: '92.63.105.56',
    port: 3000,
  },
  /*
  ** Headers of the page
  */
  head: {
    titleTemplate: '%s - ' + 'Manga-exhange.ru',
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'}
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: {color: '#34c3eb'},
  /*
  ** Global CSS
  */
  css: [],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    '@nuxtjs/vuetify',
    ['@nuxtjs/google-analytics', {
      id: 'UA-157374239-1'
    }]
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    ['@nuxtjs/axios', { host: '92.63.105.56', port: 80}],
    // ['@nuxtjs/axios', {host: 'localhost', port: 8000}],
    ['nuxt-vuex-localstorage', {
      localStorage: ['user'],  //  If not entered, “localStorage” is the default value
    }],
    ['@nuxtjs/robots', { /* module options */}],
    '@nuxtjs/sitemap',
    ['@nuxtjs/google-adsense', {
      id: 'ca-pub-3545937564525761'
    }]
  ],
  // Sitemap config
  sitemap: [
    {
      path: '/sitemapindex.xml',
      hostname: 'http://manga-exchange.ru',
      gzip: true,
      exclude: [
        '/admin/**'
      ],
      sitemaps: [
        {
          path: '/sitemap-default.xml',
        },
        {
          path: '/sitemap-manga.xml',
          routes: async () => {
            const {data} = await axios.get(axiosConfUrl + '/api/v1/manga/');
            return data.results.map(manga => `/manga/${manga.slug}/`)
          },
          exclude: [
            '/**'
          ],
        },
      ],
    }
  ],
  //Robots config
  robots: [
    {
      UserAgent: '*',
      Sitemap: 'http://manga-exchange.ru/sitemapindex.xml',
      CrawlDelay: 2000,
      Disallow: () => '/admin' // accepts function
    }
  ],

  /*
  ** vuetify module configuration
  ** https://github.com/nuxt-community/vuetify-module
  */
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    }
  }
}
