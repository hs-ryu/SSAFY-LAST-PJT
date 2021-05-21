<template>
  <div>
    <h1>개별리뷰상세</h1>
    <h3>리뷰 제목: {{ review.title }}</h3>
    <p>영화: {{ movieTitle }}</p>
    <p>평점: {{ review.rank }}</p>
    <p>리뷰 내용: {{ review.content }}</p>
    <button @click="goToUpdate">수정</button>
    <button @click="deleteReview">삭제</button>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

export default {
  name: 'ReviewDetail',
  data: function () {
    return {
      review: {},
      movieTitle: this.$route.query.movieTitle,
      movieId: this.$route.params.movieId,
      reviewId: this.$route.params.reviewId
    }
  },
  methods: {
    getReviewDetail: function () {
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/`,
        method: 'get',
      })
      .then((res) => {
        this.review = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteReview: function () {
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/deletereview/`,
        method: 'delete',
      })
      .then(() => {
        this.$router.push({ name: 'MovieDetail', params: { movieId: this.movieId}})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToUpdate: function () {
      this.$router.push({ name: 'UpdateReview', params: { movieId: this.movieId, reviewId: this.reviewId }, query: { review: this.review }})
    }
  },
  created: function () {
    this.getReviewDetail()
  }
}
</script>

<style>

</style>