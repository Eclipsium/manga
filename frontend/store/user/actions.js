export default {
  LOGOUT({commit}) {
    commit('logout');
    this.$axios.setHeader('Authorization', null)
  },
  async GET_USER_DATA({commit}, token){
    this.$axios.setToken('Token ' + token);
    const userData = await this.$axios.$get('/api/v1/auth/users/me/');
    if (userData){
      commit('setUserData', userData);
      commit('setAuth', true);
    }
  }
}
