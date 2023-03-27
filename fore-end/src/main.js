import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueCookie from "vue-cookie";

const app=createApp(App);
app.use(router);
app.config.globalProperties.$cookie=VueCookie
app.mount('#app')
