import time
from slack import WebClient
from slack.errors import SlackApiError

# User OAuth Token
userOAuthToken = 'xoxp-5152878191811-5176692665200-5222232003411-c43a8e0715b41247deb60740ddbbd460'
# 频道ID
channel_id = 'D054VJKSSD7'
# 连接slack
client = WebClient(token=userOAuthToken)

print("""\

***************************************************
    你好! 此程序使用slack的api实现与claude对话;
    两次回车换行进行交互, 请您开始吧!
***************************************************\

    """)

def get_new_msg():
    new_msg = client.conversations_history(channel=channel_id, oldest=last_message_timestamp)
    # 违规警告
    # \n&gt; _*Please note:* This request may violate our Acceptable Use Policy._\n&gt; _See the <https://console.anthropic.com/docs|Claude documentation> for more information._'''
    idx = len(new_msg['messages']) - 1
    return new_msg['messages'][idx]['text']

def get_user_input():
    global flag
    print('You:')
    lines = []
    # 空输入不执行
    while not lines:
        # 两次回车尝试输入
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
    return "\n".join(lines)

def get_print_new_msg(message):
    global last_message_timestamp
    print('Claude:')

    # 发送到指定频道，更新时间戳
    try:
        response = client.chat_postMessage(channel=channel_id, text=message, as_user=True)
    except SlackApiError as e:
        print(f"Error sending message: {e}")
    last_message_timestamp = response['ts']

    # 时间更新，避免与时间戳相同
    time.sleep(1)
    
    # 捕获最新的回答
    # 更新回答时间间隔
    time_step = 0.5
    len_new_msg = 1
    while True:
        # 更新答案
        new_msg = get_new_msg()
        # 未回复
        if new_msg == '_Typing…_': 
            time.sleep(time_step)
            continue
        # 开始回复
        if new_msg.endswith('Typing…_'):
            print(new_msg[len_new_msg:-11], end='')
            len_new_msg = len(new_msg)-11
            time.sleep(time_step)
        else:
            print(new_msg[len_new_msg:],end = '[END]\n\n')
            break
    return new_msg[1:]

last_message_timestamp = None
# 主程序
def chat():
    while True:
        # 获取输入
        message = get_user_input()
        # 获取、打印回答
        new_msg = get_print_new_msg(message)

# 运行
if __name__ == '__main__':
    chat()
