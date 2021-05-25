<template>
  <swiper-slide><img style="height: 250px;" :src="'http://image.tmdb.org/t/p/w200/' + platformMovie.poster_path" alt=""></swiper-slide>
</template>

<script>
import { SwiperSlide } from 'vue-awesome-swiper'
export default {
  name: 'PlatformMovieItem2',
  props: {
    platformMovie: {
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