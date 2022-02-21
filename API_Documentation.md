# API Documentation

# 登录账号

## POST `api/user/login/`

### 请求数据

| 字段名     | 描述     | 类型     | 必填   |
| ---------- | -------- | -------- | ------ |
| `phone`    | 电话号码 | `string` | `True` |
| `password` | 密码     | `string` | `True` |

### 成功的返回

状态码: `200`

```json
{
	"message": "авторизация сәтті болды",
	"token": "9YinnBAA8Bea6IZ5TkQ=*K5lmi52szS+rnPd9jR/7IQ==*tzHkWCBMMweEr/NVP7h3iA==*JRVz6Uu+9VU4y3Vo9BBJow==",
	"user": {
		"id": 8,
		"username": "user_2022011701",
		"phone": "87714526550",
		"is_admin": false,
		"birthday": null,
		"gender": false,
		"avatar": "http://127.0.0.1:8000/media/img/user/avatar/default-avatar.png",
		"create_time": "2022-01-16T19:09:30.413Z"
	}
}
```

### 失败的返回

状态码: `400`

```json
{
	"message": "авторизация сәтсіз болды"
}
```

---

# 注册账号

## POST `api/user/register/`

### 请求数据

| 字段名     | 描述             | 类型     | 必填    |
| ---------- | ---------------- | -------- | ------- |
| `phone`    | 电话号码         | `string` | `True`  |
| `password` | 密码             | `string` | `True`  |
| `is_admin` | 是否是管理员账号 | `bool`   | `False` |

### 成功的返回

状态码: `201`

```json
{
	"message": "тіркелу сәтті болды",
	"token": "ldJOVAVl8+Mwl3iuswM=*kQRk+M8rJ2YkAYhZ6DG/zg==*vTfnrKPr1w3vYo16dF8ROA==*nHD5geXcCeKB7DtfzIL/jw==",
	"user": {
		"id": 8,
		"username": "user_2022011701",
		"phone": "87714526550",
		"is_admin": false,
		"birthday": null,
		"gender": 0,
		"avatar": "http://127.0.0.1:8000/media/img/user/avatar/default-avatar.png",
		"create_time": "2022-01-16T19:09:30.413Z"
	}
}
```

### 失败的返回

状态码: `400`

```json
{
	"message": "телефон нөмер тіркелген"
}
```

---

# 编辑用户信息

## PUT `api/user/edit/`

### 请求数据

| 字段名     | 描述     | 类型     | 必填    |
| ---------- | -------- | -------- | ------- |
| `username` | 用户名   | `string` | `False` |
| `phone`    | 电话号码 | `string` | `False` |
| `password` | 密码     | `string` | `False` |
| `birthday` | 生日     | `string` | `False` |
| `gender`   | 性别     | `bool`   | `False` |

### 成功的返回

状态码: `200`

```json
{
	"message": "өзгерту сәтті болд",
	"user": {
		"username": "user_2022020121",
		"phone": "87714526555",
		"is_admin": false,
		"birthday": "2001-05-19",
		"gender": true,
		"avatar": "http://127.0.0.1:8000/media/img/user/avatar/default-avatar.png",
		"create_time": "2022-02-01 16:47:52"
	}
}
```

### 失败的返回

状态码: `400`

```json
{
	"message": "телефон нөмер тіркелген"
}
```

---

# 更新用户头像

## POST `api/user/edit/avatar/`

### 请求数据

| 字段名   | 描述 | 类型       | 必填   |
| -------- | ---- | ---------- | ------ |
| `avatar` | 头像 | `FormData` | `True` |

### 成功的返回

状态码: `201`

```json
{
	"message": "өзгерту сәтті болд",
	"user": {
		"username": "user_2022020121",
		"phone": "87714526555",
		"is_admin": false,
		"birthday": "2001-05-19",
		"gender": true,
		"avatar": "http://127.0.0.1:8000/media/img/user/avatar/new_avatar.png",
		"create_time": "2022-02-01 16:47:52"
	}
}
```

### 失败的返回

状态码: `400`

```json
{
	"message": "сурет пішімі 60kb-дан артық болмау керек"
}
```

---

# 获取所有音乐类型

## GET `api/music/type/`

### 成功的返回

状态码: `200`

```json
{
	"message": "барлық жанрлар",
	"music_types": [
		{
			"id": 1,
			"name": "hip-hop"
		},
		{
			"id": 2,
			"name": "rock"
		},
		{
			"id": 3,
			"name": "ballad"
		},
		{
			"id": 4,
			"name": "classic"
		}
	]
}
```

---

# 创建音乐类型

## POST `api/music/type/`

### 请求数据

| 字段名 | 描述     | 类型     | 必填   |
| ------ | -------- | -------- | ------ |
| `name` | 类型名称 | `string` | `True` |

### 成功的返回

状态码: `201`

```json
{
	"message": "музыка жаныры сәтті құрылды",
	"music": {
		"id": 5,
		"name": "jazz"
	}
}
```

### 失败的返回

状态码: `400`

```json
{
	"message": "жаныр атауы болу керек"
}
```

---
