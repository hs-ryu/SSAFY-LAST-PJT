<template>
  <div>
    <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex">
        <p class="fw-bold me-4">{{ comment.username }}</p>
        <p :class="{hide: modifyActivate}">{{ comment.content }}</p>
        <input style="width: 550px; height: 30px;" :class="{hide: !modifyActivate}" :value="comment.content" @change="updateContent" type="text">
      </div>
      <div class="d-flex">
        <p :class="{hide: modifyActivate}">(작성시각)</p>
        <div v-if="loginedUser=(comment.username)">
          <button class="mx-1 btn btn-sm main-color-background text-white" @click="updateMode">수정</button>
          <button :class="{hide: modifyActivate}" class="mx-1 btn btn-sm main-color-background text-white" @click="deleteComment">삭제</button>
        </div>
      </div>
    </div>
    <!-- <p :class="{hide: modifyActivate}">{{ comment.content }}</p> -->
    <!-- <p>{{ comment.id }}</p> -->
    <!-- <input :class="{hide: !modifyActivate}" :value="comment.content" @change="updateContent" type="text">
    <button @click="updateMode">수정</button>
    <button @click="deleteComment">삭제</button> -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'ArticleComment',
  props: {
    comment: {
      type: Object,
    },
    articleId: {
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
    ])
  },
  methods: {
    deleteComment: function () {
      const commentId = this.comment.id
      const headers = this.config
      axios({
        // path('articles/<int:article_pk>/comments/<int:comment_pk>/deletecomment/', views.deletecomment, name='deletecomment'),
        url: SERVER.URL + `/community/articles/${this.articleId}/comments/${commentId}/deletecomment/`,
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
          const headers = this.config
          axios({
            // path('articles/<int:article_pk>/comments/<int:comment_pk>/updatecomment/', views.updatecomment, name='updatecomment'),
            url: SERVER.URL + `/community/articles/${this.articleId}/comments/${commentId}/updatecomment/`,
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