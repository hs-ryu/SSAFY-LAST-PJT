<template>
  <div class="my-1">
    <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex justify-content-center align-items-center">
        <button v-if="comment.choice" class="btn btn-danger me-4" type="button" disabled>반대</button>
        <button v-else class="btn btn-primary me-4" type="button" disabled>찬성</button>
        <div class="justify-content-center me-3">
          <p align="center" class="fw-bold m-0 ">{{ comment.username }}</p>
        </div>
        <div>
          <p align="center" class="m-0">{{ comment.content }}</p>
        </div>
      </div>
      <div class="d-flex">
        <button class="mx-1 btn btn-sm main-color-background text-white" @click="deleteComment">삭제</button>
      </div>
    </div>

  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: "VoteComment",
  props: {
    comment: {
      type: Object,
    },
    movieId: {
      type: String,
    },
    voteId: {
      type: String,
    },
  },
  data: function () {
    return {
    }
  },
  computed: {
    ...mapGetters([
      'config'
    ]),
  },
  methods: {
    getVoteComments: function () {
      const headers = this.config
      // path('<int:movie_pk>/votes/<int:vote_pk>/votecomments/', views.getvotecomments, name='getallvotecomments'),
      axios({
        url: SERVER.URL + '/movies/' + `${this.movieId}/votes/` + `${this.voteId}/` + 'votecomments/',
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
    deleteComment: function () {
      const headers = this.config
      const commentId = this.comment.id
      // path('<int:movie_pk>/votes/<int:vote_pk>/<int:votecomment_pk>/deletevotecomment/', views.deletevotecomment, name='deletevotecomment'),
      axios({
        url: SERVER.URL + '/movies/' + `${this.movieId}/votes/` + `${this.voteId}/` + `${commentId}/` + 'deletevotecomment/',
        method: 'delete',
        headers,
      })
      .then(() => {
        // this.getReviewComments()
        this.$router.push({ name: 'VoteDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
      })
    },
  }
}
</script>

<style>

</style>