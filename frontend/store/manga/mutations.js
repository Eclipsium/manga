export default {
  setTopManga(store, payload) {
    store.topManga = payload
  },
  setLastManga(store, payload){
    store.lastManga = payload
  },
  setSlugOfAddManga(store, payload){
    store.slugOfAddManga = payload
  },
  setMangaMessage(store, payload){
    store.mangaMessage = payload
  },
  setMangaCatalog(store, payload){
    store.mangaCatalog = payload
  },
  clearMangaCatalog(store){
    store.mangaCatalog = []
  }
}
