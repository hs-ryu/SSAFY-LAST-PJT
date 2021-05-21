<template>
  <div>
    <p>{{ comment.content }}</p>
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
      type: Number,
    },
    reviewId: {
      type: Number,
    }
  },
  methods: {
    deleteComment: function () {
      const commentId = this.comment.id
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/${commentId}/deletecomment/`,
        method: 'delete',
      })
      .then(() => {
        this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
      })
    },
    updateComment: function () {
      // 수정을 어떻게 하지...
    }
  }
}
</script>

<style>

</style>