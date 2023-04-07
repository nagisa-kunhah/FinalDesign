<template>
<!--  <MyHead></MyHead>-->
  <div id="p1">
    <div id="my-swipper">
      <swiper
          class="swiper"
          :modules="modules"
          :space-between="30"
          :centered-slides="true"
          :navigation="true"
          :pagination="{
            clickable: true
           }"
          :autoplay="{
      delay: 2500,
      disableOnInteraction: false
      }">
        <swiper-slide class="slide">
          <div class="swiper-img">{{slide_recommend[0]}}</div>
        </swiper-slide>
        <swiper-slide class="slide">
          <div class="swiper-img">{{slide_recommend[1]}}</div>
        </swiper-slide>
      </swiper>
    </div>
    <div id="p1-content-right">
      <div class="movie-preview" @mouseenter="mouseenter(0)" @mouseleave="mouseleave(0)" @click="img_jump(0)">
        <div class="screen" :style="{backgroundImage:'url('+imgs[0]+')'}">
        </div>
        <div class="info" :style="{top:top_value[0]}">
          <p class="movie-title" :title=titles[0]>{{titles[0]}}</p>
        </div>
      </div>

      <div class="movie-preview" @mouseenter="mouseenter(1)" @mouseleave="mouseleave(1)" @click="img_jump(1)">
        <div class="screen" :style="{backgroundImage:'url('+imgs[1]+')'}">
        </div>
        <div class="info" :style="{top:top_value[1]}">
          <p class="movie-title" :title=titles[1]>{{titles[1]}}</p>
        </div>
      </div>
      <div class="movie-preview" @mouseenter="mouseenter(2)" @mouseleave="mouseleave(2)" @click="img_jump(2)">
        <div class="screen" :style="{backgroundImage:'url('+imgs[2]+')'}">
        </div>
        <div class="info" :style="{top:top_value[2]}">
          <p class="movie-title" :title=titles[2]>{{titles[2]}}</p>
        </div>
      </div>
        <div class="movie-preview" @mouseenter="mouseenter(3)" @mouseleave="mouseleave(3)" @click="img_jump(3)">
          <div class="screen" :style="{backgroundImage:'url('+imgs[3]+')'}">
          </div>
            <div class="info" :style="{top:top_value[3]}">
              <p class="movie-title" :title=titles[3]>{{titles[3]}}</p>
            </div>
        </div>
      <div class="movie-preview" @mouseenter="mouseenter(4)" @mouseleave="mouseleave(4)" @click="img_jump(4)">
        <div class="screen" :style="{backgroundImage:'url('+imgs[4]+')'}">
        </div>
        <div class="info" :style="{top:top_value[4]}">
          <p class="movie-title" :title=titles[4]>{{titles[4]}}</p>
        </div>
      </div>
      <div class="movie-preview" @mouseenter="mouseenter(5)" @mouseleave="mouseleave(5)" @click="img_jump(5)">
        <div class="screen" :style="{backgroundImage:'url('+imgs[5]+')'}">
        </div>
        <div class="info" :style="{top:top_value[5]}">
          <p class="movie-title" :title=titles[5]>{{titles[5]}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {Swiper,SwiperSlide} from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/pagination'
import {Pagination} from "swiper";
import MyHead from "@/components/MyHead.vue";
import axios from "axios";
export default {
  name: "HelloWorld",
  data(){
    return{
      top_value:new Array(6).fill('70%'),
      imgs:[],
      titles:[],
      val:1,
      slide_recommend:["占位","占位"],
      movie_id:[]
    }
  },
  watch:{
    imgs(){
      this.fresh_recommend()
    }
  },
  computed:{
    default_img:{
      get(){
        return require('@/assets/logo.png')
      },
    }
  },
  components: {
    MyHead,
    Swiper,
    SwiperSlide,
  },
  created() {
    this.fresh_recommend()
  },
  methods:{
    img_jump(id){
      console.log(id)
      // console.log("aaaaaa")
      this.$router.push({ name: 'VideoRating', query: { movie_id:this.movie_id[id],title:this.titles[id] } })
    },
    mouseenter:function (index){
      this.top_value[index]='20%'
    },
    mouseleave:function (index){
      this.top_value[index]='70%'
    },
    fresh_recommend(){
      let data={
        id:1
      }
      axios.post("http://localhost:8087/user/get_recommend",data).then((res)=>{
        let recommends=res.data.recommend
        this.movie_id=[]
        this.titles=[]
        console.log("recommend:",res.data)
        for(let i=0;i<recommends.length;i++){
          this.movie_id.push(recommends[i])
          let file_name='@/assets/photo/'+recommends[i]+'.jpg'
          try{
            let required=require(file_name)
            this.imgs.push(required)
          }catch (e){
            console.log("error!")
            this.imgs.push(this.default_img)
          }
        }
        let recommend_title=res.data.recommend_title
        for(let i=0;i<recommend_title.length;i++){
          this.titles.push(recommend_title[i])
        }
        console.log(this.titles)
      })
    },
  },
  setup() {
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = () => {
      console.log('slide change');
    };
    return {
      onSwiper,
      onSlideChange,
      modules: [Pagination],
    };
  }
}
</script>
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}

.swiper-img{
  width: 100%;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  //background-color: red;
}
.info{
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 2;
  //top: 70%;
}
#p1{
  margin-top: 10px;
  display: flex;
  height: 300px;
}
#my-swipper{
  width: 50%;
  margin-right: 10px;
}
.slide{
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
#p1-content-right{
  height: 300px;
  width: 50%;
  border: dashed;
}
#p1-content-right{
  display: flex;
  justify-content: space-between;
  align-content: space-between;
  flex-wrap: wrap;
}
.movie-preview{
  cursor: pointer;
  position: relative;
  margin: auto;
  //background-color: blue;
  width: 33%;
  height: 49%;
  justify-content: space-around;
  overflow: hidden;
}
.movie-title{
  text-align: center;
  height: 20%;
  width: 100%;
  font-size: 10px;
}
.screen{
  position: relative;
  margin: auto;
  background-color: white;
  width: 50%;
  height: 100%;
  background-size: 100%,100%;
  background-repeat: no-repeat;
}
a {
  color: #42b983;
}

</style>
