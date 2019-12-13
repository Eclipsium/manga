<template>
  <v-dialog v-model="dialog" fullscreen hide-overlay dark transition="slide-x-reverse-transition">
    <v-card>
      <v-toolbar dark dense flat>
        <v-toolbar-title>{{title}}</v-toolbar-title>
        <v-spacer/>
        <v-btn icon dark @click="closeDialog()">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-carousel
        hide-delimiters
        :show-arrows="true"
        show-arrows-on-hover
        :continuous="false"
        v-model="currentImageIndex"
      >
        <v-carousel-item
          v-for="(item,i) in items"
          :key="i"
        >
          <template v-slot:default>
            <div class="d-flex justify-center">
              <v-img
                :src="item.src"
                @click="toNextImage()"
                :aspect-ratio="0.7"
                contain
                :max-height="imageHeight"
                class="mr-1"
              >
              </v-img>
              <v-img
                :src="item.src"
                v-if="isHorizontal"
                @click="toNextImage()"
                :aspect-ratio="0.7"
                contain
                :max-height="imageHeight"
                class="ml-1"
              >
              </v-img>
            </div>

          </template>
        </v-carousel-item>
      </v-carousel>
    </v-card>
  </v-dialog>
</template>

<script>
    export default {
        name: "horizontal",
      data: ()=> ({
        currentImageIndex: null,
      }),
      props: ['dialog', 'title', 'items'],
      computed: {
        imageHeight() {
          switch (this.$vuetify.breakpoint.name) {
            case 'xs':
              return '270px'
            case 'sm':
              return '320px'
            case 'md':
              return '500px'
            case 'lg':
              return '700px'
            case 'xl':
              return '800px'
          }
        },
        isHorizontal(){
          return this.$vuetify.breakpoint.width > this.$vuetify.breakpoint.height
        }
      },
      methods: {
        toNextImage() {
          if (this.currentImageIndex + 1 < this.items.length) {
            this.currentImageIndex++
          } else {
            this.closeDialog()
          }
        },
        closeDialog() {
          this.dialog = false;
          this.currentVolume = null;
          this.currentImageIndex = null;
        }
    },
    }
</script>

<style scoped>

</style>
