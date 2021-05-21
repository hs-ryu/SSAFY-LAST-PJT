import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieList from '@/views/movies/MovieList'
import MovieDetail from '@/components/MovieDetail'
import ReviewDetail from '@/views/reviews/ReviewDetail'
import CreateReview from '@/views/reviews/CreateReview'
import UpdateReview from '@/views/reviews/UpdateReview'
import ArticleList from '@/views/community/ArticleList'
import ArticleDetail from '@/components/ArticleDetail'
import UpdateArticle from '@/views/community/UpdateArticle'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/:movieId/reviews/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/:movieId/reviews/create',
    name: 'CreateReview',
    component: CreateReview
  },
  {
    path: '/:movieId/reviews/:reviewId/update',
    name: 'UpdateReview',
    component: UpdateReview
  },
  {
    path: '/community',
    name: 'ArticleList',
    component: ArticleList
  },
  {
    path: '/community/:articleId',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  {
    path: '/community/:articleId/update',
    name: 'UpdateArticle',
    component: UpdateArticle
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
