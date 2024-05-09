import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoggedIn: false
  },
  mutations: {
    setLoggedIn(state, value) {
      state.isLoggedIn = value
    }
  },
  actions: {
    checkLoginState({ commit }) {
      const token = localStorage.getItem('authToken')
      if (token) {
        commit('setLoggedIn', true)
      } else {
        commit('setLoggedIn', false)
      }
    }
  }
})