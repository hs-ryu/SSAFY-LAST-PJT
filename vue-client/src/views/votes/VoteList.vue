<template>
  <div>
    <h1>투표목록</h1>
    <VoteItem />
  </div>
</template>

<script>
import VoteItem from '@/components/VoteItem'

export default {
  name: 'VoteList',
  components: {
    VoteItem
  }
}
</script>

<style>

</style>