<template>
  <MyTitle></MyTitle>
  <router-view></router-view>
</template>
<script>
import MyTitle from "@/components/MyHead.vue";

export default {
  components: {MyTitle},
  data(){
    return{
      user_id:null
    }
  }
}
</script>
