<template>
  <div>
    <h1>게시글 목록</h1>
    <div v-for="(article, idx) in articles" :key="idx">
      <h2 @click="goToArticleDetail(article.id)">{{ article.title }}</h2>
    </div>
    <button>게시글 작성</button>
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'

export default { 
  name: 'ArticleList',
  components: {
  },
  data: function () {
    return {
      articles: [],
    }
  },
  methods: {
    getAllArticles: function () {
      axios({
        // path('articles/', views.getallarticles, name='getallarticles'),
        url: SERVER.URL + 'community/articles/',
        method: 'get',
      })
      .then((res) => {
        this.articles = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToArticleDetail: function (articleId) {
      this.$router.push({ name: 'ArticleDetail', params: { articleId }})
    },
    goToCreateArticle: function () {
      this.$router.push({ name: 'CreateArticle' })
    }
  },
  created: function () {
    this.getAllArticles()
  }
}
</script>

<style>

</style>