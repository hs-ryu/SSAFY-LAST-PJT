<template>
  <div>
    <h3 @click="goToDetail">{{ movie.title }}</h3>
    <p>{{ movie.content }}</p>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie: {
      type: Object
    },
  },
  methods: {
    goToDetail: function () {
      const movieId = this.movie.id
      this.$router.push({ name: 'MovieDetail', params: { movieId: movieId}})
    }
  }

}
</script>

<style>

</style>