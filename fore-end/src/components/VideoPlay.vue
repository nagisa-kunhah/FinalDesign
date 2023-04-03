<template>
  <h1>???????????????</h1>
</template>

<script>
export default {
  name: "VedioPlay",
  data(){
    return{
      id:1
    }
  },
  created() {
    this.id=this.$route.query.movieId
  }
}
</script>

<style scoped>

</style>