import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '@/components/HelloWorld.vue'
import VideoRating from '@/components/VideoRating.vue'
import VideoPlay from '@/components/VideoPlay.vue'
import Register from '@/components/Register.vue'
import Login from "@/components/Login.vue";
import CommentItem from "@/components/CommentItem.vue";
import Test from "@/components/Test.vue";
import UserCenter from "@/components/UserCenter.vue";
import LoginSuccess from "@/components/LoginSuccess.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HelloWorld
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/PlayVideo',
    name:'PlayVideo',
    component: VideoPlay
  },
  {
    path:'/VideoRating',
    name:'VideoRating',
    component: VideoRating
  },
  {
    path:'/Register',
    name:'Register',
    component: Register
  },
  {
    path:'/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/CommentItem',
    name:'CommentItem',
    component:CommentItem,
  },
  {
    path: '/test',
    name: 'test',
    component: Test,
  },
  {
    path: '/UserCenter',
    name: 'UserCenter',
    component:UserCenter,
  },
  {
    path:'/LoginSuccess',
    name:'LoginSuccess',
    component: LoginSuccess
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// router.beforeEach(async (to, from) => {
//   return true
//   if (to.fullPath === '/UserCenter') {
//     return true
//     let token=localStorage.getItem("8080:userInfo")
//     let flag
//     console.log(token)
//     if(token===undefined){
//       return false
//     }
//     let data={
//       "token":token
//     }
//     console.log("to post...")
//     await axios.post('http://localhost:8087/user/JustCheckLogin',data).then((res) => {
//       console.log('to process post')
//       flag = res.data.response
//     })
//     console.log('to ret,flag:',flag)
//     return flag
//   } else {
//     return true
//   }
// })

export default router
