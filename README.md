# ElysianRealmAssistant

<!--
## 插件开发者详阅

### 开始

此仓库是 QChatGPT 插件模板，您可以直接在 GitHub 仓库中点击右上角的 "Use this template" 以创建你的插件。  
接下来按照以下步骤修改模板代码：

#### 修改模板代码

- 修改此文档顶部插件名称信息
- 将此文档下方的`<插件发布仓库地址>`改为你的插件在 GitHub· 上的地址
- 补充下方的`使用`章节内容
- 修改`main.py`中的`@register`中的插件 名称、描述、版本、作者 等信息
- 修改`main.py`中的`MyPlugin`类名为你的插件类名
- 将插件所需依赖库写到`requirements.txt`中
- 根据[插件开发教程](https://qchatgpt.rockchin.top/develop/plugin-dev.html)编写插件代码
- 删除 README.md 中的注释内容


#### 发布插件

推荐将插件上传到 GitHub 代码仓库，以便用户通过下方方式安装。   
欢迎[提issue](https://github.com/RockChinQ/QChatGPT/issues/new?assignees=&labels=%E7%8B%AC%E7%AB%8B%E6%8F%92%E4%BB%B6&projects=&template=submit-plugin.yml&title=%5BPlugin%5D%3A+%E8%AF%B7%E6%B1%82%E7%99%BB%E8%AE%B0%E6%96%B0%E6%8F%92%E4%BB%B6)，将您的插件提交到[插件列表](https://github.com/stars/RockChinQ/lists/qchatgpt-%E6%8F%92%E4%BB%B6)

下方是给用户看的内容，按需修改
-->

## 安装

参照详细的[插件安装说明](https://docs.langbot.app/zh/plugin/plugin-intro.html#%E5%AE%89%E8%A3%85)

## 使用

**`乐土推荐`指令**

依照推荐度排序，支持添加序号请求

![image](https://github.com/user-attachments/assets/9c30491c-8ad7-4aed-acfe-8ef29dab8dde)

![image](https://github.com/user-attachments/assets/ea3ef8ea-ae9c-44c8-874b-117cc2707bef)

**攻略搜索指令**

![image](https://github.com/user-attachments/assets/4fea1c40-a954-4be9-baf0-6d37173dc68c)

**`乐土list`指令**

可查询相关关键词的列表，支持模糊匹配，输入`乐土list`可查询全文

![image](https://github.com/user-attachments/assets/980d35a1-cf88-498a-bdae-1b88d356e894)

**异常处理**

![image](https://github.com/user-attachments/assets/96a3dc7b-9696-4fd0-bad0-fa46928a1a73)

![image](https://github.com/user-attachments/assets/90aacfd5-f46a-45b2-aa6c-28289435623c)


**角色名部分仅匹配五个字符**

![image](https://github.com/user-attachments/assets/9bc12c87-4ce0-426d-aa75-20c9b125f0ac)


**v1.2更新说明**

提供了以下报错的临时解决方案。此问题是偶发性的，我一开始没问题，后来突然就报错了，查了一下貌似是bot框架本身的权限问题。我测试过用插件可以下载图片，却发不出去，应该不是网络问题。
![image](https://github.com/user-attachments/assets/1e6cbd03-cb9c-4ee0-b249-7d80363cb71a)
![image](https://github.com/user-attachments/assets/978c7dd8-e5b7-4d77-810e-a371ceceed53)


**v1.5更新说明**

米游社图片获取部分，不知道是不是个例，dns解析耗时过长，因此加入缓存机制；单次缓存中采用单session复用方案，加快缓存速度。
