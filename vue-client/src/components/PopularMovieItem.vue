<template>
  <div>
    <!-- 원래 코드 -->
    <!-- <img :src="'http://image.tmdb.org/t/p/w200/' + popularMovie.poster_path" alt="" @click="goToDetail">
    <h3 @click="goToDetail">{{ popularMovie.title }}</h3>
    <p>{{ popularMovie.content }}</p> -->

    <div class="d-flex justify-content-center mb-1 ">
      <div class="card text-center mt-1 border-light">
        <div class="card-body p-0">
          <img :src="'http://image.tmdb.org/t/p/w200/' + popularMovie.poster_path " style="width: 200px;  height: 300px; object-fit: cover;" class="card-img-top rounded mx-auto d-block" alt="" @click="goToDetail">
          <p class="card-title m-0" @click="goToDetail">{{ popularMovie.title }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PopularMovieItem',
  props: {
    popularMovie: {
      type: Object,
    }
  },
  methods: {
    goToDetail: function () {
      const popularMovieId = this.popularMovie.id
      this.$router.push({ name: 'MovieDetail', params: { movieId: popularMovieId}})
    }
  }

}
</script>

<style>

</style>