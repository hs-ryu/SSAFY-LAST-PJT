const URL = process.env.VUE_APP_SERVER_URL
const KOFIC_API_KEY = process.env.VUE_APP_KOFIC_API_KEY

export default {
  URL,
  KOFIC_API_KEY,
  ROUTES: {
    getAllMovies: '/getmovies/',
    getPopularMovies: '/getpopularmovies/',
    getNowShowing: '/getnowshowing/',
  }
}