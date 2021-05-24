<template>
  <div>
    <h1 class="mb-4">투표 만들기</h1>
    <div class="mx-auto" style="width: 600px;">
      <input class="mb-3" style="width: 600px;" v-model.trim="title" type="text" name="title" id="title" placeholder="제목">
      <input class="mb-3" style="width: 600px;" v-model.trim="optionone" type="text" name="optionone" placeholder="첫번째 주제">
      <input class="mb-3" style="width: 600px;" v-model.trim="optiontwo" type="text" name="optiontwo" placeholder="두번째 주제">
      <div class="d-flex justify-content-end">
        <input class="mx-2 btn main-color-background text-white" @click="createVote" type="submit" value="작성">
        <input class="btn main-color-background text-white" @click="$router.go(-1)" type="submit" value="취소">
      </div>
    </div>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters, mapState } from 'vuex'

export default {
  name:'CreateVote',
  data: function() {
    return {
      title: '',
      optionone: '',
      optiontwo: '',
      movieId: this.$route.params.movieId,
      movieTitle: this.$route.query.movieTitle,
    }
  },
  computed: {
    ...mapGetters([
      'config'
    ]),
    ...mapState({
      'loginSuperStatus' : 'isSuperuser',
    })
  },
  methods: {
    createVote: function () {
      const headers = this.config
      const VoteItem = {
        title: this.title,
        option_one: this.optionone,
        option_two: this.optiontwo,
      }
      if (VoteItem.title && VoteItem.option_one && VoteItem.option_two) {
        // path('<int:movie_pk>/createvote/', views.createvote, name='createvote'),
        axios({
          url: SERVER.URL + '/movies/' + `${this.movieId}/createvote/`,
          method: 'post',
          data: VoteItem,
          headers,
        })
        .then(() => {
          this.title = ''
          this.optionone = ''
          this.optiontwo = ''
          this.$router.push({ name: 'MovieDetail', params: { movieId: this.movieId}})
        })
      }
    }
  }
}
</script>

<style>

</style>