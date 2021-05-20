<template>
  <div>
    <h3>{{ nowShowingMovie.movieNm }}</h3>
    <p>개봉일: {{ nowShowingMovie.openDt }}</p>
    <p>누적관객: {{ nowShowingMovie.audiAcc }}</p>
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