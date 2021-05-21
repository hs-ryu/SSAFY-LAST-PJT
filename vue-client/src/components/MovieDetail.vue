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
    <div v-if="reviews">
      <ReviewItem
        v-for="(review, idx) in reviews"
        :key="idx"
        :review="review"
        :movieId="movieId"
        :movieTitle="movie.title"
      />
    </div>
    <div v-else>
      <p>리뷰가 아직 없어요. 리뷰를 작성해주세요!</p>
    </div>
    <button @click="goToCreateReview">리뷰 작성하기</button>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

import ReviewItem from '@/components/ReviewItem'

export default {
  name: 'MovieDetail',
  components: {
    ReviewItem
  },
  data: function () {
    return {
      movie: {},
      movieId: this.$route.params.movieId,
      netflix: '',
      watcha: '',
      wavve: '',
      naver: '',
      reviews: [],
    }
  },
  methods: {
    getMovieDetail: function() {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getAllMovies + `${this.movieId}/`,
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
    },
    getReviews: function() {
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/`,
        method: 'get',
      })
      .then((res) => {
        this.reviews = res.data
      })
    },
    goToCreateReview: function () {
      this.$router.push({ name: 'CreateReview', params: { movieId: this.movieId }, query: { movieTitle: this.movieTitle}})
    }
  },
  created: function () {
    this.getMovieDetail()
    this.getReviews()
  }

}
</script>

<style>

</style>