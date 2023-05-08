# chat_with_slack_claude

获得个人Claude频道ID的方法


ClaudeID
网页打开与Claude聊天的界面，此时网址如下：
https://app.slack.com/client/字符串1/字符串2
您需要记下：字符串2
1. 获取 User OAuth Token
> 进入网址：https://api.slack.com/ --> 点击右上角的Your apps --> 弹出窗口【Create an app】 --> 点击【From scratch】
> 填写app名称以及选择工作空间（例：name: Bot, workspace: chat） --> 点击【Create App】
> 点击左侧边栏上的【OAuth & Permissions】 〉》 下拉至【Scopes】卡片，在 【User Token Scopes】 项下添加权限，如下：
```
channels:history
channels:read
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
```
> 回到顶部【OAuth Tokens for Your Workspace】栏，点击【Install to Workspace】，然后确认授权即可

你的 User OAuth Token：
![image](https://user-images.githubusercontent.com/32289652/236881898-383112da-0078-464d-899a-70a7a5d11923.png)


获得个人User OAuth Token的方法

1. 进入这个网址：https://api.slack.com/
2. 点击右上角的Your apps
3. 点击 Create an App，选择第二个From an app manifest
4. 选择自己工作区，然后下一步的配置我选择的默认(这一步也许很重要，但不会影响到我想实现的功能，或许想要实现更复杂功能的时候要改这个配置)

5. 创建成功后会进入下面这个页面，继续往下滚动会看到Bots这个选项，看到之后点击进入





6. 然后点击下面这个绿色按钮Review Scopes to Add




7. 进入下面这个页面后找到Scopes下面的User Token Scopes




8. 点击User Token Scopes下面的Add an OAuth Scope给用户添加权限。要添加的权限如下：

channels:history
channels:read
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

（一共13种，我是参考官方claude的权限设置的，有些权限也许添加也没什么用）




9. 添加完用户权限之后，点击当前页面OAuth Tokens for Your Workspace下面的Install to workspace，点击允许之后会出现下面这个页面。然后就得到了自己的User OAuth Token




写在后面：我只研究了slack的一小部分，它的功能还有很多很多，也许还有比这种方式更方便的方式，欢迎大家来交流slack的用法。 作者：深海与鲸LI https://www.bilibili.com/read/cv23452942#reply164158352160 出处：bilibili
