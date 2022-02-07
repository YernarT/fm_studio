# fm_studio 项目前端部分

## API

使用的是 `axios` 请求库, `src/api/ajax.ts` 文件封装了 axios, 添加了请求拦截和响应拦截。

请求拦截器负责在请求头添加 X-AUTH-TOKEN, 值从 localStorage 里获取。

## 全局状态管理

使用 `Vue3` 内置的 `inject, provide` 函数实现, 初始化默认值从 `LocalStorage`获取, 通过在 `App.vue` 中向 `windows` 对象绑定一个 `onBeforeUnload` 监听事件, 在每次刷新页面时将全局数据保存进 `LocalStorage`, 确保下次初始化的值是理想的。
