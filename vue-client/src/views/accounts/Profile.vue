<template>
  <div style="width: 1000px" class="mx-auto">
    <div class="mb-3 d-flex justify-content-between">
      <div>
        <h1 class="fw-bold" style="text-align: left">{{userProfile.username}}님의 프로필</h1>
      </div>
      <div class="d-flex">
        <h5>팔로워 {{ userProfile.followers.length }} | 팔로잉 {{ userProfile.followings.length }}</h5>
        <div class="ms-3" v-if="userProfile.user_id!==loginedUserId">
          <button class="mx-2 btn main-color-background text-white" v-if="userProfile.followers.includes(loginedUserId)" @click="updateFollowStatus">unfollow</button>
          <button class="mx-2 btn main-color-background text-white" v-else @click="updateFollowStatus">follow</button>
        </div>
      </div>
    </div>
    
    <h2 class="fw-bold" style="text-align: left;">좋아요 한 영화</h2>
    <div v-for="(movie, idx) in userProfile.like_movies" :key="idx + 'movie'"
      class="card-group row row-cols-6 row-cols-md-2 g-4">
        <div class="col">
          <div class="card text-center mt-1 border-light">
            <div class="card-body p-0">
              <img :src="'http://image.tmdb.org/t/p/w200/' + movie.poster_path" style="width: 200px; height: 300px; object-fit: cover;" class="card-img-top rounded mx-auto d-block" :alt="movie.title">
              <p class="card-title m-0">{{ movie.title }}</p>
              <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
            </div>
          </div>
        </div>
    </div>
    <h2 class="fw-bold" style="text-align: left;">작성한 리뷰 목록</h2>
    <div v-for="(review, idx) in userProfile.create_reviews" :key="idx + '1'">
      <p>{{ review.movie }}</p>
      <p>{{ review.title }}</p>
    </div>
    <h2>작성한 게시글 목록</h2>
    <div v-for="(article, idx) in userProfile.create_articles" :key="idx + '2'">
      <p>{{ article.title }}</p>
    </div>
    {{userProfile}}
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapState, mapGetters } from 'vuex'

export default {
  name: 'Profile',
  data: function () {
    return {
      userName: this.$route.params.username,
      userProfile: {},
    }
  },
  computed: {
    ...mapState({
      'loginedUserId': 'userId',
    }),
    ...mapGetters([
      'config',
    ])
  },
  methods: {
    getUserProfile: function () {
      axios({
        // path('<int:user_id>/', views.profile, name='profile'),
        url: SERVER.URL + `/accounts/${this.userName}/`,
        method: 'get',
      })
      .then((res) => {
        this.userProfile = res.data
      })
    },
    updateFollowStatus: function () {
      const headers = this.config
      axios({
        // path('<int:user_pk>/follow/', views.follow, name='follow'),
        url: SERVER.URL + `/accounts/${this.userProfile.user_id}/follow/`,
        method: 'post',
        headers,
      })
      .then(() => {
        // const { likeCount } = res.data
        // this.likeCount = likeCount
        // this.likeStatus = liked
        this.getUserProfile()
      })
    },
  },
  created: function () {
    this.getUserProfile()
  }
}
</script>

<style>

</style>