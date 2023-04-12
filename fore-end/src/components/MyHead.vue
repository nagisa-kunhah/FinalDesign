<template>
  <div id="title">
    <div id="info">
      <Navi></Navi>
    </div>
  </div>
</template>

<script>
import Navi from "@/components/Navi.vue";

export default {
  name: "MyTitle",
  components: {Navi},
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
#info{
  width: 100%;
  opacity: 70%;
}
</style>