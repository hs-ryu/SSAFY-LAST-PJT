<template>
  <div>
    <!-- <div class="d-flex justify-content-center mb-1 ">
      <div class="card text-center mt-1 border-light">
        <div class="card-body p-0">
          <img :src="'http://image.tmdb.org/t/p/w200/' + searchMovie.poster_path " style="width: 200px;  height: 300px; object-fit: cover;" class="card-img-top rounded mx-auto d-block" alt="" @click="goToDetail">
          <p class="card-title m-0" @click="goToDetail">{{ searchMovie.title }}</p>
        </div>
      </div>
    </div> -->
    <div class="mb-1" @click="goToDetail">
      <div class="card text-center mt-1 border-light">
        <div class="card-body p-0" >
          <div class="hover_effect_box hover_effect_1">
            <div class="content_bg" >
              <img :src="'http://image.tmdb.org/t/p/w200/' + searchMovie.poster_path" style="width: 200px;  height: 300px; object-fit: cover;  z-index: 0;" class="card-img-top rounded mx-auto d-block" alt="">
            </div>
            <div class="caption">
              <p class="caption_title">
                <br>
                {{ searchMovie.title }}
              </p>
              <div class="caption_desc">
                평점 : {{ searchMovie.rank_average.toFixed(1) }}<br>
                개봉일 : {{ searchMovie.release_date }}<br>
                <br>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
export default {
  name: 'SearchMovieItem',
  props: {
    searchMovie: {
      type: Object
    },
  },
  methods: {
    goToDetail: function () {
      const movieId = this.searchMovie.id
      this.$router.push({ name: 'MovieDetail', params: { movieId: movieId}})
    },
    ...mapActions ([
      'fetchMovies'
    ])
  },
  computed: {
    ...mapState([
      'inputValue'
    ])
  },
  updated: function () {
    this.fetchMovies()
  }
}
</script>

<style>

</style>