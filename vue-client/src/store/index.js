import Vue from 'vue'
import Vuex from 'vuex'

import SERVER from '@/api/drf.js'
import axios from 'axios'
import router from '../router'

Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    allMovies: [],
    popularMovies: [],
    nowShowingMovies: [],
    authToken: localStorage.getItem('jwt'),
  },
  getters: {
    // 로그인상태 확인 boolean 값
    isLoggedIn: function (state) {
      return state.authToken ? true : false
    },
    config: function (state) {
      return {
        Authorization: `JWT ${state.authToken}`
      }
    }
  },
  mutations: {
    SET_TOKEN: function (state, token) {
      state.authToken = token
      localStorage.setItem('jwt', token)
    },
    REMOVE_TOKEN: function (state) {
      localStorage.removeItem('jwt')
      state.authToken = ''
    },
    GET_ALL_MOVIES: function (state, allmovies) {
      state.allMovies = allmovies
    },
    GET_POPULAR_MOVIES: function (state, popularmovies) {
      state.popularMovies = popularmovies
    },
    GET_NOW_SHOWING: function (state, nowShowingMovies) {
      state.nowShowingMovies = nowShowingMovies
    }
  },
  actions: {
    /* 인증 & 권한 */
    login: function ({ commit }, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.login,
        method: 'post',
        data: credentials,
      })
      .then((res) => {
        commit('SET_TOKEN', res.data.token)
        router.push({ name: 'MovieList' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    logout: function ({ commit }) {
      commit('REMOVE_TOKEN')
      router.push({ name: 'MovieList' })
    },
    signup: function (context, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.signup,
        method: 'post',
        data: credentials,
      })
      .then(() => {
        router.push({ name: 'Login' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    /* 전체 영화 조회 */
    getAllMovies: function ({ commit }) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getAllMovies,
        method: 'get',
      })
      .then((res) => {
        commit('GET_ALL_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    /* 인기 영화 조회 */
    getPopularMovies: function ({ commit }) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getPopularMovies,
        method: 'get'
      })
      .then((res) => {
        commit('GET_POPULAR_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    /* 현재상영중 영화 조회 */
    getNowShowing: function ({ commit }) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getNowShowing,
        method: 'get',
      })
      .then((res) => {
        commit('GET_NOW_SHOWING', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
