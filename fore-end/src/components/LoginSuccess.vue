<template>
  <MyTitle></MyTitle>
  <h1>登陆成功</h1>
</template>

<script>
import MyTitle from "@/App.vue";

export default {
  name: "LoginSuccess",
  components: {MyTitle},
  created() {
    this.threeGo()
  },
  methods:{
    threeGo(){
      const TIME_COUNT = 3;
      if(!this.timer){
        this.count = TIME_COUNT;
        this.show = false;
        this.timer = setInterval(()=>{
          if(this.count > 0 && this.count <= TIME_COUNT){
            this.count--;
          }else{
            this.show = true;
            clearInterval(this.timer);
            this.timer = null;
            //跳转的页面写在此处
            this.$router.push({
              name:'home'
            });
          }
        },1000)
      }
    },
  }
}
</script>

<style scoped>

</style>