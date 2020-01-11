<template>
  <v-card class="overflow-hidden">
    <v-toolbar
      flat
      color="success"
    >
      <v-toolbar-title color="success">
        <v-icon left color="white">mdi-face-profile</v-icon>
      </v-toolbar-title>
      <v-toolbar-title class="headline font-weight-regular white--text">User avatar
      </v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-container>
        <v-row class="justify-center text-center align-center">
          <v-col cols="12" sm="3">
            <v-avatar size="128">
              <v-img
                :aspect-ratio="9/16"
                max-height="300"
                rounded
                contain
                :src="showPreview ? imagePreview : avatar"
              >
              </v-img>
            </v-avatar>
          </v-col>
          <v-col cols="12" sm="6" class="text-left">
            <v-form v-model="imageValid">
              <v-file-input
                :rules="imageRules"
                @change="handleFileUpload($event)"
                v-model="image"
                type="file"
                accept="image/png, image/jpeg, image/bmp"
                placeholder="Upload new avatar"
                prepend-icon="mdi-camera"
                label="Avatar"
              />
            </v-form>
          </v-col>
          <v-col cols="12" sm="3">
            <v-btn :disabled="!imageValid" @click="submitAvatar" color="success">Save</v-btn>
          </v-col>
        </v-row>
      </v-container>

    </v-card-text>
  </v-card>

</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "profilePhoto",
    data() {
      return {
        image: null,
        file: null,
        showPreview: false,
        imagePreview: false,
        imageValid: true,
        imageRules: [
          v => !!v || 'Is required',
          v => !v || v.size < 2000000 || 'Avatars should less than 2 MB! !',
        ],
      }
    },
    methods: {
      async submitAvatar() {
        const formData = new FormData();
        formData.append('avatar', this.file);
        await this.$axios.$patch('/api/v1/auth/users/' + this.id + '/', formData)
          .then((res) => {
            this.$store.commit('status/setAlert', {
              'message': 'Avatar updated!',
              'type': 'success'
            });
            this.$store.commit('user/setUserAvatar', res.avatar)
          })
          .catch((e) => {
            this.$store.commit('status/setAlert', {
              'message': e.response.data.avatar[0],
              'type': 'error'
            });
            this.image = null;
          });
        setTimeout(() => (
          this.$store.commit('status/cleanAlert')
        ), 4000)
      },
      handleFileUpload(file) {
        /*
          Set the local file variable to what the user has selected.
        */
        this.file = file;

        /*
          Initialize a File Reader object
        */
        let reader = new FileReader();

        /*
          Add an event listener to the reader that when the file
          has been loaded, we flag the show preview as true and set the
          image to be what was read from the reader.
        */
        reader.addEventListener("load", function () {
          this.showPreview = true;
          this.imagePreview = reader.result;
        }.bind(this), false);

        /*
          Check to see if the file is not empty.
        */
        if (this.file) {
          /*
            Ensure the file is an image file.
          */
          if (/\.(jpe?g|png|gif)$/i.test(this.file.name)) {
            /*
              Fire the readAsDataURL method which will read the file in and
              upon completion fire a 'load' event which we will listen to and
              display the image in the preview.
            */
            reader.readAsDataURL(this.file);
          }
        }

      }
    },
    computed: mapGetters({
      avatar: 'user/getUserAvatar',
      nickname: 'user/getUserNickName',
      id: 'user/getUserId',
      onAction: 'status/getProcess',
      isAlert: 'status/getAlert'
    }),
  }
</script>

<style scoped>

</style>
