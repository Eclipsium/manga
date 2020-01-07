export default {
  getUserToken(state) {
    return state.token
  },
  getUserId(state){
    return state.id
  },
  getUserAvatar(state){
    return state.avatar
  },
  getUserEmail(state){
    return state.email
  },
  getUserNickName(state){
    return state.nickname
  },
  getUserFullName(state){
    return state.fullName
  },
  getIsFirstTime(state){
    return state.isFirstTime
  }
};
