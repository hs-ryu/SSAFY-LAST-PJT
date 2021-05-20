<template>
  <div>
    <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title">
    {{ movie.title }}
    {{ movie.content }}
    <p>제공하는 플랫폼</p>
    <a v-if="netflix" :href="netflix"><img src="@/assets/netflix_logo.png" alt="netflix logo"></a>
    <a v-if="watcha" :href="watcha"><img src="@/assets/watcha_logo.png" alt="watcha logo"></a>
    <a v-if="wavve" :href="wavve"><img src="@/assets/wavve_logo.png" alt="wavve logo"></a>
    <a v-if="naver" :href="naver"><img src="@/assets/naver_logo.png" alt="naver logo"></a>
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
      netflix: '',
      watcha: '',
      wavve: '',
      naver: '',
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
        this.netflix = res.data.netflix
        this.watcha = res.data.watcha
        this.wavve = res.data.wavve
        this.naver = res.data.naver
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