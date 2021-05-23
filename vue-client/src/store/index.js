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
    username: '손님',
    isSuperuser: false,
    userId: -1,
    today: new Date(),

    // 검색
    inputValue: '',
    searchMovies : [],
    
    // 플랫폼 영화
    platformvalue: 'netflix',
    platformMovies : [],
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
    },
    movieLength: function (state) {
      if (state.searchMovies) {
        return state.searchMovies.Length
      }
    },
    inputLength: function (state) {
      if (state.inputValue) {
        return state.inputValue.Length
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
    },

    // 검색
    SET_INPUT_VALUE : function (state, inputValue) {
      state.inputValue = inputValue
    },
    SET_SEARCH_MOVIES: function (state, searchMovies) {
      state.searchMovies = searchMovies
    },
    GET_PLATFORM_MOVIES: function (state, platformMovies) {
      state.platformMovies = platformMovies
    },
    SET_PLATFORM: function(state, platform) {
      state.platformvalue = platform
    },
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
        axios({
          url: SERVER.URL + SERVER.ROUTES.verify_user,
          method: 'post',
          data: {
            token: this.state.authToken,
          }
        })
        .then((res) => {
          console.log(res.data)
          const username = res.data.username ? res.data.username : '손님'
          const userId = res.data.user_id ? res.data.user_id : null
          const issuperuser = res.data.issuperuser ? res.data.issuperuser : false
          this.state.username = username
          this.state.userId = userId
          this.state.isSuperuser = issuperuser
          // console.log(this.state.username)
          // console.log(this.state.userId)
          // console.log(this.state.isSuperuser)
        })
        router.push({ name: 'MovieList' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    get_user_info: function () {
      console.log(this.state)
        axios({
          url: SERVER.URL + SERVER.ROUTES.verify_user,
          method: 'post',
          data: {
            token: this.state.authToken,
          }
        })
        .then((res) => {
          console.log(res.data)
          const username = res.data.username ? res.data.username : '손님'
          const userId = res.data.user_id ? res.data.user_id : null
          const issuperuser = res.data.issuperuser ? res.data.issuperuser : false
          this.state.username = username
          this.state.userId = userId
          this.state.isSuperuser = issuperuser
          console.log(this.state.username)
          console.log(this.state.userId)
          console.log(this.state.isSuperuser)
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
    setPlatform: function ({ commit }, platform) {
      commit('SET_PLATFORM', platform)
      axios({
        url: SERVER.URL + SERVER.ROUTES.getPlatformMovies + platform + '/',
        method: 'get',
      })
      .then((res) => {
        commit('GET_PLATFORM_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    // 검색 
    fetchMovies: function ({ commit, state }, event) {
      commit('SET_INPUT_VALUE', event.target.value)
      axios({
        url: SERVER.URL + SERVER.ROUTES.searchMovies + state.inputValue + '/',
        method: 'get',
      })
      .then((res) => {
        console.log(res)
        commit('SET_SEARCH_MOVIES', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    getPlatformMovies: function ({ commit }, platform) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getPlatformMovies + platform + '/',
        method: 'get',
      })
      .then((res) => {
        commit('GET_PLATFORM_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
