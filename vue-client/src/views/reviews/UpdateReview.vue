<template>
  <div>
    <h1>리뷰 수정</h1>
    <label for="title">글 제목</label>
    <input :value="review.title" @change="updateTitle" type="text" name="title" id="title">
    <label for="rank" min="0.5" max="5" step="0.5">평점</label>
    <input :value="review.rank" @change="updateRank" type="number" name="rank" id="rank">
    <label for="content">글 내용</label>
    <input :value="review.content" @change="updateContent" type="text" name="content" id="content">
    <input @click="updateReview" type="submit" value="리뷰 수정">
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters } from 'vuex'

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
  computed: {
    ...mapGetters([
      'config'
    ])
  },
  methods: {
    updateTitle: function (event) {
      // console.log(event.target.value)
      this.title = event.target.value
      // console.log(this.title)
    },
    updateRank: function (event) {
      this.rank = event.target.value
    },
    updateContent: function (event) {
      this.content = event.target.value
    },
    updateReview: function () {
      const movieId = this.$route.params.movieId
      const reviewId = this.$route.params.reviewId
      const title = this.title ? this.title : this.review.title
      const rank = this.rank ? this.rank : this.review.rank
      const content = this.content ? this.content : this.review.content
      const headers = this.config
      const reviewItem = {
        title,
        rank,
        content,
      }
      console.log(reviewItem.title)
      if (reviewItem.title && reviewItem.rank && reviewItem.content) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.reviews + `${movieId}/reviews/${reviewId}/updatereview/`,
          method: 'put',
          data: reviewItem,
          headers,
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