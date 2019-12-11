export default {
  setAuth(state, payload) {
    state.isAuth = payload
  },
  setUserData(state, payload) {
    state.email = payload.email;
    state.avatar = payload.avatar;
    state.isAdmin = payload.is_staff;
    state.nickname = payload.nickname;
    state.fullName = payload.full_name;
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
  setToken(state, token) {
    state.token = token
  },
  logout(state) {
    state.isAdmin = false;
    state.isAuth = false;
    state.email = null;
    state.photo = null;
    state.token = null;
  },
}
