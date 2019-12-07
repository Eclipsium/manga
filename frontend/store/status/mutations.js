export default {
  setAlert(state, payload) {
    state.alert = payload
  },
  cleanAlert(state) {
    state.alert = false
  },
  onProcess(state, payload) {
    state.process = payload
  },

}
