import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieList from '@/views/movies/MovieList'
import MovieDetail from '@/components/MovieDetail'
import ReviewDetail from '@/views/reviews/ReviewDetail'
import CreateReview from '@/views/reviews/CreateReview'
import UpdateReview from '@/views/reviews/UpdateReview'
import VoteList from '@/views/votes/VoteList'
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
    path: '/vote',
    name: 'VoteList',
    component: VoteList
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
