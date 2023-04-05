# -*- coding: Shift-JIS -*-

from discord.ext import commands
from discord.commands import Option

from distutils.util import strtobool

class PhotoReply(commands.Cog):
 def __init__(self, bot):
  self.bot = bot
  self.server_pic_list={}
  

 def get_pic_list(self):
  return self.server_pic_list


 def del_server_id(self,s_id):
  del self.server_pic_list[s_id]


 def is_list_server_id(self,server_id):
  """サーバーIDがdic_listに登録されているか調べる"""
  return server_id in self.server_pic_list


 @commands.slash_command(name='a_画像返信機能を有効', description='画像返信機能をtrueで有効。falseで辞書一時保存データ削除')
 async def dic_server_st(self,ctx,
                         status:Option(str, 'trueで有効、falseでこのサーバーの登録情報をすべて消し無効にする', choices=['true', 'false'])
                         ):
  """このbotの画像返信機能をサーバーで有効にする"""
  server_id = ctx.guild.id
  server_name = ctx.guild.name
  #bool result =サーバーIDが連想配列に登録されているか調べる
  result =self.is_list_server_id(server_id)
  status_bool=bool(strtobool(status))
  
  if status_bool:
   if result:
    await ctx.respond('サーバー名['+str(server_name)+']でこのbotはすでに有効です')
    return
   await ctx.respond('サーバー名['+str(server_name)+']でこのbotを有効にします')
   await ctx.send('辞書型「サーバーID['+str(server_id)+']」オブジェクトを[server_list]に作成しました')
   self.server_pic_list[server_id]={}
  if  not status_bool:
   if not result:
    await ctx.respond('サーバー名['+str(server_name)+']では既にこのbotは無効です')
    return
   await ctx.respond('サーバー名['+str(server_name)+']でこのbotを無効にします')
   await ctx.send('辞書型「サーバーID['+str(server_id)+']」を削除しました')
   self.del_server_id(server_id)


#@commands.slash_command(name='a_画像返信機能を有効', description='画像返信機能をtrueで有効。falseで辞書一時保存データ削除')
