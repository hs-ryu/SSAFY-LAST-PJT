<template>
  <div>
    <h1>리뷰 수정</h1>
    <label for="title">글 제목</label>
    <input :value="review.title" type="text" name="title" id="title">
    <label for="rank" min="0.5" max="5" step="0.5">평점</label>
    <input :value="review.rank" type="number" name="rank" id="rank">
    <label for="content">글 내용</label>
    <input :value="review.content" type="text" name="content" id="content">
    <input @click="updateReview(title, rank, content)" type="submit" value="리뷰 수정">
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

export default {
  name: 'UpdateReview',
  data: function () {
    return {
      review: this.$route.query.review,
      title: '',
      rank: 0,
      content: '',
    }
  },
  methods: {
    updateReview: function (title, rank, content) {
      const movieId = this.$route.params.movieId
      const reviewId = this.$route.params.reviewId
      console.log(movieId)
      const reviewItem = {
        title,
        rank,
        content,
      }
      if (reviewItem.title && reviewItem.rank && reviewItem.content) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.reviews + `${movieId}/reviews/${reviewId}/updatereview/`,
          method: 'put',
          data: reviewItem,
        })
        .then(() => {
          // console.log(this.movieId)
          this.title = ''
          this.rank = 0
          this.content = ''
          this.$router.push({ name: 'MovieDetail', params: { movieId: movieId}})
        })
        .catch((err) => {
          console.log(err)
        })
      }
    }
  }
}
</script>

<style>

</style>