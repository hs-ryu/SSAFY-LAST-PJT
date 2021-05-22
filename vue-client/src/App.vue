<template>
  <div id="app">
    <div id="nav">
        <p v-if="isLoggedIn">{{ username }}님 환영합니다!</p>
        <p v-else>손님 환영합니다!</p>
        <router-link :to="{ name: 'MovieList' }">Main</router-link> |
        <router-link :to="{ name: 'ArticleList' }">Community</router-link> |
      <span v-if="isLoggedIn">
        <router-link @click.native="logout" to="#">Logout</router-link> |
        <a v-if="isSuperuser" href="http://127.0.0.1:8000/admin/">SYSTEM</a>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link>
      </span>
    </div>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'

export default {
  name: 'App',
  methods: {
    ...mapActions([
      'logout',
      'get_user_info',
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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
