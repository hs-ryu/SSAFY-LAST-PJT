<template>
  <div>
    <h1>글 작성</h1>
    <label for="title">글 제목</label>
    <input v-model.trim="title" type="text" name="title" id="title">
    <label for="category">분류</label>
    <select v-model="category" name="category" id="category">
      <option disabled value="">분류를 선택해 주세요</option>
      <option value="1">공지사항</option>
      <option value="2">건의사항</option>
      <option value="3">자유글</option>
    </select>
    <label for="content">글 내용</label>
    <input v-model.trim="content" type="text" name="content" id="content">
    <input @click="createArticle(title, category, content)" type="submit" value="작성">
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

export default {
  name: 'CreateArticle',
  data: function () {
    return {
      title: '',
      category: '',
      content: '',
    }
  },
  methods: {
    createArticle: function (title, category, content) {
      const articleItem = {
        title,
        category,
        content,
      }
      if (articleItem.title && articleItem.category && articleItem.content) {
        // path('createarticle/', views.createarticle, name='createarticle'),
        axios({
          url: SERVER.URL + 'community/createarticle/',
          method: 'post',
          data: articleItem,
        })
        .then(() => {
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