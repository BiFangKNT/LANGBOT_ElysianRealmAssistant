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

配置完成 [QChatGPT](https://github.com/RockChinQ/QChatGPT) 主程序后使用管理员账号向机器人发送命令即可安装：

```
!plugin get https://github.com/BiFangKNT/QChatGPT_ElysianRealmAssistant.git
```
或查看详细的[插件安装说明](https://qchatgpt.rockchin.top/develop/plugin-intro.html#%E6%8F%92%E4%BB%B6%E7%94%A8%E6%B3%95)

## 使用

**效果展示**

![image](https://github.com/user-attachments/assets/8e1329af-c75f-44fa-89d2-16c61dc2125c)
![image](https://github.com/user-attachments/assets/e5edef8e-856b-4cf5-9aca-c12966708877)
![image](https://github.com/user-attachments/assets/0ff56e9f-8b57-4201-b549-639ccbeed87a)
![image](https://github.com/user-attachments/assets/7c1fdb53-1667-407c-8883-f4ef4e6dcb6e)

**角色名部分仅匹配五个字符**

![image](https://github.com/user-attachments/assets/9bc12c87-4ce0-426d-aa75-20c9b125f0ac)


**v1.2更新说明**

提供了以下报错的临时解决方案。此问题是偶发性的，我一开始没问题，后来突然就报错了，查了一下貌似是bot框架本身的权限问题。我测试过用插件可以下载图片，却发不出去，应该不是网络问题。
![image](https://github.com/user-attachments/assets/1e6cbd03-cb9c-4ee0-b249-7d80363cb71a)
![image](https://github.com/user-attachments/assets/978c7dd8-e5b7-4d77-810e-a371ceceed53)



