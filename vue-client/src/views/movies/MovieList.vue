<template>
  <div>
    <h1>메인페이지</h1>
    <div class="d-flex justify-content-center">
      <input @input="fetchMovies" class="form-control m-3 w-75" type="search" placeholder="Search" aria-label="Search">
    </div>
    <div v-if="inputValue">
      <h2>검색결과</h2>
      <div class="card-group">
        <SearchMovieItem
          v-for="(searchMovie, idx) in searchMovies"
          :key="idx + '0'"
          :searchMovie="searchMovie"
        />
      </div>
    </div>
    <div v-else>
      <h2>현재상영중</h2>
      <!-- <p>{{ nowShowingMovies }}</p> -->
      <div class="card-group">
        <NowShowingItem
          v-for="(nowShowingMovie, idx) in nowShowingMovies"
          :key="idx + '1'"
          :nowShowingMovie="nowShowingMovie"
        />
      </div>
      <h2>인기영화목록</h2>
      <!-- <p>{{ popularMovies }}</p> -->
      <div class="card-group">
        <PopularMovieItem
          v-for="(popularMovie, idx) in popularMovies"
          :key="idx + '2'"
          :popularMovie="popularMovie"
        />
      </div>
      <h2>전체영화목록</h2>
      <div class="card-group">
        <MovieItem
          v-for="(movie, idx) in allMovies"
          :key="idx + '3'"
          :movie="movie"
        />
      </div>
    </div>
      
  </div>
</template>
<script>
import MovieItem from '@/components/MovieItem'
import PopularMovieItem from '@/components/PopularMovieItem'
import NowShowingItem from '@/components/NowShowingItem'
import SearchMovieItem from '@/components/SearchMovieItem'
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
  name: 'MovieList',
  components: {
    MovieItem,
    PopularMovieItem,
    NowShowingItem,
    SearchMovieItem,
  },
  methods: {
    ...mapActions([
      'getAllMovies',
      'getPopularMovies',
      'getNowShowing',
      'fetchMovies',
    ])
  },
  computed: {
    ...mapState([
      'allMovies',
      'popularMovies',
      'nowShowingMovies',
      'searchMovies',
      'inputValue',
    ]),
    ...mapGetters([
      'movieLength',
      'inputLength',
    ])
  },
  created: function () {
    this.getNowShowing()
    this.getAllMovies()
    this.getPopularMovies()
  },
}
</script>

<style>

</style>