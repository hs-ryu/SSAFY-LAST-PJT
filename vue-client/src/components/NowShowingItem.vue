<template>
  <div>
    <img :src="nowShowingMovie.image_path" :alt="nowShowingMovie.movieNm">
    <h3>{{ nowShowingMovie.movieNm }}</h3>
  </div>
</template>

<script>

export default {
  name: 'NowShowingItem',
  data: function () {
    return {

    }
  },
  props: {
    nowShowingMovie: {
      type: Object,
    }
  },
}
</script>

<style>

</style>