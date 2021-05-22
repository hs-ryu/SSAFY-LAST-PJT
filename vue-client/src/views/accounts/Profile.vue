<template>
  <div>
    {{userProfile}}
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

export default {
  name: 'Profile',
  data: function () {
    return {
      userId: this.$route.params.userId,
      userProfile: {},
    }
  },
  methods: {
    getUserProfile: function () {
      axios({
        // path('<int:user_id>/', views.profile, name='profile'),
        url: SERVER.URL + `/accounts/${this.userId}/`,
        method: 'get',
      })
      .then((res) => {
        this.userProfile = res.data
      })
    }
  },
  created: function () {
    this.getUserProfile()
  }
}
</script>

<style>

</style>