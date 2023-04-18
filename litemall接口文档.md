## Python接口自动化

### Litemall商城常用地址

- 商城管理后台地址：http://litemall.hogwarts.ceshiren.com/
- 商城客户端地址：http://litemall.hogwarts.ceshiren.com/vue/index.html
- 接口swagger文档地址：http://litemall.hogwarts.ceshiren.com/swagger-ui.html

### Litemall商城常用接口

1. 管理后台登录接口

- 类型：POST
- 地址："http://litemall.hogwarts.ceshiren.com/admin/auth/login"

- 请求示例：

```json
{
  "username": "admin123",
  "password": "admin123",
  "code": ""
}
```

- 响应示例：

```json
{
  "errno": 0,
  "data": {
    "adminInfo": {
      "nickName": "admin123",
      "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
    },
    "token": "a362f0e0-e07c-420e-b79c-40754bd9a021"
  },
  "errmsg": "成功"
}
```

2. 商品上架接口

- 类型：POST
- 地址："http://litemall.hogwarts.ceshiren.com/admin/goods/create"
- 请求示例：

```json
{
  "goods": {
    "picUrl": "https://ceshiren.com/uploads/default/original/1X/809c63f904a37bc0c6f029bbaf4903c27f03ea8a.png",
    "gallery": [],
    "isHot": true,
    "isNew": true,
    "isOnSale": true,
    "goodsSn": "123124215412",
    "name": "hogwarts",
    "counterPrice": "88"
  },
  "specifications": [
    {
      "specification": "自动化测试",
      "value": "接口自动化",
      "picUrl": ""
    }
  ],
  "products": [
    {
      "id": 0,
      "specifications": [
        "接口自动化"
      ],
      "price": 66,
      "number": 3,
      "url": ""
    }
  ],
  "attributes": [
    {
      "attribute": "测试",
      "value": "接口"
    }
  ]
}
```

- 响应示例：

```json
{
  "errno": 0,
  "errmsg": "成功"
}
```

3. 商品列表接口（可以提取商品ID）

- 类型：GET
- 地址："http://litemall.hogwarts.ceshiren.com/admin/goods/list"
- 请求示例：

```json
{
  "name": "hogwarts",
  "order": "desc",
  "sort": "add_time"
}
```

- 响应示例：

```json
{
  "errno": 0,
  "data": {
    "total": 1,
    "pages": 1,
    "limit": 10,
    "page": 1,
    "list": [
      {
        "id": 1181668,
        "goodsSn": "123124215412",
        "name": "hogwarts",
        "categoryId": 0,
        "brandId": 0,
        "gallery": [],
        "keywords": "",
        "brief": "",
        "isOnSale": true,
        "sortOrder": 100,
        "picUrl": "https://ceshiren.com/uploads/default/original/1X/809c63f904a37bc0c6f029bbaf4903c27f03ea8a.png",
        "isNew": true,
        "isHot": true,
        "unit": "’件‘",
        "counterPrice": 88.0,
        "retailPrice": 66.0,
        "addTim": "2022-06-10 11:51:53",
        "updateTime": "2022-06-10 11:51:53",
        "deleted": false
      }
    ]
  },
  "errmsg": "成功"
}
```

4. 商品详情接口（可以提取商品库存ID）

- 类型：GET
- 地址："http://litemall.hogwarts.ceshiren.com/admin/goods/detail"
- 请求示例：

```json
{
  "id": 1181668
}
```

- 响应示例：

```json
{
  "errno": 0,
  "data": {
    "categoryIds": [],
    "goods": {
      "id": 1181668,
      "goodsSn": "123124215412",
      "name": "hogwarts",
      "categoryId": 0,
      "brandId": 0,
      "gallery": [],
      "keywords": "",
      "brief": "",
      "isOnSale": true,
      "sortOrder": 100,
      "picUrl": "https://ceshiren.com/uploads/default/original/1X/809c63f904a37bc0c6f029bbaf4903c27f03ea8a.png",
      "isNew": true,
      "isHot": true,
      "unit": "’件‘",
      "counterPrice": 88.00,
      "retailPrice": 66.00,
      "addTime": "2022-06-10 11:51:53",
      "updateTime": "2022-06-10 11:51:53",
      "deleted": false
    },
    "attributes": [
      {
        "id": 1186,
        "goodsId": 1181668,
        "attribute": "测试",
        "value": "接口",
        "addTime": "2022-06-10 11:51:53",
        "updateTime": "2022-06-10 11:51:53",
        "deleted": false
      }
    ],
    "specifications": [
      {
        "id": 916,
        "goodsId": 1181668,
        "specification": "自动化测试",
        "value": "接口自动化",
        "picUrl": "",
        "addTime": "2022-06-10 11:51:53",
        "updateTime": "2022-06-10 11:51:53",
        "deleted": false
      }
    ],
    "products": [
      {
        "id": 915,
        "goodsId": 1181668,
        "specifications": [
          "接口自动化"
        ],
        "price": 66.00,
        "number": 3,
        "url": "",
        "addTime": "2022-06-10 11:51:53",
        "updateTime": "2022-06-10 11:51:53",
        "deleted": false
      }
    ]
  },
  "errmsg": "成功"
}
```

5. 用户登录接口

- 类型：POST
- 地址："http://litemall.hogwarts.ceshiren.com/wx/auth/login"
- 请求示例：

```json
{
  "username": "user123",
  "password": "user123"
}
```

- 响应示例：

```json
{
  "errno": 0,
  "data": {
    "userInfo": {
      "nickName": "user123",
      "avatarUrl": ""
    },
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0aGlzIGlzIGxpdGVtYWxsIHRva2VuIiwiYXVkIjoiTUlOSUFQUCIsImlzcyI6IkxJVEVNQUxMIiwiZXhwIjoxNjU0ODQ3OTA1LCJ1c2VySWQiOjEsImlhdCI6MTY1NDg0MDcwNX0.JrF6RNSnUenus85oGCZ5IRWxuLneKHBJdcJRE9TVK8s"
  },
  "errmsg": "成功"
}

```

6. 加入购物车接口

类型：POST 地址："http://litemall.hogwarts.ceshiren.com/wx/cart/add"

- 请求示例：

```json
{
  "goodsId": 1181668,
  "number": 2,
  "productId": 915
}
```

- 响应示例：

```json
{
  "errno": 0,
  "data": 5,
  "errmsg": "成功"
}
```

7. 删除商品接口

类型：POST 地址："http://litemall.hogwarts.ceshiren.com/admin/goods/delete"

- 请求示例：

```json
{
  "id": 1181677,
}
```

- 响应示例：

```json
{
  "errno": 0,
  "errmsg": "成功"
}
```