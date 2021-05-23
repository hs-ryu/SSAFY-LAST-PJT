<template>
  <div>
    <!-- 기존 코드 -->
    <!-- <img :src="nowShowingMovie.image_path" :alt="nowShowingMovie.movieNm">
    <h3>{{ nowShowingMovie.movieNm }}</h3> -->
    <div class="mb-1">
      <div class="card text-center mt-1 border-light">
        <div class="card-body p-0" >
          <!-- <p>{{ nowShowingMovie.movieNm }}</p> -->
          <img :src="nowShowingMovie.image_path" style="width: 100px;  height: 150px; object-fit: cover;  z-index: 0;" class="card-img-top rounded mx-auto d-block" alt="" @mouseover="zoomIn" @mouseleave="zoomOut">
          <p class="card-img-overlay" >{{ nowShowingMovie.movieNm }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NowShowingItem',
  props: {
    nowShowingMovie: {
      type: Object,
    }
  },
  methods: {
    zoomIn: function(event) {
      console.log(event)
      event.target.style.transform = "scale(2)";
      event.target.style.zIndex = '1';
      event.target.style.transition = "all 0.5s";
      event.target.style.webkitFilter = "blur(3px) brightness(50%)";
      
    },
    zoomOut: function(event) {
      console.log(event)
      event.target.style.transform = "scale(1)";
      event.target.style.zIndex = '-1';
      event.target.style.transition = "all 0.5s";
      event.target.style.webkitFilter = "blur(0px) brightness(100%)";
    }
  }
}
</script>

<style>

</style>