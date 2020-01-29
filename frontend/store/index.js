export default {
  actions: {
    async nuxtServerInit ({ state }, { req }) {
      let token = state.user.token;
      if (token) {
        this.$axios.setToken('Token ' + token);
        let userData = null;
        try {
          userData = await this.$axios.$get('/api/v1/auth/users/me/');
        }catch (e) {
          this.$axios.setHeader('Authorization', null);
          commit('logout');
        }
       if (userData['detail']){
         this.$axios.setHeader('Authorization', null);
         commit('logout');
       }else {
         commit('user/setUserData', userData);
         commit('user/setAuth', true);
       }
      }
    }
  }
}
