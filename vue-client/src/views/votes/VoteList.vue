<template>
  <div>
    <h1>투표목록</h1>
    <VoteItem
      v-for="(vote, idx) in votes"
      :key="idx"
      :vote="vote"
    />
    <button @click="goToCreateVote"> 투표 만들기! </button>
  </div>
</template>

<script>
import VoteDetail from '@/components/VoteDetail'

export default {
  name: 'VoteList',
  components: {
    VoteDetail
  },
  data: {
    function() {
      return {
        votes = [],
      }
    }
  },
  methods: {
    getVotes: function () {
      // path('<int:movie_pk>/votes/', views.getallvotes, name='getallvotes'),
      axios({
        url: SERVER.URL + '/movies/' + `${this.movieId}/votes/`,
        method: 'get',
      })
      .then((res) => {
        this.votes = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToCreateVote: function () {
      this.$router.push({ name: 'CreateVote'})
    },
  },
  created: function () {
    this.getVotes()
  }
}
</script>

<style>

</style>