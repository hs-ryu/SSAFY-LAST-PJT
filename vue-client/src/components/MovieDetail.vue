<template>
  <div style="text-align: center">
    <!-- {{ movie }} -->
    <h1 class="m-4">{{ movie.title }}</h1>
    <div class="d-flex justify-content-center align-items-center">
      <div class="img-container">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title">
      </div>
      <div class="mx-4" style="width: 500px; text-align: left;">
        <div class="video-container" v-if="movie.trailer">
          <iframe width="560" height="315" class="m-2" :src="'https://www.youtube.com/embed/' + movie.trailer" frameborder="0" allowfullscreen></iframe>
        </div>
        <br>
        <p style="font-size: 14px;">{{ movie.overview }}</p>
        <p>개봉일: {{ movie.release_date }}</p>
        <p>평점: {{ movie.rank_average.toFixed(1) }}⭐</p>

        <div class="d-inline" v-if="isLoggedIn">
          <button class="btn d-inline" v-if="movie.like_users && movie.like_users.includes(decoded.user_id)" @click="getLikeStatus"><i class="fas fa-heart fa-lg" style="color:crimson;"></i></button>
          <button class="btn d-inline" v-else @click="getLikeStatus"><i class="far fa-heart fa-lg" style="color:crimson;"></i></button>
        </div>
        <div class="d-inline" v-else>
          <i class="d-inline fas fa-heart fa-lg" style="color:crimson;"></i>
        </div>
        <p class="d-inline">{{ movie.like_users.length }}명이 이 영화를 좋아합니다.</p>
        <div class="d-flex">
          <div v-if="netflix" class="m-1" style="max-width: 35px;">
            <a v-if="netflix" :href="netflix"><img img style="width: 100%" src="@/assets/netflix_logo.png" alt="netflix logo"></a>
          </div>
          <div v-if="watcha" class="m-1" style="max-width: 35px;">
            <a v-if="watcha" :href="watcha"><img img style="width: 100%" src="@/assets/watcha_logo.png" alt="watcha logo"></a>
          </div>
          <div v-if="wavve" class="m-1" style="max-width: 35px;">
            <a v-if="wavve" :href="wavve"><img img style="width: 100%" src="@/assets/wavve_logo.png" alt="wavve logo"></a>
          </div>
          <div v-if="naver" class="m-1" style="max-width: 35px;">
            <a v-if="naver" :href="naver"><img style="width: 100%" src="@/assets/naver_logo.png" alt="naver logo"></a>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <div style="width: 1000px;" class="mx-auto">
      <div class="m-2" v-if="reviews.length">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">글 제목</th>
              <th scope="col">평점</th>
              <th scope="col">작성자</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(review, idx) in reviews" :key="idx +'1'">
              <td @click="goToReviewDetail(review.id)">{{ review.title }}</td>
              <td>{{ review.rank }}</td>
              <td>{{ review.username }}</td>
              <!-- <ReviewItem
                v-for="(review, idx) in reviews"
                :key="idx"
                :review="review"
                :movieId="movieId"
                :movieTitle="movie.title"
              /> -->
            </tr>
          </tbody>
        </table>
      </div>
      <div class="m-5" v-else>
        <p>리뷰가 아직 없어요. 첫번째 글을 쓸 수 있는 절호의 찬스! 🤘</p>
      </div>
      <div class="d-flex justify-content-center">
        <button class="mx-2 btn main-color-background text-white" @click="goToCreateReview">리뷰 작성하기</button>
        <button style="border-color: #CE93D8" class="btn main-color-content" @click="$router.push({ name: 'MovieList' })">목록</button>
      </div>
    </div>

    <hr>
    <div style="width: 1000px;" class="mx-auto">
      <div class="m-2" v-if="votes.length">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">제목</th>
              <th scope="col">당신의 선택은?</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(vote, idx) in votes" :key="idx +'2'">
              <td @click="goToVoteDetail(vote.id)">{{ vote.title }}</td>
              <td>{{ vote.option_one }}   VS   {{ vote.option_two }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="m-5" v-else>
        <p>투표가 아직 없어요. 첫번째 투표를 등록해 보세요! 🤘</p>
      </div>
      <div class="d-flex justify-content-center">
        <button class="mx-2 btn main-color-background text-white" @click="goToCreateVote">투표 만들기</button>
      </div>
    </div>

    
  


  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters, mapState } from 'vuex'

// import ReviewItem from '@/components/ReviewItem'

export default {
  name: 'MovieDetail',
  components: {
    // ReviewItem
  },
  data: function () {
    return {
      movie: {},
      movieId: this.$route.params.movieId,
      netflix: '',
      watcha: '',
      wavve: '',
      naver: '',
      reviews: [],
      votes: [],
    }
  },
  computed: {
    ...mapGetters([
      'config',
      'isLoggedIn',
    ]),
    ...mapState([
      'userId',
      'decoded',
    ])
  },
  methods: {
    getMovieDetail: function() {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getAllMovies + `${this.movieId}/`,
        method: 'get',
      })
      .then((res) => {
        this.movie = res.data
        this.netflix = res.data.netflix
        this.watcha = res.data.watcha
        this.wavve = res.data.wavve
        this.naver = res.data.naver
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getReviews: function() {
      axios({
        url: SERVER.URL + SERVER.ROUTES.reviews + `${this.movieId}/reviews/`,
        method: 'get',
      })
      .then((res) => {
        this.reviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },

    goToCreateReview: function () {
      const movieTitle = this.movie.title
      const moviePosterPath = this.movie.poster_path
      // console.log(moviePosterPath)
      this.$router.push({ name: 'CreateReview', params: { movieId: this.movieId }, query: { movieTitle: movieTitle, moviePosterPath: moviePosterPath }})
    },

    getLikeStatus: function () {
      const headers = this.config
      axios({
        // 'getmovies/<int:movie_pk>/likes/
        url: SERVER.URL + `/movies/getmovies/${this.movieId}/likes/`,
        method: 'post',
        headers,
      })
      .then(() => {
        this.getMovieDetail()
      })
    },
    goToReviewDetail: function (reviewId) {
      const movieTitle = this.movie.title
      const moviePosterPath = this.movie.poster_path
      // console.log(moviePosterPath)
      this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: reviewId }, query: { movieTitle: movieTitle, moviePosterPath: moviePosterPath }})
      console.log(movieTitle)
    },

    // 굳!!!!
    getVotes: function () {
      // path('<int:movie_pk>/votes/', views.getallvotes, name='getallvotes'),
      axios({
        url: SERVER.URL + '/movies/' + `${this.movieId}/votes/`,
        method: 'get',
      })
      .then((res) => {
        this.votes = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToVoteDetail: function (voteId) {
      const movieId = this.movieId
      this.$router.push({ name: 'VoteDetail', params: { movieId: movieId, voteId: voteId }})
      // console.log(movieId)
    },
    goToCreateVote: function () {
      this.$router.push({ name: 'CreateVote', params: { movieId: this.movieId }})
    },
  },
  created: function () {
    this.getMovieDetail()
    this.getReviews()
    this.getVotes()
  }

}
</script>

<style>
.img-container {
  max-width: 380px;
}
img {
  width: 100%;
}
.video-container {
  position: relative;
  height: 0;
  padding-bottom: 56.25%;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

</style>