export default {
  setAuth(state, payload) {
    state.isAuth = payload
  },
  setUserData(state, payload) {
    state.email = payload.email;
    state.avatar = payload.avatar;
    state.isAdmin = payload.is_superuser;
    state.nickname = payload.nickname;
    state.id = payload.id
  },
  setUserNickName(state, nickname){
    state.nickname = nickname
  },
  setUserEmail(state, email){
    state.email = email
  },
  setUserFullName(state, fullName){
    state.fullName = fullName
  },
  setUserAvatar(state, avatar){
    state.avatar = avatar
  },
  setToken(state, token) {
    state.token = token
  },
  logout(state) {
    state.isAdmin = false;
    state.isAuth = false;
    state.email = null;
    state.avatar = null;
    state.token = null;
    state.id = null;
    state.nickname = null;
  },
  seeFirstMessage(state){
    state.isFirstTime = false
  }
}
