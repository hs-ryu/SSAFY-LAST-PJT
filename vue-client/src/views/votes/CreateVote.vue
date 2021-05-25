<template>
  <div>
    <div class="mx-auto" style="width: 600px;">
      <label for="title">제목</label>
      <input style="width: 500px;" v-model.trim="title" type="text" name="title" id="title">
      <br>
      <label for="optionone">첫번째</label>
      <input style="width: 500px;" v-model.trim="optionone" type="text" name="optionone" id="optionone">
      <br>
      <label for="optiontwo">두번째</label>
      <input style="width: 500px;" v-model.trim="optiontwo" type="text" name="optiontwo" id="optiontwo">
      <br>
      <div class="d-flex justify-content-end">
        <input class="mx-2 btn main-color-background text-white" @click="createVote(title, optionone, optiontwo)" type="submit" value="작성">
        <input class="btn main-color-background text-white" @click="$router.go(-1)" type="submit" value="취소">
      </div>
    </div>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'CreateVote',
  data: function () {
    return {
      title: '',
      rank: 0,
      optionone: '',
      optiontwo:'',
      movieId: this.$route.params.movieId,
    }
  },
  computed: {
    ...mapGetters([
      'config',
    ])
  },
  methods: {
    createVote: function (title, optionone, optiontwo) {
      const headers = this.config
      const VoteItem = {
        title: title,
        option_one: optionone,
        option_two: optiontwo,
      }
      if (VoteItem.title && VoteItem.option_one && VoteItem.option_two) {
        // path('<int:movie_pk>/createvote/', views.createvote, name='createvote'),
        axios({
          url: SERVER.URL + SERVER.ROUTES.votes + `${this.movieId}/createvote/`,
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
        .catch((err) => {
          console.log(err)
        })
      }
    }
  }
}
</script>

<style>

</style>