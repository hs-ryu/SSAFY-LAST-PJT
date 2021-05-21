<template>
  <div>
    <p>{{ comment.content }}</p>
    <p>{{ comment.id }}</p>
    <button @click="updateComment">수정</button>
    <button @click="deleteComment">삭제</button>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

export default {
  name: 'ReviewComment',
  props: {
    comment: {
      type: Object,
    },
    movieId: {
      type: String,
    },
    reviewId: {
      type: String,
    }
  },
  methods: {
    getReviewComments: function () {
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/getcomments/`,
        method: 'get',
      })
      .then((res) => {
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteComment: function () {
      const commentId = this.comment.id
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/${commentId}/deletecomment/`,
        method: 'delete',
      })
      .then(() => {
        // this.getReviewComments()
        this.$emit('comment-deleted')
        // this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
      })
    },
    updateComment: function () {
      // 수정을 어떻게 하지...
    }
  },
}
</script>

<style>

</style>