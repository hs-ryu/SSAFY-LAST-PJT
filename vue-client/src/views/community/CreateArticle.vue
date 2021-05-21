<template>
  <div>
    <h1>글 작성</h1>
    <label for="title">글 제목</label>
    <input v-model.trim="title" type="text" name="title" id="title">
    <label for="categories">분류</label>
    <select v-model="categories" name="categories" id="categories">
      <option disabled value="">분류를 선택해 주세요</option>
      <option value="1">공지사항</option>
      <option value="2">건의사항</option>
      <option value="3">자유글</option>
    </select>
    <label for="content">글 내용</label>
    <input v-model.trim="content" type="text" name="content" id="content">
    <input @click="createArticle" type="submit" value="작성">
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'CreateArticle',
  data: function () {
    return {
      title: '',
      categories: '',
      content: '',
    }
  },
  computed: {
    ...mapGetters([
      'config'
    ])
  },
  methods: {
    createArticle: function () {
      const headers = this.config
      const articleItem = {
        title: this.title,
        categories: this.categories,
        content: this.content,
      }
      // console.log(articleItem)
      if (articleItem.title && articleItem.categories && articleItem.content) {
        // path('createarticle/', views.createarticle, name='createarticle'),
        axios({
          url: SERVER.URL + '/community/createarticle/',
          method: 'post',
          data: articleItem,
          headers,
        })
        .then(() => {
          // console.log(res)
          this.$router.push({ name: 'ArticleList' })
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