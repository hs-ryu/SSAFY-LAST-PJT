<template>
  <div>
    <!-- {{ movie }} -->
    <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title">
    {{ movie.title }}
    {{ movie.content }}
    <div>
      <p>{{ movie.like_users.length }}명이 좋아합니다.</p>
      <button v-if="movie.like_users.includes(userId)" @click="getLikeStatus">좋아요취소</button>
      <button v-else @click="getLikeStatus">좋아요</button>
    </div>
    <div v-if="movie.trailer">
      <p>트레일러</p>
      <iframe :src="'https://www.youtube.com/embed/' + movie.trailer" frameborder="0" style="display:block; width:100vw; height: 100vh"></iframe>
    </div>

    <p>제공하는 플랫폼</p>
    <a v-if="netflix" :href="netflix"><img src="@/assets/netflix_logo.png" alt="netflix logo"></a>
    <a v-if="watcha" :href="watcha"><img src="@/assets/watcha_logo.png" alt="watcha logo"></a>
    <a v-if="wavve" :href="wavve"><img src="@/assets/wavve_logo.png" alt="wavve logo"></a>
    <a v-if="naver" :href="naver"><img src="@/assets/naver_logo.png" alt="naver logo"></a>
    <!-- {{ movie }} -->
    <div v-if="reviews.length">
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
import { mapGetters, mapState } from 'vuex'

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
  computed: {
    ...mapGetters([
      'config',
    ]),
    ...mapState([
      'userId',
    ])
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
      .catch((err) => {
        console.log(err)
      })
    },
    goToCreateReview: function () {
      this.$router.push({ name: 'CreateReview', params: { movieId: this.movieId }, query: { movieTitle: this.movieTitle}})
    },
    getLikeStatus: function () {
      const headers = this.config
      axios({
        // 'getmovies/<int:movie_pk>/likes/
        url: SERVER.URL + `/movies/getmovies/${this.movieId}/likes/`,
        method: 'post',
        headers,
      })
      .then(() => {
        this.getMovieDetail()
      })
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