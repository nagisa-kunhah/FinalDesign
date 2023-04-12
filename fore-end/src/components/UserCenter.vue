<template>
  <MyTitle></MyTitle>
  <div class="show-info">
    <div class="avatar-block">
      <div class="avatar">
        <el-avatar :size="'large'" :src="img" />
      </div>
    </div>
    <div class="form">
      <div class="form-item">
        用户编号：{{user_id}}
      </div>
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
          <el-button type="primary" plain @click="submit">保存</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import MyTitle from "@/components/MyHead.vue";
import axios from "axios";
import {charAt} from "core-js/internals/string-multibyte";

export default {
  name: "UserCenter",
  components: {MyTitle},
  data(){
    return{
      nick_name:null,
      sex:0,
      birthday:null,
      personal_signature:null,
      input_password:null,
      email:null,
      user_id:null,
      img:require('@/assets/logo.png'),
    }
  },
  created() {
    this.user_id=this.$route.query.user_id
    let data={
      "user_id":this.user_id,
    }
    console.log('??????')
    axios.post('http://localhost:8087/user/GetUserInfo',data).then((res)=>{
      this.nick_name=res.data.nick_name
      this.sex=charAt(res.data.sex,0)
      this.birthday=res.data.birthday
      this.personal_signature=res.data.personalSignature
      this.input_password=res.data.password
      this.email=res.data.email
      console.log(typeof this.sex)
    })
  }
}
</script>

<style scoped>
.avatar-block{
  width: 100%;
  //background-color: red;
  display: flex;
  justify-content: center;
}
.show-info{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin: auto auto;
  width: 90%;
}
.avatar{
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
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