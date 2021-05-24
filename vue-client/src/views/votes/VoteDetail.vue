<template>
  <div>

  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

export default {
  name: 'VoteDetail',

  data: function () {
    return {
      comment: {},
      voteTitle: this.$route.query.voteTitle,
      movieId: this.$route.params.movieId,
      voteId: this.$route.params.voteId,
      comments: [],
      commentContent: '',
    }
  },
  methods: {
    getVoteDetail: function () {
      const headers = this.config
      // path('<int:movie_pk>/createvote/', views.createvote, name='createvote'),
      // path('<int:movie_pk>/votes/<int:vote_pk>/', views.getvote, name='getvote'),
      
      axios({
        url: SERVER.URL + SERVER.ROUTES.votes + `${this.movieId}/votes/${this.voteId}/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.votes = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },



    deleteVote: function () {
      // path('<int:movie_pk>/<int:vote_pk>/deletevote/', views.deletevote, name='deletevote'),
      const headers = this.config
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

    // path('<int:movie_pk>/votes/<int:vote_pk>/createvotecomment/', views.createvotecomment, name='createvotecomment'),
    // path('<int:movie_pk>/votes/<int:vote_pk>/votecomments/', views.getvotecomments, name='getallvotecomments'),
    // path('<int:movie_pk>/votes/<int:vote_pk>/<int:votecomment_pk>/deletevotecomment/', views.deletevotecomment, name='deletevotecomment'),
    getVoteComments: function() {
      const headers = this.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.votes + `${this.movieId}/votes/${this.voteId}/votecomments/`,
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
    createComment: function () {
      const headers = this.config
      const commentItem = {
        content: this.commentContent
      }
      if (commentItem.content) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.votes + `${this.movieId}/votes/${this.voteId}/createvotecomment/`,
          method: 'post',
          data: commentItem,
          headers,
        })
        .then(() => {
          this.commentContent = ''
          this.getVoteComments()
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
  },
  created: function() {
    this.getVoteDetail()
    this.getVoteComments()
  }
}
</script>

<style>

</style>