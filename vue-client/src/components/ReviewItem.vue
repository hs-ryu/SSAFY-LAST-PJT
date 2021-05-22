<template>
  <div>
    <h1>개별리뷰제목</h1>
    <h2 @click="goToReviewDetail">{{ review.title }}</h2>
  </div>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: {
      type: Object,
    },
    movieId: {
      type: String,
    },
    movieTitle: {
      type: String,
    }
  },
  methods: {
    goToReviewDetail: function () {
      const reviewId = this.review.id
      this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: reviewId }, query: { movieTitle: this.movieTitle}})
    }
  }

}
</script>

<style>

</style>