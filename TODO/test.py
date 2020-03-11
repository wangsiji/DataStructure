# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 6:22 下午
# @Author  : siJi
# @File    : test.py
# @Desc    :

import sys
import re

a = []
b = []
lines = ["abc", "___"]
for line in sys.stdin:
    line = line.strip()
    if re.match(r'^[a-zA-Z0-9]+', line):

        a.append(line)
    else:
        b.append(line)

    print(" ".join(a))
    print(" ".join(b))

#     # 读取每一行
#     line = sys.stdin.readline().strip()
# #for line in lines.strip().split("???"):
#     line = line.strip().split("|")
#     info = re.findall(r'^\[.*?\]', line[-1].strip())[0]
#
#     if info in ["[ENTER]", "[EXIT]"]:
#         # 时间
#         t = re.split(r'\s+', line[0].strip().split(",")[0])[1]
#         h, m, s = t.strip().split(":")
#         s = int(h) * 3600 + int(m) * 60 + int(s)
#         ms = line[0].strip().split(",")[1].strip()
#         stamp = s * 1000 + int(ms)
#         # 类名
#         className = line[3].strip()
#         # 方法名
#         method = line[4].strip()
#         if className not in lookup:
#             # 1
#             lookup[className] = {}
#             # 2
#             lookup[className][method] = {}
#             lookup[className][method][info] = stamp
#         else:
#             if method not in lookup[className]:
#                 lookup[className][method] = {}
#                 lookup[className][method][info] = stamp
#             else:
#                 lookup[className][method][info] = stamp
#
# for className in lookup:
#     print(className+":")
#     for method in lookup[className]:
#         diff = int(lookup[className][method]['[EXIT]']) - int(lookup[className][method]['[ENTER]'])
#         lookup[className][method]["diff"] = diff
#         print(method+","+str(diff))
