const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    proxy:{
      '/api':{                     //这个就是的标识，当接口用 localhost 开头才用代理
        target:'http://localhost:9191',       //这是代理到哪里
        pathRewrite: {
          '^/api': ''
        },
        ws:true,
        changeOrigin:true                //开启代理：在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
      }
    }
  }
})
