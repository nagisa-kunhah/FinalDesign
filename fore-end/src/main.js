import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueCookie from "vue-cookie";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import 'view-ui-plus/dist/styles/viewuiplus.css'
import 'undraw-ui/dist/style.css'
import axios from "axios";
const app=createApp(App)
app.use(ElementPlus)
app.use(router)

app.config.globalProperties.$cookie=VueCookie
app.config.globalProperties.$axios = axios
app.mount('#app')
