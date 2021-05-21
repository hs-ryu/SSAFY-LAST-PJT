const URL = process.env.VUE_APP_SERVER_URL

export default {
  URL,
  ROUTES: {
    getAllMovies: '/movies/getmovies/',
    getPopularMovies: '/movies/getpopularmovies/',
    getNowShowing: '/movies/getnowshowing/',
    reviews: '/movies/',
  }
}