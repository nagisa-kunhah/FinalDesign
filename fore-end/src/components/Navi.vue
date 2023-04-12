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
    <el-menu-item index="3" v-if="!this.$root.login" @click="to_login">
      <div class="my-menu-item" >登录</div>
    </el-menu-item>
    <el-menu-item index="4" v-if="!this.$root.login" @click="to_register">
      <div class="my-menu-item">注册</div>
    </el-menu-item>
    <el-menu-item index="3" v-if="this.$root.login" style="height: 100%" @click="to_center">
        <div class="img-box" style="{display: flex;align-items: center;justify-content: center;height: 100%}">
            <div class="img-show" :style="{backgroundImage:'url('+img+')'}">
            </div>
        </div>
    </el-menu-item>
    <el-menu-item index="4" v-if="this.$root.login" style="height: 100%" @click="logout">
      <div class="my-menu-item" >登出</div>
    </el-menu-item>
  </el-menu>
</template>

<script>
import axios from "axios";

export default {
  name: "Navi",
  data(){
    return{
      activeIndex:'1',
      img:require('@/assets/logo.png'),
    }
  },
  created(){
    console.log('navi: to set login')
    console.log('navi: set login!',this.$root.user_id,'  ',this.$root.login)
  },
  methods:{
    to_center(){
      this.$router.push({name:"UserCenter",query:{
          user_id:this.user_id,
        }})
    },
    to_home(){
      this.$router.push({name:'home'})
    },
    logout(){
      localStorage.removeItem("8080:userInfo")
      this.$router.go(0)
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