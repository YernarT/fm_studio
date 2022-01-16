# Django3 + Vue3 全栈项目 (音乐平台)

> 同学的毕业设计作品, 只做了部分功能且代码相对朴素

---

## 运行项目

- 代码克隆到本地: `git clone https://github.com/YernarT/fm_studio.git`

- 安装依赖: 进入项目根目录, 命令行工具输入`pip install -r requirements.txt`

- 运行 Django 端服务器: `python manage.py runserver`, 打开`http://localhost:8000` 即可预览项目

---

## 项目结构

未准备...

---

## 技术栈

### 前端: Vue3

### 后端: Django3

### 数据库: SQLite

---

## 功能

### 音乐播放: 包括播放进度条, 播放动画, 歌曲切换

### 登录注册: 登录, 注册, 修改个人信息

### 歌曲搜索: 通过歌曲名称, 演唱者名字, 歌词模糊查询

---

## 在线演示及项目地址

### 在线演示地址: xxx.html

### github 地址: https://github.com/YernarT/fm_studio

---

## 开发 & 维护 需知

Django 自带的用户表 (table) 仅用于 开发者使用

网站管理员, 这里假设是网站购买者, 持有者以及普通用户的账户信息都在 user 模块里的 User 模型指定的 table 里保存

### 开发 & 生产模式流程:

1. 服务上线
2. migrate Django 自带的 tables
3. makemigration 所有 app 的 models
4. migrate 所有 app 的 models
5. 通过 manage.py create_superuser 创建 admin

   create_superuser 创建的用户保存在 django_auth_user 表中, 再通过 这个用户登录 django-admin 站点

   在自定义的 User 表中创建一个 is_admin 为真的用户作为网站持有者

---

## 项目截图

### 首页

<img src="./result_img/index_page_src.jpeg" alt="index_page_scr" />

### 登录页面

<img src="./result_img/login_page_src.jfif" alt="index_page_scr" />

### 注册页面

<img src="./result_img/register_page_src.jfif" alt="index_page_scr" />
