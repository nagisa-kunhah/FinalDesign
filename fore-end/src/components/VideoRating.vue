<template>
  <MyTitle></MyTitle>
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
        </div>
      </div>
    </div>
  </div>
  <div style="width: 20%;height: 30px">
    <el-rate
        v-model="value"
        show-text>
    </el-rate>
  </div>
</template>
<script>
import MyTitle from "@/components/MyTitle.vue";
export default {
  components: {MyTitle},
  data() {
    return {
      value:null,
      title:"博人传 火影忍者新时代",
      desciption:"简介：随着和平的到来而走向近代化的木叶隐村。高楼林立，巨大显示屏中播放出影像，连结各区域的电车在村里奔驰。虽说是忍者村，但一般民众也增多，忍者的生存方式也在逐渐改变的这个时代——村子的领袖、第七代火影·漩涡鸣人的儿子博人，进入了培育忍者的学校“忍者学校”。周围的学生们带着“火影的儿子”这样偏见的目光看待博人，但博人凭借天生的破天荒性格将这种小事轻松越过！博人与新的伙伴相遇，他将如何挑战突然发生的神秘事件？在众人心中如疾风般狂奔的“漩涡博人”的物语，现在开始！！"
    };
  }
};
</script>

<style scoped>
.back-ground{
  display: flex;
  justify-content: center;
  align-content: center;
  width: 100%;
}
.show-ground{
  margin-top: 20px;
  display: flex;
  width: 90%;
  overflow: hidden;
  height: 400px;
  background-color: yellow;
}
.img-show{
  height: 100%;
  width: 35%;
  min-width: 35%;
  background-color: red;
}
.img{
  background-image: url("@/assets/photo/679.png");
  height: 281px;
  width: 190px;
  margin-top: 10%;
  margin-left: 40%;
  background-color: green;
}
.description{
  padding: 20px;
  display: flex;
  height: 80px;
  flex-wrap: wrap;
  word-break: break-all;
  word-wrap: break-word;
}
.title{
  font-family: Microsoft Yahei,Tahoma,Helvetica,Arial,"\5B8B\4F53",sans-serif;
  color: white;
}
.info{
  padding: 20px;
  font-family: Microsoft Yahei,Tahoma,Helvetica,Arial,"\5B8B\4F53",sans-serif;
  color: white;
}

</style>
