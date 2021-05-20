<template>
  <div>
    <h3>{{ popularMovie.title }}</h3>
    <p>{{ popularMovie.content }}</p>
  </div>
</template>

<script>
export default {
  name: 'PopularMovieItem',
  props: {
    popularMovie: {
      type: Object,
    }
  }

}
</script>

<style>

</style>