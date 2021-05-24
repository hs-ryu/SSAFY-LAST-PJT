<template>
  <div>
    <h1>개별투표정보</h1>
    <tr>
      <td @click="goToVoteDetail">{{ vote.title }}</td>
      <td>{{ vote.username }}</td>
    </tr>
  </div>
</template>

<script>
export default {
  name: 'VoteItem',
  props: {
    vote: {
      type: Object,
    },
    movieId: {
      type: String,
    },
    voteTitle: {
      type: String,
    }
  },
  methods: {
    goToVoteDetail: function () {
      const voteId = this.vote.id
      this.$router.push({ name: 'VoteDetail', params: { movieId: this.movieId, voteId: voteId }, query: { voteTitle: this.voteTitle}})
    }
  }
}
</script>

<style>

</style>


<script>
export default {

  

}
</script>

<style>

</style>