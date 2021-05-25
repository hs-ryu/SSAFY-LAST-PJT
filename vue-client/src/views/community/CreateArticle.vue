<template>
  <div>
    <h1 class="mb-4">게시글 작성</h1>
    <div class="mx-auto" style="width: 600px;">
      <div class="d-flex my-3">
        <select v-model="categories" name="categories" id="categories">
          <option disabled value="">말머리</option>
          <option v-if="loginSuperStatus" value="1">공지</option>
          <option value="2">건의</option>
          <option value="3">일상</option>
        </select>
      </div>
      <input class="mb-3" style="width: 600px;" v-model.trim="title" type="text" name="title" id="title" placeholder="제목">
      <br>
      <!-- <input v-model.trim="content" type="text" name="content" id="content"> -->
      <textarea v-model.trim="content" name="content" id="content" cols="70" rows="7" placeholder="내용"></textarea>
      <br>
      <div class="d-flex justify-content-end">
        <input class="mx-2 btn main-color-background text-white" @click="createArticle" type="submit" value="작성">
        <input class="btn main-color-background text-white" @click="$router.go(-1)" type="submit" value="취소">
      </div>
    </div>
    <!-- <label for="title">글 제목</label>
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
    <input @click="createArticle" type="submit" value="작성"> -->
  </div>
</template>

<script>
import SERVER from '@/api/drf.js'
import axios from 'axios'
import { mapGetters, mapState } from 'vuex'

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
    ]),
    ...mapState({
      'loginSuperStatus': 'isSuperuser',
    })
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
        .then((res) => {
          // console.log(res)
          // '/community/articles/:articleId',
          this.$router.push({ name: 'ArticleDetail', params: { articleId: res.data.id } })
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