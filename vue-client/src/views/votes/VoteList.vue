<template>
  <div>
    <h1>투표목록</h1>
    <VoteDetail 
    
    />
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
    getAllVotes: function () {
      // path('<int:movie_pk>/votes/', views.getallvotes, name='getallvotes'),
      axios({
        url: SERVER.URL + '/movies/' + movieId + '/votes/',
        method: 'get',
      })
      .then((res) => {
        this.votes = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToVoteItem: function (voteId) {
      this.$router.push({ name: 'VoteItem', params: { voteId}})
    },
    goToCreateVote: function () {
      this.$router.push({ name: 'CreateVote'})
    },
  },
  created: function () {
    this.getAllVotes()
  }
}
</script>

<style>

</style>