import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieList from '@/views/movies/MovieList.vue'
import MovieDetail from '@/components/MovieDetail.vue'
import ReviewList from '@/views/reviews/ReviewList.vue'
import VoteList from '@/views/votes/VoteList.vue'
import Signup from '@/views/accounts/Signup.vue'
import Login from '@/views/accounts/Login.vue'

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
    path: '/review',
    name: 'ReviewList',
    component: ReviewList
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
