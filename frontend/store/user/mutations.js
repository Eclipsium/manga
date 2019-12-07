export default {
  setAuth(state, payload) {
    state.isAuth = payload
  },
  setUserData(state, payload) {
    state.email = payload.email;
    state.avatar = payload.avatar;
    state.isAdmin = payload.is_staff;
    state.nickname = payload.nickname;
  },
  setToken(state, token) {
    state.token = token
  },
  logout(state) {
    state.isModerator = false;
    state.isAdmin = false;
    state.isAuth = false;
    state.email = null;
    state.photo = null;
    state.token = null;
  },
}
