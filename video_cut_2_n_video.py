# 1 video -> n video
# 从一个视频截取多个片段
#
# 需要：ffmpeg
# 接收参数：
#   - 1个视频地址
#   - 多组片段信息
#     ，格式：<开始时间><结束时间><名字>
#     ，如"4:37 8:29 古伤"

# 流程
# 1. 输入视频地址
# 2. 输入片段信息

import threading
import os
# from posixpath import split

def cut(name, start_time, end_time, video, extension_name):
    cmd = "ffmpeg -ss %s -to %s -y -accurate_seek -i %s -c copy -avoid_negative_ts 1 %s.%s" \
          %(start_time, end_time, video, name, extension_name)
    os.system(cmd)

video = input("输入视频地址(可拖动文件到此):")
extension_name = video.replace("'", "").split(".")[-1]

while(True):
    snippet = input("输入<开始时间><结束时间><名字>:")
    start_time, end_time, name = snippet.split()
    threading.Thread(target=cut, args=(name, start_time, end_time, video, extension_name,)).start()
