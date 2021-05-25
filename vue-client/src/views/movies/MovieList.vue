<template>
  <div>
    <h1>메인페이지</h1>
    <div class="d-flex justify-content-center">
      <input @input="fetchMovies" class="form-control m-3 w-75" type="search" placeholder="Search" aria-label="Search">
    </div>
    <div v-if="inputValue">
      <div class="mx-auto" style="width: 1000px; height: 1000px;">
        <div v-if="searchMovies.length">
          <div class="card-group">
            <SearchMovieItem
              v-for="(searchMovie, idx) in searchMovies"
              :key="idx + '0'"
              :searchMovie="searchMovie"
            />
          </div>
        </div>
        <div v-else style="height: 100px;">
          <h5 class="my-4">검색 결과가 존재하지 않습니다.</h5>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="mx-auto" style="width: 1000px;">
        <h2>NOW SHOWING</h2>
        <!-- <p>{{ nowShowingMovies }}</p> -->
        <swiper class="swiper" :options="swiperOption">
          <NowShowingItem2
            v-for="(nowShowingMovie, idx) in nowShowingMovies"
            :key="idx + '8'"
            :nowShowingMovie="nowShowingMovie"
          />
          <!-- <div class="swiper-pagination" slot="pagination"></div> -->
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
        <br>
        <h2>실시간 인기 영화</h2>
        <swiper class="swiper" :options="swiperOption">
          <PopularMovieItem2
          v-for="(popularMovie, idx) in popularMovies"
          :key="idx + '9'"
          :popularMovie="popularMovie"
          />
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
        <br>
        <h2>{{ platformvalue }} 상영 영화</h2>
        <div>
          <p class="d-inline mx-3" @click="setPlatform('netflix')">netflix</p>
          <p class="d-inline mx-3" @click="setPlatform('watcha')">watcha</p>
          <p class="d-inline mx-3" @click="setPlatform('wavve')">wavve</p>
          <p class="d-inline mx-3" @click="setPlatform('naver')">naver</p>
        </div>
        <swiper class="swiper" :options="swiperOption">
          <PlatformMovieItem2
          v-for="(platformMovie, idx) in platformMovies"
          :key="idx + 'platform'"
          :platformMovie="platformMovie"
          />
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
      </div>


      <!-- 원래 nowshowing -->
      <div class="card-group">
        <NowShowingItem
          v-for="(nowShowingMovie, idx) in nowShowingMovies"
          :key="idx + '1'"
          :nowShowingMovie="nowShowingMovie"
        />
      </div>
      <h2>{{ today.getHours() }}시의 인기영화</h2>
      <!-- <p>{{ popularMovies }}</p> -->
      <div class="card-group">
        <PopularMovieItem
          v-for="(popularMovie, idx) in popularMovies"
          :key="idx + '2'"
          :popularMovie="popularMovie"
        />
      </div>
      <!-- 플랫폼상영 -->
      <h2>현재 {{ platformvalue }}에서 상영중인 영화입니다</h2>
      <div>
        <div>
          <p class="d-inline mx-3" @click="setPlatform('netflix')">netflix</p>
          <p class="d-inline mx-3" @click="setPlatform('watcha')">watcha</p>
          <p class="d-inline mx-3" @click="setPlatform('wavve')">wavve</p>
          <p class="d-inline mx-3" @click="setPlatform('naver')">naver</p>
        </div>
      </div>
      <div class="card-group">
        <PlatformMovieItem
          v-for="(platformMovie, idx) in platformMovies"
          :key="idx + '3'"
          :platformMovie="platformMovie"
        />
      </div>
      


      <h2>전체영화목록</h2>
      <div class="card-group">
        <MovieItem
          v-for="(movie, idx) in allMovies"
          :key="idx + '3'"
          :movie="movie"
        />
      </div>
    </div>
      
  </div>
</template>
<script>
import MovieItem from '@/components/MovieItem'
import PopularMovieItem from '@/components/PopularMovieItem'
import PopularMovieItem2 from '@/components/PopularMovieItem2'
import NowShowingItem from '@/components/NowShowingItem'
import NowShowingItem2 from '@/components/NowShowingItem2'
import SearchMovieItem from '@/components/SearchMovieItem'
import PlatformMovieItem from '@/components/PlatformMovieItem'
import PlatformMovieItem2 from '@/components/PlatformMovieItem2'
import { mapActions, mapState, mapGetters } from 'vuex'
// SwiperSlide 
import { Swiper } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'


export default {
  name: 'MovieList',
  components: {
    MovieItem,
    PopularMovieItem,
    PopularMovieItem2,
    NowShowingItem,
    NowShowingItem2,
    SearchMovieItem,
    PlatformMovieItem,
    PlatformMovieItem2,
    Swiper,
    // SwiperSlide,
  },
  data: function () {
    return {
      swiperOption: {
        slidesPerView: 6,
        spaceBetween: 0,
        slidesPerGroup: 4,
        loopedSlides: 6,
        // autoplay: {
        //   delay: 6000,
        //   waitForTransition: true,
        // },
        loop: true,
        loopFillGroupWithBlank: false,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        }
      },
    }
  },
  methods: {
    ...mapActions([
      'getAllMovies',
      'getPopularMovies',
      'getNowShowing',
      'fetchMovies',
      'getPlatformMovies',
      'setPlatform',
      'resetInputValue',
    ]),
  },
  computed: {
    ...mapState([
      'allMovies',
      'popularMovies',
      'nowShowingMovies',
      'searchMovies',
      'inputValue',
      'platformMovies',
      'platformvalue',
      'today',
    ]),
    ...mapGetters([
      'movieLength',
      'inputLength',
    ])
  },
  created: function () {
    this.getNowShowing()
    this.getAllMovies()
    this.getPopularMovies()
    this.getPlatformMovies(this.platformvalue)
    this.resetInputValue()
    console.log(this.inputValue)
  },
}
</script>

<style lang="scss" scoped>
  // @import './base.scss';
</style>