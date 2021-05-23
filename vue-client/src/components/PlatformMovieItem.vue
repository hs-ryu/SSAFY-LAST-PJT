<template>
  <div class="d-flex justify-content-center mb-1 ">
      <div class="card text-center mt-1 border-light">
        <div class="card-body p-0">
          <img :src="'http://image.tmdb.org/t/p/w200/' + platformMovie.poster_path " style="width: 200px;  height: 300px; object-fit: cover;" class="card-img-top rounded mx-auto d-block" alt="" @click="goToDetail">
          <p class="card-title m-0" @click="goToDetail">{{ platformMovie.title }}</p>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'PlatformMovieItem',
  props: {
    platformMovie: {
      type: Object,
    }
  },
  methods: {
    goToDetail: function () {
      const popularMovieId = this.platformMovie.id
      this.$router.push({ name: 'MovieDetail', params: { movieId: popularMovieId}})
    }
  }
}
</script>

<style>

</style>