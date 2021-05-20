<template>
  <div>
    <img :src="movie.poster_path" :alt="movie.title">
    {{ movie.title }}
    {{ movie.content }}
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
      const movieId = this.$route.params
      axios({
        url: SERVER.URL + SERVER.ROUTES.getAllMovies + `/${movieId}/`,
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