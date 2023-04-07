<template>
  <div class="common-layout">
    <div class="aside">aside</div>
    <div class="right">
      <div class="title"><h4>{{info.CommentId}}</h4></div>
      <div class="comment">{{info.Comment}}</div>
      <div class="info">{{info.CommitTime}}</div>
    </div>
  </div>
</template>

<script>
export default {
  props:{
    info:null
  },
  name: "CommentItem"
}
</script>

<style scoped>
.common-layout{
  display: flex;
  align-items: center;
  justify-content: left;
  height: 100px;
  width: 100%;
  background-color: rgba(0,255,255,30%);
}
.aside{
  width: 10%;
}
.title{
  display: flex;
  align-items: center;
  justify-content: left;
  height: 30px;
}
.info{
  display: flex;
  align-items: center;
  justify-content: left;
  height: 30px;
}
.comment{
  display: flex;
  justify-content: left;
  flex-wrap: wrap;
}
.comment{
  display: flex;
  align-items: center;
  justify-content: left;
}
</style>