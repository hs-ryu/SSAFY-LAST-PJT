<template>
  <div>
    <div class="mx-auto" style="width: 700px;">
      <h1 style="text-align: left;" class="fw-bold">{{ article.title }}</h1>
      <div style="text-align: left;">
        <h4 class="d-inline" @click="goToProfile">{{ article.username }}</h4>
        <h4 class="mx-3 d-inline">|</h4>
        <div class="d-inline" v-if="article.categories=='1'">
          <h4 class="d-inline">[공지사항]</h4>
        </div>
        <div class="d-inline" v-else-if="article.categories=='2'">
          <h4 class="d-inline">[건의사항]</h4>
        </div>
        <div class="d-inline" v-else-if="article.categories=='3'">
          <h4 class="d-inline">[자유글]</h4>
        </div>
      </div>
      <p>글 내용: {{ article.content }}</p>
      <button @click="deleteArticle">삭제</button>
      <button @click="goToUpdateArticle">수정</button>
    </div>
    <div>
      <p>{{ article.like_users.length }}명이 좋아합니다.</p>
      <button v-if="article.like_users.includes(userId)" @click="getLikeStatus">좋아요취소</button>
      <button v-else @click="getLikeStatus">좋아요</button>
    </div>
    <div>
      <h2>댓글목록</h2>
      <label for="comment">댓글작성</label>
      <input v-model="commentContent" type="text" name="comment" id="comment">
      <input @click="createComment" type="submit" value="작성">
      <ArticleComment
        v-for="(comment, idx) in comments"
        :key="idx"
        :comment="comment"
        :articleId="articleId"
        @comment-deleted="getArticleComments"
        @modify-activate="getArticleComments"
      />
    </div>
    {{ article }}
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import ArticleComment from '@/components/ArticleComment'
import { mapGetters, mapState } from 'vuex'

export default {
  name: 'ArticleDetail',
  components: {
    ArticleComment,
  },
  data: function () {
    return {
      articleId: this.$route.params.articleId,
      article: {},
      commentContent: '',
      comments: [],
    }
  },
  computed: {
    ...mapGetters([
      'config'
    ]),
    ...mapState([
      'userId'
    ])
  },
  methods: {
    // path('articles/<int:article_pk>/', views.getarticle, name='getarticle'),
    getArticleDetail: function() {
      const headers = this.config
      axios({
        url: SERVER.URL + `/community/articles/${this.articleId}`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getArticleComments: function () {
      const headers = this.config
      axios({
        // path('articles/<int:article_pk>/comments/', views.getallcomments, name='getallcomments'),
        url: SERVER.URL + `/community/articles/${this.articleId}/comments/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteArticle: function () {
      const headers = this.config
      axios({
        // path('articles/<int:article_pk>/deletearticle/', views.deletearticle, name='deletearticle'),
        url: SERVER.URL + `/community/articles/${this.articleId}/deletearticle/`,
        method: 'delete',
        headers,
      })
      .then(() => {
        this.$router.push({ name: 'ArticleList' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToUpdateArticle: function () {
      this.$router.push({ name: 'UpdateArticle', params: { articleId: this.articleId }, query: { article: this.article }})
    },
    createComment: function () {
      const commentItem = {
        content: this.commentContent,
      }
      if (commentItem.content) {
        const headers = this.config
        axios({
          // path('articles/<int:article_pk>/createcomment/', views.createcomment, name='createcomment'),
          url: SERVER.URL + `/community/articles/${this.articleId}/createcomment/`,
          method: 'post',
          data: commentItem,
          headers,
        })
        .then(() => {
          this.commentContent = ''
          this.getArticleComments()
          // this.$router.push({ name: 'ReviewDetail', params: { movieId: this.movieId, reviewId: this.reviewId }})
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    getLikeStatus: function () {
      const headers = this.config
      axios({
        // 'articles/<int:article_pk>/likes/'
        url: SERVER.URL + `/community/articles/${this.articleId}/likes/`,
        method: 'post',
        headers,
      })
      .then(() => {
        // const { likeCount } = res.data
        // this.likeCount = likeCount
        // this.likeStatus = liked
        this.getArticleDetail()
      })
    },
    goToProfile: function () {
      const userName = this.article.username
      this.$router.push({ name: 'Profile', params: { username: userName }})
    },
  },
  created: function () {
    this.getArticleDetail()
    // 현선 추가
    this.getArticleComments()
  }
}
</script>

<style>

</style>