<template>
  <div>
    <h1>글 수정</h1>
    <label for="title">글 제목</label>
    <input :value="article.title" @change="updateTitle" type="text" name="title" id="title">
    <label for="category">분류</label>
    <select :value="article.category" @onchange="updateCategory" name="category" id="category">
      <option disabled value="">분류를 선택해 주세요</option>
      <option value="1">공지사항</option>
      <option value="2">건의사항</option>
      <option value="3">자유글</option>
    </select>
    <label for="content">글 내용</label>
    <input :value="article.content" @change="updateContent" type="text" name="content" id="content">
    <input @click="updateArticle" type="submit" value="수정">
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

export default {
  name: 'UpdateArticle',
  data: function () {
    return {
      article: this.$route.query.article,
      title: '',
      category: '',
      content: '',
    }
  },
  methods: {
    updateTitle: function (event) {
      this.title = event.target.value
    },
    updateCategory: function (event) {
      this.category = event.target.value
    },
    updateContent: function (event) {
      this.content = event.target.value
    },
    updateArticle: function () {
      const articleId = this.$route.params.articleId
      const title = this.title ? this.title : this.article.title
      const category = this.category ? this.category : this.article.category
      const content = this.content ? this.content : this.article.content
      const articleItem = {
        title,
        category,
        content,
      }
      console.log(articleItem.title)
      if (articleItem.title && articleItem.category && articleItem.content) {
        axios({
          // path('articles/<int:article_pk>/updatearticle/', views.updatearticle, name='updatearticle'),
          url: SERVER.URL + `community/articles/${articleId}/updatearticle/`,
          method: 'put',
          data: articleItem,
        })
        .then(() => {
          this.$router.push({ name: 'articleDetail', params: { articleId: articleId}})
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