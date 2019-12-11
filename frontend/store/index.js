const cookieparser = process.server ? require('cookieparser') : undefined;

export default {
  actions: {
    async nuxtServerInit ({ commit }, { req }) {
      let token = null;
      if (req.headers.cookie) {
        const parsed = cookieparser.parse(req.headers.cookie);
        try {
          token = parsed.token;
        } catch (e) {
          console.log(e)
        }
      }
      commit('user/setToken', token);
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
