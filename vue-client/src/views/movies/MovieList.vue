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
      <h2>NOW SHOWING</h2>
      <!-- <p>{{ nowShowingMovies }}</p> -->
      <div class="card-group">
        <NowShowingItem
          v-for="(nowShowingMovie, idx) in nowShowingMovies"
          :key="idx + '1'"
          :nowShowingMovie="nowShowingMovie"
        />
      </div>
      <h2>{{ today.getHours() }}시의 인기영화</h2>
      <!-- <p>{{ popularMovies }}</p> -->
      <div class="card-group">
        <PopularMovieItem
          v-for="(popularMovie, idx) in popularMovies"
          :key="idx + '2'"
          :popularMovie="popularMovie"
        />
      </div>
      <!-- 플랫폼상영 -->
      <h2>현재 {{ platformvalue }}에서 상영중인 영화입니다</h2>
      <div>
        <div>
          <p class="d-inline mx-3" @click="setPlatform('netflix')">netflix</p>
          <p class="d-inline mx-3" @click="setPlatform('watcha')">watcha</p>
          <p class="d-inline mx-3" @click="setPlatform('wavve')">wavve</p>
          <p class="d-inline mx-3" @click="setPlatform('naver')">naver</p>
        </div>
      </div>
      <div class="card-group">
        <PlatformMovieItem
          v-for="(platformMovie, idx) in platformMovies"
          :key="idx + '3'"
          :platformMovie="platformMovie"
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
import PlatformMovieItem from '@/components/PlatformMovieItem'
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
  name: 'MovieList',
  components: {
    MovieItem,
    PopularMovieItem,
    NowShowingItem,
    SearchMovieItem,
    PlatformMovieItem,
  },
  methods: {
    ...mapActions([
      'getAllMovies',
      'getPopularMovies',
      'getNowShowing',
      'fetchMovies',
      'getPlatformMovies',
      'setPlatform',
      'resetInputValue',
    ])
  },
  computed: {
    ...mapState([
      'allMovies',
      'popularMovies',
      'nowShowingMovies',
      'searchMovies',
      'inputValue',
      'platformMovies',
      'platformvalue',
      'today',
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
    this.getPlatformMovies(this.platformvalue)
    this.resetInputValue()
    console.log(this.inputValue)
  },
}
</script>

<style>

</style>