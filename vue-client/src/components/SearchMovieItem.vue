<template>
  <div>
    <div class="d-flex justify-content-center mb-1 ">
      <div class="card text-center mt-1 border-light">
        <div class="card-body p-0">
          <img :src="'http://image.tmdb.org/t/p/w200/' + movie.poster_path " style="width: 200px;  height: 300px; object-fit: cover;" class="card-img-top rounded mx-auto d-block" alt="" @click="goToDetail">
          <p class="card-title m-0" @click="goToDetail">{{ movie.title }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchMovieItem',
  props: {
    searchMovie: {
      type: Object
    },
  },
  methods: {
    goToDetail: function () {
      const movieId = this.movie.id
      this.$router.push({ name: 'MovieDetail', params: { movieId: movieId}})
    },
  }
}
</script>

<style>

</style>