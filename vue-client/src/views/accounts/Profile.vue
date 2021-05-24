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
    <div class="card-group mb-5">
      <div v-for="(movie, idx) in userProfile.like_movies" :key="idx + 'movie'">
        <div class="mb-1">
          <div class="card text-center mt-1 border-light" style="width: 150px;  height: 200px;">
            <div class="card-body p-0">
              <img :src="'http://image.tmdb.org/t/p/w200/' + movie.poster_path" style="object-fit: cover;" class="card-img-top img-fluid rounded mx-auto d-block" :alt="movie.title">
              <p class="card-title m-0">{{ movie.title }}</p>
              <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="my-2 d-flex justify-content-between">
      <div>
        <h2 class="fw-bold" style="text-align: left;">작성한 리뷰</h2>
        <div class="m-2" v-if="userProfile.create_reviews.length">
          <table style="width: 450px; height: 275px;" class="table">
            <thead>
              <tr>
                <th scope="col">영화</th>
                <th scope="col">제목</th>
                <th scope="col">평점</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(review, idx) in displayReviews" :key="idx +'1'">
                <td>{{ review.movie }}</td>
                <td @click="goToReviewDetail(review.id)">{{ review.title }}</td>
                <td>{{ review.rank }} ⭐</td>
              </tr>
            </tbody>
          </table>
          <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
              <li class="page-item">
                <button type="button" class="text-dark page-link" v-if="reviewsPage != 1" @click="reviewsPage--"> Previous </button>
              </li>
              <li class="text-dark page-item" v-for="(pageNumber,idx) in reviewsPages.slice(reviewsPage-1, reviewsPage+5)" :key=idx>
                <button type="button" class="text-dark page-link"  @click="page=pageNumber">{{ pageNumber }}</button>
              </li>
              <li class="page-item">
                <button type="button" @click="reviewsPage++" v-if="reviewsPage < reviewsPages.length" class="text-dark page-link"> Next </button>
              </li>
            </ul>
          </nav>
        </div>
        <div v-else>
          <p>작성한 리뷰가 없습니다.</p>
        </div>
      </div>
      <div>
        <h2 class="fw-bold" style="text-align: left;">작성한 게시글</h2>
        <div class="m-2" v-if="userProfile.create_articles.length">
          <table style="width: 450px; height: 275px;" class="table">
            <thead>
              <tr>
                <th scope="col">카테고리</th>
                <th scope="col">제목</th>
                <th scope="col">날짜</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(article, idx) in displayArticles" :key="idx +'2'">
                <td v-if="article.categories=2">
                  자유글
                </td>
                <td v-else>
                  건의사항
                </td>
                <td>{{ article.title }}</td>
                <td>{{ article.created_at }}</td>
              </tr>
            </tbody>
          </table>
          <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
              <li class="page-item">
                <button type="button" class="text-dark page-link" v-if="articlesPage != 1" @click="articlesPage--"> Previous </button>
              </li>
              <li class="page-item" v-for="(pageNumber,idx) in articlesPages.slice(articlesPage-1, articlesPage+5)" :key=idx>
                <button type="button" class="text-dark page-link"  @click="articlesPage=pageNumber">{{ pageNumber }}</button>
              </li>
              <li class="page-item">
                <button type="button" @click="articlesPage++" v-if="articlesPage < articlesPages.length" class="text-dark page-link"> Next </button>
              </li>
            </ul>
          </nav>
        </div>
      </div>
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
      reviewsPage: 1,
      articlesPage: 1,
			reviewsPerPage: 6,
			articlesPerPage: 6,
			reviewsPages: [],	
			articlesPages: [],	
    }
  },
  computed: {
    ...mapState({
      'loginedUserId': 'userId',
    }),
    ...mapGetters([
      'config',
    ]),
    displayReviews () {
      return this.reviewPaginate(this.userProfile.create_reviews)
    },
    displayArticles () {
      return this.articlePaginate(this.userProfile.create_articles)
    },
    Reviews () {
      return this.userProfile.create_reviews
    },
    Articles () {
      return this.userProfile.create_articles
    }
  },
  watch: {
    Reviews () {
      this.setReviewPages()
    },
    Articles () {
      this.setArticlePages()
    }
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
    setReviewPages: function () {
      let numberOfPages = Math.ceil(this.userProfile.create_reviews.length / this.reviewsPerPage)
      for (let index=1; index <= numberOfPages; index++)
      {
        this.reviewsPages.push(index)
      }
    },
    setArticlePages: function () {
      let numberOfPages = Math.ceil(this.userProfile.create_articles.length / this.articlesPerPage)
      for (let index=1; index <= numberOfPages; index++)
      {
        this.articlesPages.push(index)
      }
    },
    reviewPaginate: function (reviews) {
      let reviewsPage = this.reviewsPage
      let reviewsPerPage = this.reviewsPerPage
      let from = (reviewsPage * reviewsPerPage) - reviewsPerPage;
      let to = (reviewsPage * reviewsPerPage)
      return reviews.slice(from, to)
    },
    articlePaginate: function (articles) {
      let articlesPage = this.articlesPage
      let articlesPerPage = this.articlesPerPage
      let from = (articlesPage * articlesPerPage) - articlesPerPage;
      let to = (articlesPage * articlesPerPage)
      return articles.slice(from, to)
    }
  },
  created: function () {
    this.getUserProfile()
  }
}
</script>

<style>

</style>