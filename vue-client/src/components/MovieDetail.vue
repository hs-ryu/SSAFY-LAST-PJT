<template>
  <div>
    <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title">
    {{ movie.title }}
    {{ movie.content }}
    <!-- {{ movie }} -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movie: {},
    }
  },
  methods: {
    getMovieDetail: function() {
      const movieId = this.$route.params.movieId
      console.log(movieId)
      axios({
        url: SERVER.URL + SERVER.ROUTES.getAllMovies + `${movieId}/`,
        method: 'get',
      })
      .then((res) => {
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created: function () {
    this.getMovieDetail()
  }

}
</script>

<style>

</style>