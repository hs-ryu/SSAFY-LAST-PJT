<template>
  <div>
    <p :class="{hide: modifyActivate}">{{ comment.content }}</p>
    <!-- <p>{{ comment.id }}</p> -->
    <input :class="{hide: !modifyActivate}" :value="comment.content" @change="updateContent" type="text">
    <button @click="updateMode">수정</button>
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
  data: function () {
    return {
      modifyActivate: false,
      updatedContent: '',
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
    updateMode: function () {
      console.log(this.modifyActivate)
      if (!this.modifyActivate) {
        this.modifyActivate = true // 수정창 열림
        this.$emit('modify-activate')
      } else {
        const commentContent = this.updatedContent ? this.updatedContent : this.comment.content
        console.log(commentContent)
        const commentItem = {
          content: commentContent,
        }
        if (commentItem.content) {
          const commentId = this.comment.id
          axios({
            url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/${commentId}/updatecomment/`,
            method: 'put',
            data: commentItem,
          })
          .then(() => {
          })
          .catch((err) => {
            console.log(err)
          })
        }
        this.modifyActivate = false
        this.$emit('modify-activate')
      }
    },
    updateContent: function (event) {
      this.updatedContent = event.target.value
    }
  },
}
</script>

<style>
.hide {
  display: none;
}
</style>