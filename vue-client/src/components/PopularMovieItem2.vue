<template>
  <swiper-slide><img style="height: 250px;" :src="'http://image.tmdb.org/t/p/w200/' + popularMovie.poster_path" alt=""></swiper-slide>
</template>

<script>
import { SwiperSlide } from 'vue-awesome-swiper'
export default {
  name: 'PopularMovieItem2',
  props: {
    popularMovie: {
      type: Object,
    },
  },
  components: {
    SwiperSlide,
  }
}
</script>

<style>

</style>