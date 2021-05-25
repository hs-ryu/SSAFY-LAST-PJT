<template>
  <div>
    <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex">
        <p class="fw-bold me-4">{{ comment.username }}</p>
        <p :class="{hide: modifyActivate}">{{ comment.content }}</p>
        <input style="width: 700px; height: 30px;" :class="{hide: !modifyActivate}" :value="comment.content" @change="updateContent" type="text">
      </div>
      <div class="d-flex">
        <p :class="{hide: modifyActivate}">(작성시각)</p>
        <div v-if="loginedUser==(comment.username)">
          <button class="mx-1 btn btn-sm main-color-background text-white" @click="updateMode">수정</button>
          <button :class="{hide: modifyActivate}" class="mx-1 btn btn-sm main-color-background text-white" @click="deleteComment">삭제</button>
        </div>
      </div>
    </div>
    <!-- <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex">
        <p class="fw-bold me-4">{{ comment.username }}</p>
        <p :class="{hide: modifyActivate}">{{ comment.content }}</p>
        <input style="width: 500px;" :class="{hide: !modifyActivate}" :value="comment.content" @change="updateContent" type="text">
      </div>
      <div class="d-flex">
        <p>(작성시각)</p>
        <div v-if="loginedUser=(comment.username)">
          <button class="mx-1 btn btn-sm main-color-background text-white" @click="updateMode">수정</button>
          <button class="mx-1 btn btn-sm main-color-background text-white" @click="deleteComment">삭제</button>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters, mapState } from 'vuex'

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
  computed: {
    ...mapGetters([
      'config'
    ]),
    ...mapState({
      'loginedUser': 'username'
    }),
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
      const headers = this.config
      const commentId = this.comment.id
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/${commentId}/deletecomment/`,
        method: 'delete',
        headers,
      })
      .then(() => {
        // this.getReviewComments()
        this.$emit('comment-deleted')
        // this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
      })
    },
    updateMode: function () {
      // console.log(this.modifyActivate)
      if (!this.modifyActivate) {
        this.modifyActivate = true // 수정창 열림
        this.$emit('modify-activate')
      } else {
        const commentContent = this.updatedContent ? this.updatedContent : this.comment.content
        // console.log(commentContent)
        const commentItem = {
          content: commentContent,
        }
        if (commentItem.content) {
          const headers = this.config
          const commentId = this.comment.id
          axios({
            url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/${commentId}/updatecomment/`,
            method: 'put',
            data: commentItem,
            headers,
          })
          .then(() => {
            // 여기 필요할듯
            this.$emit('modify-activate')
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