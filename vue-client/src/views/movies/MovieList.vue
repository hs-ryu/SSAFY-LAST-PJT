<template>
  <div>
    <h1>메인페이지</h1>
    <h2>현재상영중</h2>
    <NowShowingItem
      v-for="(nowShowingMovie, idx) in nowShowingMovies"
      :key="idx"
      :nowShowingMovie="nowShowingMovie"
    />
    <h2>인기영화목록</h2>
    <PopularMovieItem
      v-for="(popularMovie, idx) in popularMovies"
      :key="idx"
      :popularMovie="popularMovie"
    />
    <h2>전체영화목록</h2>
    <MovieItem
      v-for="(movie, idx) in allMovies"
      :key="idx"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem'
import PopularMovieItem from '@/components/PopularMovieItem'
import NowShowingItem from '@/components/NowShowingItem'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'MovieList',
  components: {
    MovieItem,
    PopularMovieItem,
    NowShowingItem,
  },
  methods: {
    ...mapActions([
      'getNowShowing',
    ])
  },
  computed: {
    ...mapState([
      'allMovies',
      'popularMovies',
      'nowShowingMovies',
    ])
  },
  created: function () {
    this.getNowShowing()
  }
}
</script>

<style>

</style>