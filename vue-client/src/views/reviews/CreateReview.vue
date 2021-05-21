<template>
  <div>
    <h1>리뷰 작성</h1>
    <p>영화제목: {{ movieTitle }}</p>
    <form action="">
      <label for="title">글 제목</label>
      <input v-model.trim="title" type="text" name="title" id="title">
      <label for="rank" min="0.5" max="5" step="0.5">평점</label>
      <input v-model="rank" type="number" name="rank" id="rank">
      <label for="content">글 내용</label>
      <input v-model.trim="content" type="text" name="content" id="content">
      <input @click="createReview(title, rank, content)" type="submit" value="리뷰 작성">
    </form>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

export default {
  name: 'CreateReview',
  data: function () {
    return {
      title: '',
      rank: 0,
      content: '',
      movieId: this.$route.params.movieId,
      movieTitle: this.$route.query.movieTitle,
    }
  },
  methods: {
    createReview: function (title, rank, content) {
      const reviewItem = {
        title,
        rank,
        content,
      }
      if (reviewItem.title && reviewItem.rank && reviewItem.content) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/createreview/`,
          method: 'post',
          data: reviewItem,
        })
        .then(() => {
          this.$router.push({ name: 'MovieDetail', params: { movieId: this.movieId}})
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