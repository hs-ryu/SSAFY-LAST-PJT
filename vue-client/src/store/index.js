import Vue from 'vue'
import Vuex from 'vuex'

import SERVER from '@/api/drf.js'
import axios from 'axios'

Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    allMovies: [
      { id: 1,
        title: '테스트제목',
      content: '테스트'},
      {title: '테스트제목2',
      content: '테스트2'},
      {title: '테스트제목2',
      content: '테스트2'},
      {title: '테스트제목2',
      content: '테스트2'},
      {title: '테스트제목2',
      content: '테스트2'},
      {title: '테스트제목2',
      content: '테스트2'},
      {title: '테스트제목2',
      content: '테스트2'},
      {title: '테스트제목2',
      content: '테스트2'},
    ],
    popularMovies: [
      {title: '인기영화제목',
      content: '인기영화'},
      {title: '인기영화제목',
      content: '인기영화'},
      {title: '인기영화제목',
      content: '인기영화'},
      {title: '인기영화제목',
      content: '인기영화'},
    ],
    nowShowingMovies: [],
  },
  mutations: {
    GET_ALL_MOVIES: function (state, allmovies) {
      state.allMovies = allmovies
    },
    GET_POPULAR_MOVIES: function (state, popularmovies) {
      state.popularMovies = popularmovies
    },
    GET_NOW_SHOWING: function (state, nowShowingMovies) {
      console.log(nowShowingMovies)
      state.nowShowingMovies = nowShowingMovies
    }
  },
  actions: {
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
    getNowShowing: function ({ commit }) {
      axios({
        url: SERVER.URL + SERVER.ROUTS.getNowShowing,
        method: 'get',
      })
      .then((res) => {
        commit('GET_NOW_SHOWING', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
