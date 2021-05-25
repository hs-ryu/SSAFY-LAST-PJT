<template>
  <div>
    <!-- <p>{{vote}}</p> -->
    <h2>{{vote.title}}</h2>
    <br>
    <p> 총 {{vote.option_one_count + vote.option_two_count}}명 참여했습니다</p>
    <div class="d-flex justify-content-center">
      <div class="progress" style="height: 30px; width: 700px">
        <div class="progress-bar bg-primary" role="progressbar" :style="{width: scoreone + '%'}" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">{{ vote.option_one }}  :  {{scoreone}}% ({{vote.option_one_count}} 명)</div>
        <div class="progress-bar bg-danger" role="progressbar" :style="{width: scoretwo + '%'}" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">{{ vote.option_two }}  :  {{ scoretwo }}% ({{vote.option_two_count}} 명)</div>
      </div>
    </div>
    <br>
    <input class="btn main-color-background text-white" @click="deleteVote" type="submit" value="삭제">
    <div style="width: 850px;" class="mx-auto">
      <hr>

      <div v-if="comments.length">
        <h3 style="text-align: left" class="my-3">{{ comments.length }}개의 댓글</h3>
        <VoteComment
          v-for="(comment,idx) in comments"
          :key="idx"
          :comment="comment"
          :movieId="movieId"
          :voteId="voteId"
        />
      </div>

      <div v-else>
        <p>당신의 의견을 기다리고 있어요 🤘</p>
      </div>
      <div class="my-5">
        <input class="mx-1 btn btn-sm main-color-background text-white" @click="createCommentOne" type="submit" value="왼쪽!">
        <input style="width: 500px" v-model="commentContent" type="text" name="comment" id="comment" placeholder="당신의 생각은?">
        <input class="mx-1 btn btn-sm main-color-background text-white" @click="createCommentTwo" type="submit" value="오른쪽!">
      </div>
    </div>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters} from 'vuex'
import VoteComment from '@/components/VoteComment'

export default {
  name: 'VoteDetail',
  components: {
    VoteComment,
  },
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
      commentContent: '',
      scoreone: 0,
      scoretwo: 0,

      // comments: [],
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
        this.scoreone = (this.vote.option_one_count/(this.vote.option_one_count + this.vote.option_two_count) * 100).toFixed(1)
        this.scoretwo = (this.vote.option_two_count/(this.vote.option_one_count + this.vote.option_two_count) * 100).toFixed(1)
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
    createCommentOne: function () {
      const headers = this.config
      const commentItem = {
        content: this.commentContent,
        choice : 0
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
          this.getVoteDetail()
          // this.$router.push({ name: 'VoteDetail', params: { movieId: this.movieId, voteId: this.voteId }})
        })
        .catch(() => {
        })
      }
    },
    createCommentTwo: function () {
      const headers = this.config
      const commentItem = {
        content: this.commentContent,
        choice : 1
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
          this.getVoteDetail()
          // this.$router.push({ name: 'VoteDetail', params: { movieId: this.movieId, voteId: this.voteId }})
        })
        .catch(() => {
        })
      }
    },
  },
  created: function () {
    this.getVoteDetail()
    this.getVoteComments()
  }

}
</script>

<style>

</style>