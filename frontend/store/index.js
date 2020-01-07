export default {
  actions: {
    async nuxtServerInit ({ state }, { req }) {

      let token = state.user.token;
      if (token) {
        this.$axios.setToken('Token ' + token);
        let userData = null;
        try {
          userData = await this.$axios.$get('http://localhost:8000/api/v1/profile/me/');
        }catch (e) {
          console.log(e)
        }
       if (userData){
         commit('user/setUserData', userData.results[0]);
         commit('user/setAuth', true);
       }
      }
    }
  }
}
