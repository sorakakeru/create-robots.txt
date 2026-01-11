#!/usr/bin/env python
# coding: utf-8

import json
import os
from config import config

#ai.robots.txtのjsonデータからrobots.txt用データを生成する
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
robots_json_path = os.path.join(BASE_DIR, "robots.json")
with open(robots_json_path, "r") as f:
  json_load = json.load(f)

aibots_list_txt = """
## 以下AIbotのリストは、以下のMITライセンスライブラリを使用しています。
# ai.robots.txt
# https://github.com/ai-robots-txt/ai.robots.txt
# Copyright (c) 2024 ai.robots.txt
# Released under the MIT license
# https://github.com/ai-robots-txt/ai.robots.txt/blob/main/LICENSE

"""
for key, value in json_load.items():
  aibot_txt = f"User-agent: {key}\nDisallow: /\n\n"
  aibots_list_txt += aibot_txt

#Googlebot-Image botの`Disallow`設定
google_imagebot_txt = "User-agent: Googlebot-Image\nDisallow: /\n"

#指定サイトごとに独自ルールを追加してrobots.txtを生成する
for key, value in config.items():
  if isinstance(value, list):
    site_list_txt = ""
    site_list_txt += "User-agent: *\n"
    for idx, item in enumerate(value):
      if idx == len(value) - 1:
        #最後のループのみ
        site_txt = f"Disallow: {item}\n\n"
      else:
        site_txt = f"Disallow: {item}\n"
      site_list_txt += site_txt

    #ディレクトリが存在しなければ生成
    site_dir = os.path.join(BASE_DIR, f"dist/{key}")
    if not os.path.isdir(site_dir):
      os.makedirs(site_dir)

    #ファイル書き込み
    try:
      with open(os.path.join(site_dir, "robots.txt"), 'w') as f:
        f.write(site_list_txt + google_imagebot_txt + aibots_list_txt)
    except Exception as e:
        print(f"Error writing robots.txt for {key}: {e}")
# 

