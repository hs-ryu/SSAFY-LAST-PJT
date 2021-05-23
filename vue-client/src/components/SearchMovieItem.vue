<template>
  <div>
    <div class="d-flex justify-content-center mb-1 ">
      <div class="card text-center mt-1 border-light">
        <div class="card-body p-0">
          <img :src="'http://image.tmdb.org/t/p/w200/' + searchMovie.poster_path " style="width: 200px;  height: 300px; object-fit: cover;" class="card-img-top rounded mx-auto d-block" alt="" @click="goToDetail">
          <p class="card-title m-0" @click="goToDetail">{{ searchMovie.title }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
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
  updated: function () {
    this.fetchMovies()
  }
}
</script>

<style>

</style>