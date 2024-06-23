# yt-dlp 下载 youtube 视频
# 流程：默认下载视频，可输入 q 选择其他格式

import os

mp4 = '-f "bv[ext=mp4]+ba[ext=m4a]"'
m4a = "-f140"
format = mp4

def select_format():
    choice = input("视频(1)，音频(2): ")
    match choice:
        case 1:
            format = mp4
        case 2:
            format = m4a

link = input("输入链接（q 选择其他格式）：")
while link == 'q':
    select_format()
    link = input("输入链接（q 选择其他格式）：")

os.system(f"yt-dlp {format} {link}")