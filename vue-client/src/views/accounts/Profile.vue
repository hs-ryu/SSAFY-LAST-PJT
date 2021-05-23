<template>
  <div>
    {{ loginedUserId }}
    <h1>{{userProfile.username}}님의 프로필</h1>
    {{userProfile}}
    <p>팔로워 {{ userProfile.followers.length }} | 팔로잉 {{ userProfile.followings.length }}</p>
    <div v-if="userProfile.user_id!==loginedUserId">
      <button v-if="userProfile.followers.includes(loginedUserId)" @click="updateFollowStatus">unfollow</button>
      <button v-else @click="updateFollowStatus">follow</button>
    </div>
    
    <h2>좋아요 한 영화 목록</h2>
    <div v-for="(movie, idx) in userProfile.like_movies" :key="idx + 'movie'">
      <p>{{ movie.title }}</p>
    </div>
    <h2>작성한 리뷰 목록</h2>
    <div v-for="(review, idx) in userProfile.create_reviews" :key="idx + '1'">
      <p>{{ review.movie }}</p>
      <p>{{ review.title }}</p>
    </div>
    <h2>작성한 게시글 목록</h2>
    <div v-for="(article, idx) in userProfile.create_articles" :key="idx + '2'">
      <p>{{ article.title }}</p>
    </div>

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