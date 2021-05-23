<template>
  <div>
    <!-- 원래 코드 -->
    <!-- 그냥 'http://image.tmdb.org/t/p/w500/'을 함께 DB에 넣는 방식이 나을듯. -->
    <!-- <img :src="'http://image.tmdb.org/t/p/w200/' + movie.poster_path" alt="" @click="goToDetail"> -->
    <!-- <h3 @click="goToDetail">{{ movie.title }}</h3> -->

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
  name: 'MovieItem',
  props: {
    movie: {
      type: Object
    },
  },
  methods: {
    goToDetail: function () {
      const movieId = this.movie.id
      this.$router.push({ name: 'MovieDetail', params: { movieId: movieId}})
    },
    zoomIn: function(event) {
      console.log(event)
    }
  }

}
</script>

<style>

</style>