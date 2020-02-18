export default {
  async SUBMIT_MANGA_ADD_FORM({commit}, payload) {

    const formData = new FormData();
    formData.append('english_name', payload.english_name);
    formData.append('descriptions', payload.descriptions);
    formData.append('poster', payload.poster);
    formData.append('artists', payload.artists);

    await this.$axios.$post('/api/v1/manga/', formData)
      .then(function (res) {
        if (res.slug) {
          commit('setSlugOfAddManga', res.slug)
        }
      }).catch(error => {
        commit('setMangaMessage', 'A manga with the same name already exists.');
      });
  },
  async SUBMIT_MANGA_ARCHIVE({commit}, payload) {}
}
