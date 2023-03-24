<template>
  <div id="title">
    <div id="mine-header">

    </div>
  </div>
  <div id="p1">
    <div id="my-swipper">
      <swiper class="swiper" :modules="modules" :pagination="{ clickable: true }">
        <swiper-slide class="slide">
          <div class="swiper-img">p1</div>
        </swiper-slide>
        <swiper-slide class="slide">
          <div class="swiper-img">p2</div>
        </swiper-slide>
      </swiper>
    </div>
    <div id="p1-content-right">

    </div>
  </div>
  <button id="btn" @click="receive">receive</button>
  <button id="btn-send" @click="send">send</button>
</template>

<script>
import {Swiper,SwiperSlide } from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/pagination'
import {Pagination} from "swiper";
import axios,{isCancel,AxiosError} from "axios";
export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  methods:{
    receive(event){
     axios.get('http://localhost:8087/user/test').then((res)=>{
       console.log('数据:',res)
     })
    },
    send(event){
      let data={
        id:1
      }
      console.log(data)
      try {
        axios.post('http://localhost:8087/user/test_input', data).then((res)=>{
           console.log(res)
        })
        // console.log(res)
      }catch (err){
        console.log(err)
      }
    }
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
#title{
  display: flex;
  background-image: url("~@/assets/title.jpg");
  background-repeat: no-repeat;
  background-position: center 0;
  background-size: cover;
  height: 140px;
  justify-content: center;
}
.swiper-img{
  width: 100%;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: red;
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
  //background-color: blue;
  border: dashed;
}
a {
  color: #42b983;
}

</style>
