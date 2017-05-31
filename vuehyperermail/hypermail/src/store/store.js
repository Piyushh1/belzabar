import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

/* root state */
const state = {
  count: 1
}

/* getters which is used to extract values from state */
const getters = {
  evenOrOdd: state => state.count % 2 === 0 ? 'even' : 'odd'
}

/* mutate state through mutations only */
const mutations = {
  increment (state) {
    state.count++
  },
  decrement (state) {
    state.count--
  }
}

/* actions that commits mutations to update the state */
const actions = {
  increment: ({ commit }) => commit('increment'),
  decrement: ({ commit }) => commit('decrement'),
  incrementIfOdd: ({ commit, state }) => {
    if ((state.count + 1) % 2 === 0) {
      commit('increment')
    }
  },
  incrementAsync: ({ commit }) => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        commit('increment')
      }, 1000)
    })
  }
}

/* initial store */
export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions,
  plugins: [
    (state) => {
      console.log('plugins called', state)
    }
  ]
})
