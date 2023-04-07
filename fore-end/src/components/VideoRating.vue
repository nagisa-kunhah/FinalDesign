<template>
<!--  <MyTitle></MyTitle>-->
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
    <div class="comment_place">
      <div class="write-comment">
        <div class="input_comment">
          <el-input v-model="input_comment" placeholder="Please input" :size="'default'" type="textarea" rows="5" show-word-limit resize="none"/>
        </div>
        <div class="submit_comment">
          <el-button id="submit-comment-button" type="primary" :size="'large'" @click="submit_comment">发表评论</el-button>
        </div>
      </div>
      <div v-for="item in comment_list" style="width: 100%">
        <CommentItem :info="item" style="{width: 100%;margin-top: 20px;}"></CommentItem>
      </div>
    </div>
  </div>
  <button @click="fresh_comment" style="{width: 20px;height: 20px;}">???</button>
</template>
<script>
import axios from "axios";
import MyTitle from "@/components/MyHead.vue";
export default {
  components: {CommentItem, UComment, MyTitle},
  data() {
    return {
      movie_id: null,
      input_comment: null,
      value: null,
      title:"暂无，占位",
      desciption:"暂无，占位",
      comment_list:JSON.parse("[]")
    };
  },
  methods:{
    async submit_comment() {
      let date1 = {
        "txt": this.input_comment,
        "skipBidi": false,
      }
      let check=true
      await this.$axios.post('/api/json-filter',date1).then((res) => {
        console.log(res)
        if (res.data.riskLevel !== "PASS") {
          check=false
          ElNotification({
            title: '评论发表失败',
            message: h('i', {style: 'color: teal'}, '评论发表失败'),
          })
        }
      })
      if(!check){
        return
      }
      let data = {
        "belong_movie_id": this.movie_id,
        "user_id": this.$root.user_id,
        "comment": this.input_comment,
      }
      await axios.post('http://localhost:8087/user/SendComment', data).then((res) => {
        console.log(res.data.response)
        if (res.data.response === true) {
          ElNotification({
            title: '评论发表成功',
            message: h('i', {style: 'color: teal'}, '评论发表成功'),
          })
        } else {
          ElNotification({
            title: '评论发表失败',
            message: h('i', {style: 'color: teal'}, '评论发表失败'),
          })
        }
      })
      this.fresh_comment()
    },
    submit(){
      console.log("提交评价")
      ElNotification({
        title: '评价提交成功',
        message: h('i', { style: 'color: teal' }, '评价已提交'),
      })
    },
    async fresh_comment() {
      this.comment_list=JSON.parse("[]")
      // console.log(this.comment_list[0]["CommentId"])
      let data = {
        "belong_movie_id": this.movie_id,
      }
      await axios.post('http://localhost:8087/user/SelectComment', data).then((res) => {
        for(let i=0; i<res.data.content.length; i++){
          this.comment_list.push(res.data.content[i])
        }
      })
    },
  },
  created(){
    this.title=this.$route.query.title
    this.movie_id=this.$route.query.movie_id
    // this.fresh_comment()
  }
};
import { h } from 'vue'
import { ElNotification } from 'element-plus'
import {UComment} from "undraw-ui";
import CommentItem from "@/components/CommentItem.vue";


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
  display: flex;
  justify-content: left;
  height: 90px;
  margin-left: 20px;
  width: 100%;
}

.comment_place{
  display: flex;
  width: 90%;
  flex-wrap: wrap;
  //background-color: green;
  margin: 20px auto;
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
.write-comment{
  display: flex;
  width: 100%;
}
</style>
