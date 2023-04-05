 # -*- coding: Shift-JIS -*-

#文字列チェック
import re

name5go_id=377632130718498826

class Checker():
 """チェック系の関数まとめ"""
 def is_admin_id(self,id):
  return id==name5go_id

 def is_url_string(self,url):
  """文字列がurlの書式かどうか調べる"""
  pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
  return re.match (pattern, url)

 #文字列がサーバー辞書に登録されているか
 def is_pic_list_word(self,server_pic_list,server_id,word):
  return word in server_pic_list[server_id]



 def is_joined_user(self,ctx):
  """コマンド実行者がボイスチャンネルに入っていなければtrueを返す"""
  return ctx.author.voice is None

 def is_joined_bot(self,ctx):
  """BOTがボイスチャンネルに加入しているか調べる"""
  return ctx.guild.voice_client is None


 #どこのurlか調べる
 def where_url(self,url):
    youtube="youtube"
    no="not applied"
    if re.match(youtube, url):
        return youtube
    return no


