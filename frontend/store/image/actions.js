export default {
  async LOAD_VOLUME_IMAGE({commit}, volume_pk) {
    const response = await this.$axios.$get('/api/v1/volume/' + volume_pk + '/images/');
    let results = [];
    if (response.results) {
      for (let item of response.results) {
        results.push(item.image)
      }
      commit('setVolumeImage', results)
    }
  }
}
