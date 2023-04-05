<template>
  <div class="back-ground">
    <div class="show-ground">
      <div class="img-show">
        <div class="img"></div>
      </div>
      <div class="right">
        <div class="info">
          <div class="title">
            <h1>{{title}}</h1>
          </div>
          <div class="description">
            {{desciption}}
          </div>
          <div class="rating">
            <el-rate v-model="value" allow-half />
            <el-button  @click="submit">提交评价</el-button>
          </div>
        </div>
      </div>
    </div>
    <el-button plain class="back-btn" @click="back">回到首页</el-button>
    <div class="comment_place">
      <div class="input_comment">
        <el-input v-model="input_comment" placeholder="Please input" :size="'default'" type="textarea" rows="5" show-word-limit resize="none"/>
      </div>
      <div class="submit_comment">
        <el-button id="submit-comment-button" type="primary" :size="'large'" @click="submit_comment">Primary</el-button>
      </div>
    </div>
  </div>
<!--  <button @click="get_data"></button>-->
</template>
<script>
import axios, {isCancel, AxiosError, create} from "axios";
import MyTitle from "@/components/MyHead.vue";
export default {
  components: {MyTitle},
  data() {
    return {
      input_comment:null,
      value:null,
      title:"暂无，占位",
      desciption:"暂无，占位"
    };
  },
  methods:{
    submit_comment(){
      axios.post('http://')
    },
    get_data(){
      console.log('数据数据数据:',this.$route.params.title)
    },
    submit(){
      console.log("提交评价")
      ElNotification({
        title: '评价提交成功',
        message: h('i', { style: 'color: teal' }, '评价已提交'),
      })
    },
    back(){
      this.$router.push({ name: 'home'})
    }
  },
  created(){
    this.title=this.$route.query.title
  }
};
import { h } from 'vue'
import { ElNotification } from 'element-plus'

const open1 = () => {
  ElNotification({
    title: '评价提交成功',
    message: h('i', { style: 'color: teal' }, 'This is a reminder'),
  })
}

const open2 = () => {
  ElNotification({
    title: 'Prompt',
    message: 'This is a message that does not automatically close',
    duration: 0,
  })
}
</script>
<style scoped>
.back-ground{
  text-align: center;
  width: 100%;
  min-width: 1080px;
}
.show-ground{
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  display: flex;
  width: 90%;
  overflow: hidden;
  height: 400px;
  //background-color: yellow;
}
.img-show{
  height: 100%;
  width: 35%;
  min-width: 35%;
  //background-color: red;
}
.img{
  background-image: url("@/assets/photo/679.png");
  height: 281px;
  width: 190px;
  margin-top: 10%;
  margin-left: 40%;
  //background-color: green;
}
.description{
  padding: 20px;
  display: flex;
  flex-wrap: wrap;
  word-break: break-all;
  word-wrap: break-word;
  height: 200px;
}
.title{
  font-family: Microsoft Yahei,Tahoma,Helvetica,Arial,"\5B8B\4F53",sans-serif;
  height: 30%;
}
.info{
  padding: 20px;
  font-family: Microsoft Yahei,Tahoma,Helvetica,Arial,"\5B8B\4F53",sans-serif;
}
.right{
  display: flex;
  width: 65%;
  min-width: 65%;
}
.rating{
 height: 90px;
  margin-left: 20px;
  width: 100%;
}

.comment_place{
  display: flex;
  width: 90%;
  //background-color: green;
  margin: 20px auto;
}

.back-btn{
  margin-left: 0;
}
.input_comment{
  min-width: 90%;
}
.submit_comment{
  display: flex;
  justify-content: center;
  align-content: center;
}
#submit-comment-button{
  margin-top: 40%;
  margin-left:50%;
}
</style>
