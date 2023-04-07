<template>
<!--  <MyTitle></MyTitle>-->
  <div class="back-draw">
    <div class="Login">
      <div class="title">
        <h1>登录</h1>
      </div>
      <div class="form-item">
        <h3>邮箱：</h3><el-input style="width: 70%" v-model="email" placeholder="输入邮箱" />
      </div>
      <div class="form-item">
        <h3>密码：</h3><el-input
              style="width: 70%"
              v-model="password"
              type="password"
              placeholder="输入密码"
              show-password
          />
      </div>
      <div class="btn">
        <el-button type="primary" @click="Login">登录</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import MyTitle from "@/components/MyHead.vue";
import axios from "axios";
import {ElNotification} from "element-plus";
import {h} from "vue";
import router from "@/router";

export default {
  name: "Login",
  components: {MyTitle},
  data(){
    return{
      email:null,
      password:null,
    }
  },
  methods:{
    Login(){
      let data={
        "password":this.password,
        "email":this.email,
      }
      axios.post('http://localhost:8087/user/Login',data).then((res)=>{
        let ret=res.data.response
        if(ret===true){
          localStorage.setItem("8080:userInfo",res.data.token)
          router.push({name:"home"})
          ElNotification({
            title: '登录成功',
            message: h('i', { style: 'color: teal' }, 'enjoy'),
          })
        }
        else{
          ElNotification({
            title: '登陆失败',
            message: h('i', { style: 'color: teal' }, '为啥呀？我也不知道啊呜呜（。'),
          })
        }
      })
    }
  }
}
</script>

<style scoped>
.back-draw{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}
.Login{
  margin-top: 40px;
  background-color: rgba(0,255,255,0.1);
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  width: 50%;
  //background-color: red;
}
.title{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  width: 100%;
}
.form-item{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80%;
  height: 80px;
  padding: 20px;
  //background-color: yellow;
}
.btn{
  display: flex;
  width: 100%;
  height: 80px;
  align-items: center;
  justify-content: center;
}
</style>