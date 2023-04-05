import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueCookie from "vue-cookie";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import 'view-ui-plus/dist/styles/viewuiplus.css'

const app=createApp(App);
app.use(ElementPlus)
app.use(router);

app.config.globalProperties.$cookie=VueCookie
app.mount('#app')
