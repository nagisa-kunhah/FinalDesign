<template>
  <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
  >
    <el-menu-item class="my-menu-item" @click="to_home" style="margin-left: 20px">
      主站
    </el-menu-item>
    <div class="grow-user"></div>
    <el-menu-item index="3" v-if="!login" @click="to_login">
      <div class="my-menu-item" >登录</div>
    </el-menu-item>
    <el-menu-item index="4" v-if="!login" @click="to_register">
      <div class="my-menu-item">注册</div>
    </el-menu-item>
    <el-menu-item index="3" v-if="login" style="height: 100%">
      <div class="img-box" style="{display: flex;align-items: center;justify-content: center;height: 100%}">
        <div class="img-show" :style="{backgroundImage:'url('+img+')'}">
        </div>
      </div>
    </el-menu-item>
  </el-menu>
</template>

<script>
import axios from "axios";
import login from "@/components/Login.vue";

export default {
  name: "Navi",
  data(){
    return{
      user_id:null,
      login:false,
      activeIndex:'1',
      img:require('@/assets/logo.png'),
    }
  },
  created(){
    this.set_login()
  },
  methods:{
    to_root(){
      this.$root.user_id=this.user_id
    },
    async set_login() {
      let ret = localStorage.getItem("8080:userInfo")
      if (ret == null) {
        this.login = false
      } else {
        await this.check_jwt(ret)
      }
    },
    async check_jwt(token) {
      let data = {
        "token": token,
      }
      await axios.post("http://localhost:8087/user/CheckLogin", data).then((res) => {
        this.login = (!!res.data.response)
        this.user_id=res.data.user_id
        this.to_root()
      })
    },
    to_home(){
      this.$router.push({name:'home'})
    },
    handleSelect(key, keyPath) {
      console.log(key, keyPath)
    },
    to_register(){
      this.$router.push({name:'Register'})
    },
    to_login(){
      this.$router.push({name:'Login'})
    }
  }
}
</script>

<style scoped>
.el-menu-demo{
  width: 100%;
}
.grow-user{
  width: 80%;
}
.my-menu-item{
  cursor: pointer;
  width: 5%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 100%;
}
.img-show{
  border-radius: 50%;
  overflow: hidden;
  height: 55px;
  width: 55px;
  background-size: cover;
}
</style>