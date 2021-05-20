<template>
  <div>
    <h3>{{ nowShowingMovie.title }}</h3>
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