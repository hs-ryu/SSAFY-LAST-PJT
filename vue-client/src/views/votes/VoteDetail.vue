<template>
  <div>
    <p>{{vote}}</p>
    <h2>{{vote.title}}</h2>
    <div class="progress" style="height: 30px;">
      <div class="progress-bar bg-primary" role="progressbar" style="width: 50%" aria-valuenow="" aria-valuemin="0" aria-valuemax="100">{{ vote.option_one_count }}%</div>
      <div class="progress-bar bg-dark" role="progressbar" style="width: 50%" aria-valuenow="" aria-valuemin="0" aria-valuemax="100">{{ vote.option_two_count }}%</div>
    </div>
    <input class="btn main-color-background text-white" @click="deleteVote" type="submit" value="삭제">
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import {mapGetters} from 'vuex'

export default {
  name: 'VoteDetail',
  computed: {
    ...mapGetters([
      'config'
    ]),
  },
  data: function () {
    return {
      vote: {},
      // movieTitle: this.$route.query.movieTitle,
      movieId: this.$route.params.movieId,
      voteId: this.$route.params.voteId,
      comments: [],
      // comments: [],
      // commentContent: '',
      // likeCount: 0,
      // likeStatus: false,
      // likeStatus: this.review.like_users.includes('userId'),
    }
  },
  methods: {
    getVoteDetail: function () {
      const headers = this.config
      // path('<int:movie_pk>/votes/<int:vote_pk>/', views.getvote, name='getvote'),
      axios({
        url: SERVER.URL + '/movies/' + `${this.movieId}/votes/` + `${this.voteId}/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.vote = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
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

    deleteVote: function() {
      const headers = this.config
      // path('<int:movie_pk>/<int:vote_pk>/deletevote/', views.deletevote, name='deletevote'),
      axios({
        url: SERVER.URL + SERVER.ROUTES.votes + `${this.movieId}/${this.voteId}/deletevote/`,
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
    // //여기서부터 다시
    // createComment: function () {
    //   const headers = this.config
    //   const commentItem = {
    //     content: this.commentContent,
    //     choice =
    //   }
    //   if (commentItem.content) {
    //     axios({
    //       url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/${this.reviewId}/createcomment/`,
    //       method: 'post',
    //       data: commentItem,
    //       headers,
    //     })
    //     .then(() => {
    //       this.commentContent = ''
    //       this.getReviewComments()
    //       // this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    //   }
    // },



  },




  created: function () {
    this.getVoteDetail()
    this.getVoteComments()
  }

}
</script>

<style>

</style>