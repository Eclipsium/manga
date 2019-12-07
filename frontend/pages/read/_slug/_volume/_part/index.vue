<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col class="d-flex" cols="12" sm="2" offset-lg="4" offset-sm="4">
          <v-select
            v-model="select"
            :hint="`${select.attr}: ${select.description}`"
            :items="parts"
            item-text="attr"
            item-value="description"
            label="Выберите часть"
            persistent-hint
            return-object
            single-line
          ></v-select>
        </v-col>
      </v-row>
      <v-row
      >
        <v-col v-for="(image, index) in images"
               :key="index"
               cols="12" md="12"
               justify="center"
               class="pt-0"

        >
          <v-img
            :src="image"
            @click="nextPage()"
            max-height="800"
            contain
            v-if="index === page - 1"
          >
          </v-img>
        </v-col>
      </v-row>
    </v-container>
    <v-footer
      padless
      fixed
    >
      <v-row class="mx-auto" justify="center" align="center" no-gutters>
        <v-col cols="12" sm="6">
          <v-pagination
            v-model="page"
            circle
            total-visible="7"
            :length="this.images.length"
          ></v-pagination>
        </v-col>
        <v-col cols="12" sm="2">
          <v-btn-toggle
            v-model="buttonFooter"
            color="success darken-3"
            multiple
          >
            <v-btn icon>
              <v-icon>mdi-book-open-variant</v-icon>
            </v-btn>
            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-btn-toggle>
        </v-col>
      </v-row>
    </v-footer>
  </div>
</template>

<script>
    export default {
        name: "index",
        computed: {},
        mounted() {
            this.slug = this.$route.params.slug;
            this.volume = this.$route.params.volume;
            this.part = this.$route.params.part;
        },
        watch: {
            volume() {
                this.$router.push('/read/' + this.slug + '/' + this.volume + '/' + this.part)
            },
            // part() {
            //     this.$router.push('/read/' + this.slug + '/' + this.volume + '/' + this.part)
            // }

        },
        methods: {
            nextPage() {
                if (this.images.length - this.page >= 1) {
                    this.page += 1
                } else if (this.part < this.parts.length) {
                    this.part++
                    // } else if (this.volume < this.volumes.length) {
                    //     this.volume++
                }
            },
        },
      data: () => ({
            slug: null,
            volume: null,
            part: null,
            page: 1,
            buttonFooter: [],
            parts: [
                {volume: '1', part:'1', description: 'Пролог'},
                {volume: '1', part:'2', description: 'Пролог'},
                {volume: '1', part:'3', description: 'Пролог'},
                {volume: '1', part:'4', description: 'Пролог'},
                {volume: '1', part:'5', description: 'Пролог'},
            ],
            select: {volume: '1', part:'1', description: 'Пролог'},
            images: [
                'https://javasea.ru/uploads/posts/2018-08/1535400910_devochka-na-ograde-pri-zakate.jpg',
                'https://javasea.ru/uploads/posts/2018-08/1535400884_shut-kuklovod.png',
                'https://javasea.ru/uploads/posts/2018-08/1534928716_chehoslovackaya-volchya-sobaka.jpg',
                'https://javasea.ru/uploads/posts/2018-08/1534928665_chelovek-pod-dozhdem-v-megapolise.jpg',
                'https://javasea.ru/uploads/posts/2018-08/1535400884_shut-kuklovod.png',
                'https://javasea.ru/uploads/posts/2018-08/1535400910_devochka-na-ograde-pri-zakate.jpg',
                'https://javasea.ru/uploads/posts/2018-08/1535400884_shut-kuklovod.png',
                'https://javasea.ru/uploads/posts/2018-08/1534928716_chehoslovackaya-volchya-sobaka.jpg',
                'https://javasea.ru/uploads/posts/2018-08/1534928665_chelovek-pod-dozhdem-v-megapolise.jpg',
                'https://javasea.ru/uploads/posts/2018-08/1534928665_chelovek-pod-dozhdem-v-megapolise.jpg',
            ]
        })
    }
</script>

<style scoped>

</style>
