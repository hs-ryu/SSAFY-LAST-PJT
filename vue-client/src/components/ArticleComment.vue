<template>
  <div class="my-1">
    <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex align-items-center">
        <span class="fw-bold me-4">{{ comment.username }}</span>
        <span :class="{hide: modifyActivate}">{{ comment.content }}</span>
        <input style="width: 550px; height: 30px;" :class="{hide: !modifyActivate}" :value="comment.content" @change="updateContent" type="text">
        <span class="fw-bold mx-2" :class="{hide: !modifyActivate}" @click="updateMode">수정</span>
      </div>
      <div class="d-flex align-items-center">
        <span :class="{hide: modifyActivate}">(작성시각)</span>
        <div class="d-flex" v-if="decoded.username==comment.username">
          <span class="fw-bold mx-1" :class="{hide: modifyActivate}" @click="updateMode">수정</span>
          <span :class="{hide: modifyActivate}" class="fw-bold mx-1">|</span>
          <span class="fw-bold mx-1" :class="{hide: modifyActivate}" data-bs-toggle="modal" data-bs-target="#articleCommentDeleteModal">삭제</span>
        </div>
      </div>
    </div>

    <div class="modal fade" id="articleCommentDeleteModal" tabindex="-1" aria-labelledby="articleCommentDeleteModal" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="aricleCommentDeleteModal">알림</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            정말로 삭제하시겠습니까?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
            <button type="button" class="btn main-color-background text-white" data-bs-dismiss="modal" @click="deleteComment">삭제</button>
          </div>
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
import { mapGetters, mapState } from 'vuex'

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
    ]),
    ...mapState([
      'decoded'
    ]),
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