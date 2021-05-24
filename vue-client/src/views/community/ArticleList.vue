<template>
  <div class="mx-auto" style="width: 1000px;">
    <h1>게시글 목록</h1>
    <div class="my-2 d-flex justify-content-end">
      <button class="mx-2 btn btn-sm main-color-background text-white" @click="goToCreateArticle">게시글 작성</button>
    </div>
    <!-- {{ articles }} -->
    <div style="width: 1000px; height: 400px;" class="mx-auto">
      <table class="table table-hover content-font">
        <thead>
          <tr class="text-center">
            <th scope="col">글번호</th>
            <th scope="col">말머리</th>
            <th scope="col">글제목</th>
            <th scope="col">글쓴이</th>
            <th scope="col">날짜</th>
            <th scope="col">좋아요</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(article, idx) in displayArticles" :key="idx">
            <th class="text-center" scope="row">{{ article.id }}</th>
            <td v-if="article.categories==1" class="text-center" scope="row">공지사항</td>
            <td v-else-if="article.categories==2" class="text-center" scope="row">자유글</td>
            <td v-else class="text-center" scope="row">건의사항</td>
            <td class="text-center" @click="goToArticleDetail(article.id)">
              {{ article.title }}
            </td>
            <td class="text-center" @click="goToProfile(article.username)">
              {{ article.username }}
            </td>
            <td class="text-center">{{ article.created_at.substring(0,10) }}</td>
            <td class="text-center">{{ article.like_users.length }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center">
        <li class="page-item">
          <button type="button" class="text-dark page-link" v-if="page != 1" @click="page--"> Previous </button>
        </li>
        <li class="page-item" v-for="(pageNumber,idx) in pages.slice(page-1, page+5)" :key=idx>
          <button type="button" class="text-dark page-link"  @click="page=pageNumber">{{ pageNumber }}</button>
        </li>
        <li class="page-item">
          <button type="button" @click="page++" v-if="page < pages.length" class="text-dark page-link"> Next </button>
        </li>
      </ul>
    </nav>
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
      page: 1,
			perPage: 9,
			pages: [],	
    }
  },
  methods: {
    getAllArticles: function () {
      axios({
        // path('articles/', views.getallarticles, name='getallarticles'),
        url: SERVER.URL + '/community/articles/',
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
    },
    goToProfile: function (username) {
      console.log(username)
      const userName = username
      this.$router.push({ name: 'Profile', params: { username: userName }})
    },
    setPages: function () {
      let numberOfPages = Math.ceil(this.articles.length / this.perPage)
      for (let index=1; index <= numberOfPages; index++)
      {
        this.pages.push(index)
      }
    },
    paginate: function (articles) {
      let page = this.page
      let perPage = this.perPage
      let from = (page * perPage) - perPage;
      let to = (page * perPage)
      return articles.slice(from, to)
    }

  },

  computed: {
    displayArticles () {
      return this.paginate(this.articles);
    }
  },
  watch: {
    articles () {
      this.setPages()
    }
  },
  created: function () {
    this.getAllArticles()
  }
}
</script>

<style>

</style>