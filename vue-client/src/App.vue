<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">LOGO</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex justify-content-between align-items-center">
                <span class="d-flex">
                  <li class="nav-item px-2">
                    <router-link :to="{ name: 'MovieList' }">Main</router-link>
                  </li>
                  <li class="nav-item px-2">
                    <router-link :to="{ name: 'ArticleList' }">Community</router-link>
                  </li>
                </span>
                <span class="d-flex">
                  <li class="mb-0 nav-item px-2 justify-content-end">
                    <p v-if="isLoggedIn">{{ username }}님, 환영합니다!</p>
                    <p v-else>손님, 환영합니다!</p>
                  </li>
                </span>
            </ul>
            <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex justify-content-end align-items-center">
            </ul>
            <span v-if="isLoggedIn">
              <router-link @click.native="logout" to="#">Logout</router-link>
              <router-link :to="{ name: 'Profile', params: { username }}">Mypage</router-link>
              <a v-if="isSuperuser" href="http://127.0.0.1:8000/admin/">SYSTEM</a>
            </span>
            <span v-else>
              <router-link :to="{ name: 'Signup' }">Signup</router-link>
              <router-link :to="{ name: 'Login' }">Login</router-link>
              <!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                로그인
              </button> -->
            </span>
            <!-- <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button style="color: white" class="btn main-color-background" type="submit">Search</button>
            </form> -->
          </div>
        </div>
      </nav>
      <!-- Modal -->
      <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">로그인</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <form>
                <div class="mb-3">
                  <input type="text" class="form-control" id="username" v-model="credentials.username" placeholder="아이디">
                </div>
                <div class="mb-3">
                  <input
                    class="form-control" 
                    type="password" 
                    id="password"
                    placeholder="비밀번호" 
                    v-model="credentials.password"
                    @keypress.enter="login(credentials)"
                  >
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">회원가입</button>
              <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="login(credentials)">로그인</button>
            </div>
          </div>
        </div>
      </div>
        <!-- <p v-if="isLoggedIn">{{ username }}님 환영합니다!</p>
        <p v-else>손님 환영합니다!</p>
        <router-link :to="{ name: 'MovieList' }">Main</router-link> |
        <router-link :to="{ name: 'ArticleList' }">Community</router-link> |
      <span v-if="isLoggedIn">
        <router-link @click.native="logout" to="#">Logout</router-link> |
        <router-link :to="{ name: 'Profile', params: { username }}">Mypage</router-link>
        <a v-if="isSuperuser" href="http://127.0.0.1:8000/admin/">SYSTEM</a>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link>
      </span> -->
    </div>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'

export default {
  name: 'App',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    ...mapActions([
      'logout',
      'get_user_info',
      'login',
    ])
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
    ]),
    ...mapState([
      'username',
      'userId',
      'isSuperuser',
    ])
  },
  created: function () {
    this.get_user_info()
  }
}
</script>
<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Nanum Gothic', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

/* #nav {
  padding: 30px;
} */

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

#nav a.router-link-exact-active {
  color: #CE93D8;
}

.main-color-content {
  color: #CE93D8;
}

.main-color-background {
  background-color: #CE93D8;
}

.custom-button {
  background-color: #CE93D8;
  color: white;
}
</style>
