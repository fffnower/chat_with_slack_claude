# chat_with_slack_claude

你需要先做一些设置，

并获取一些参数用来调用slack的api：

---

1. 获取 User OAuth Token
- 进入网址：https://api.slack.com/ --> 点击右上角的【Your apps】 --> 弹出窗口【Create an app】 --> 点击【From scratch】

- 填写app名称以及选择工作空间（例：name: Bot, workspace: chat） --> 点击【Create App】

- 点击左侧边栏上的【OAuth & Permissions】 --> 下拉至【Scopes】卡片 --> 【User Token Scopes】 项下添加权限，如下：

  - channels:history
  - channels:read
chat:write
files:write
groups:history
groups:read
im:history
im:read
im:write
mpim:history
mpim:read
team:read
users:read

- 回到顶部【OAuth Tokens for Your Workspace】栏，点击【Install to Workspace】，然后确认授权即可

- **你的 User OAuth Token：** ![image](https://user-images.githubusercontent.com/32289652/236884379-b06af9c5-913e-4386-8454-286d60c34c57.png)

---

2.频道ID

-网页打开与Claude聊天的界面，此时网址：https://app.slack.com/client/字符串1/字符串2

- **你的 频道ID：** 字符串2

