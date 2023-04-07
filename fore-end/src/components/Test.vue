<template>
  {{val==null}}
</template>

<script>
export default {
  name: "Test",
  data(){
    return{
      val:null,
    }
  },
  created() {
    this.val=localStorage.getItem("23333")
  }
}
</script>

<style scoped>

</style>