<template>
  <div id="app">
    <router-view></router-view>
  </div>
  <button @click="btn_click">button</button>
  {{this.user_id}}
</template>
<script>
import MyTitle from "@/components/MyHead.vue";
import axios from "axios";
import {ref, onBeforeMount,computed} from 'vue'

export default {
  name:"APP",
  components: {MyTitle},
  data(){
    return {

    }
  },
  async created() {
    await this.set_login()
  },
  setup() {
    const login = ref(false);
    const user_id = ref(null);
    let token = localStorage.getItem("8080:userInfo")
    onBeforeMount(async ()=>{
      if(token==null){
        login.value=false
      }else{
        let data = {
          "token": token,
        }
        await axios.post("http://localhost:8087/user/CheckLogin", data).then((res) => {
          console.log(res.data)
          login.value = (!!res.data.response)
          user_id.value=res.data.user_id
        })
      }
    })
    return {
      login,
      user_id
    }
  },
  provide(){
    return {
      user_id:computed(()=>this.user_id),
      login:computed(()=>this.login)
    }
  },
  methods:{
    btn_click(){
      console.log('11')
      this.user_id=this.user_id-1
      console.log('00')
    },
    async set_login() {
      let ret = localStorage.getItem("8080:userInfo")
      if (ret == null) {
        this.login = false
      } else {
        await this.check_jwt(ret)
      }
    },
    async check_jwt(token) {
      let data = {
        "token": token,
      }
      await axios.post("http://localhost:8087/user/CheckLogin", data).then((res) => {
        console.log(res.data)
        this.login = (!!res.data.response)
        this.user_id=res.data.user_id
      })
    },
  }
}
</script>
