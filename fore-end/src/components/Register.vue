<template>
  <MyTitle></MyTitle>
  <div class="back-draw">
    <div class="form">
      <div class="form-item">
          昵&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp称：
          <el-input style="width: 20%" v-model="nick_name" placeholder="请输入昵称" :rows="1" />
      </div>
      <div class="form-item">
        密&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp码：
        <el-input
            style="width: 20%"
            v-model="input_password"
            type="password"
            placeholder="请输入密码"
            show-password
        />
      </div>
      <div class="form-item">
          性&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp别：
          <el-radio-group v-model="sex" class="ml-4">
            <el-radio label="0" size="large">女</el-radio>
            <el-radio label="1" size="large">男</el-radio>
          </el-radio-group>
      </div>
      <div class="form-item">
        邮&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp箱：
        <el-input v-model="email" placeholder="请输入邮箱" style="width: 190px"/>
      </div>
      <div class="form-item">
        生&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp日：
        <div class="block">
          <el-date-picker
              v-model="birthday"
              type="date"
              placeholder="请输入你的生日"
              size="default"
          />
        </div>
      </div>
      <div class="form-item">
        个性签名：
        <el-input style="width: 70%"
            v-model="personal_signature"
            :rows="2"
            type="textarea"
            placeholder="请输入你的个性签名"
            resize="none"
        />
      </div>
      <div class="form-item">
        <div class="submit-btn">
          <el-button type="primary" plain @click="submit">注册</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyTitle from "@/components/MyHead.vue";
import axios, {isCancel, AxiosError, create} from "axios";
import {ElNotification} from "element-plus";
import {h} from "vue";
import {useRouter} from "vue-router";
import router from "@/router";

export default {
  name: "Register",
  components: {MyTitle},
  data(){
    return{
      nick_name:null,
      sex:null,
      birthday:null,
      personal_signature:null,
      input_password:null,
      email:null,
    }
  },
  methods:{
    submit(){
      let data={
        "nickname":this.nick_name,
        "password":this.input_password,
        "sex":this.sex,
        "birthday":this.birthday,
        "personal_signature":this.personal_signature,
        "input_password":this.input_password,
        "email":this.email,
      }
      axios.post('http://localhost:8087/user/Register',data).then((res)=>{
        let ret=res.data.response
        if(ret===true){
          ElNotification({
            title: '注册成功',
            message: h('i', { style: 'color: teal' }, '可以尝试登陆啦！'),
          })
          router.push({name:"home"})
        }
        else {
          ElNotification({
            title: '注册失败',
            message: h('i', { style: 'color: teal' }, '为啥呀？我也不知道啊呜呜（。'),
          })
        }
      })
    }
  },
}
</script>

<style scoped>
.back-draw{
  display: flex;
  width: 100%;
  //background-color: red;
  justify-content: center;
}
.form{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  width: 70%;
  //background-color: yellow;
}

.form-item{
  display: flex;
  justify-content: left;
  align-items: center;
  width: 90%;
  height: 80px;
}
.submit-btn{
  display: flex;
  justify-content: center;
  width: 100%;
}
</style>