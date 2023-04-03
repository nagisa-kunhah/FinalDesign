<template>
  <div id="title">
    <div id="mine-header">
    </div>
  </div>
</template>

<script>
export default {
  name: "MyTitle"
}
</script>

<style scoped>
#title{
  display: flex;
  background-image: url("~@/assets/title.jpg");
  background-repeat: no-repeat;
  background-position: center 0;
  background-size: cover;
  height: 140px;
  justify-content: center;
}
</style>