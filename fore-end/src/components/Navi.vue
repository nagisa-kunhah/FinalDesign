<template>
  <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
  >
    <div class="my-menu-item">
      主站
    </div>
    <div class="grow-user"></div>
    <div class="my-menu-item" @click="to_login">登录</div>
    <div class="my-menu-item" @click="to_register">注册</div>
<!--    <el-menu-item index="3" style="margin-top: 1px">-->
<!--      <el-popover-->
<!--          :width="300"-->
<!--          popper-style="box-shadow: rgb(14 18 22 / 35%) 0px 10px 38px -10px, rgb(14 18 22 / 20%) 0px 10px 20px -15px; padding: 20px;"-->
<!--      >-->
<!--        <template #reference>-->
<!--          <el-avatar>-->
<!--            <img :src=img alt="">-->
<!--          </el-avatar>-->
<!--        </template>-->
<!--        <template #default>-->
<!--          <div-->
<!--              class="demo-rich-conent"-->
<!--              style="display: flex; gap: 16px; flex-direction: column"-->
<!--          >-->
<!--            <el-avatar-->
<!--                :size="60"-->
<!--                :src=img-->
<!--                style="margin-bottom: 8px"-->
<!--            />-->
<!--            <div>-->
<!--              <p-->
<!--                  class="demo-rich-content__name"-->
<!--                  style="margin: 0; font-weight: 500"-->
<!--              >-->
<!--                Element Plus-->
<!--              </p>-->
<!--              <p-->
<!--                  class="demo-rich-content__mention"-->
<!--                  style="margin: 0; font-size: 14px; color: var(&#45;&#45;el-color-info)"-->
<!--              >-->
<!--                @element-plus-->
<!--              </p>-->
<!--            </div>-->

<!--            <p class="demo-rich-content__desc" style="margin: 0">-->
<!--              Element Plus, a Vue 3 based component library for developers,-->
<!--              designers and product managers-->
<!--            </p>-->
<!--          </div>-->
<!--        </template>-->
<!--      </el-popover>-->
<!--    </el-menu-item>-->
  </el-menu>
</template>

<script>
export default {
  name: "Navi",
  data(){
    return{
      activeIndex:'1',
      img:require('@/assets/logo.png'),
    }
  },
  computed:{

  },
  methods:{
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
  height: 50px;
}
</style>