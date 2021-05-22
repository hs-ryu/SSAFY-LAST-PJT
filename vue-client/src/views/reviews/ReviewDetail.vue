<template>
  <div>
    <div>
      <h1>개별리뷰상세</h1>
      <h3>리뷰 제목: {{ review.title }}</h3>
      <p>영화: {{ movieTitle }}</p>
      <p>평점: {{ review.rank }}</p>
      <p>리뷰 내용: {{ review.content }}</p>
      <button @click="goToUpdate">수정</button>
      <button @click="deleteReview">삭제</button>
    </div>
    <div>
      <h2>댓글 목록</h2>
      <label for="comment">댓글작성</label>
      <input v-model="commentContent" type="text" name="comment" id="comment">
      <input @click="createComment" type="submit" value="작성">
      <!-- {{ comments }} -->
      <ReviewComment
        v-for="(comment, idx) in comments"
        :key="idx"
        :comment="comment"
        :movieId="movieId"
        :reviewId="reviewId"
        @comment-deleted="getReviewComments"
        @modify-activate="getReviewComments"
      />
    </div>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import ReviewComment from '@/components/ReviewComment'
import { mapGetters } from 'vuex'

export default {
  name: 'ReviewDetail',
  components: {
    ReviewComment,
  },
  computed: {
    ...mapGetters([
      'config'
    ])
  },
  data: function () {
    return {
      review: {},
      movieTitle: this.$route.query.movieTitle,
      movieId: this.$route.params.movieId,
      reviewId: this.$route.params.reviewId,
      comments: [],
      commentContent: '',
    }
  },
  methods: {
    getReviewDetail: function () {
      const headers = this.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.review = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getReviewComments: function () {
      const headers = this.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/getcomments/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteReview: function () {
      const headers = this.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/deletereview/`,
        method: 'delete',
        headers,
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
    },
    createComment: function () {
      const headers = this.config
      const commentItem = {
        content: this.commentContent,
      }
      if (commentItem.content) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/createcomment/`,
          method: 'post',
          data: commentItem,
          headers,
        })
        .then(() => {
          this.commentContent = ''
          this.getReviewComments()
          // this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
        })
        .catch((err) => {
          console.log(err)
        })
      }
    }
  },
  created: function () {
    this.getReviewDetail()
    this.getReviewComments() // 댓글목록 가져오는 함수
  }
}
</script>

<style>

</style>