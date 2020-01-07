export default {
  setSearchResult(state, payload){
    state.searchResults = payload
  },
  clearSearchResult(state){
    state.searchResults = []
  }
}
