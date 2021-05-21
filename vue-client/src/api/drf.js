const URL = process.env.VUE_APP_SERVER_URL

export default {
  URL,
  ROUTES: {
    signup: '/accounts/signup/',
    login: '/accounts/api-token-auth/',
    getAllMovies: '/movies/getmovies/',
    getPopularMovies: '/movies/getpopularmovies/',
    getNowShowing: '/movies/getnowshowing/',
    reviews: '/movies/',
  }
}