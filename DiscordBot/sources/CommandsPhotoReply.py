# -*- coding: Shift-JIS -*-

from discord.ext import commands
from discord.commands import Option

class PhotoReply(commands.Cog):
 def __init__(self, bot):
  self.bot = bot
  self.server_pic_list={}

 def get_pic_list(self):
  return self.server_pic_list

 def clear_pic_list(self):
  self.server_pic_list.clear()

 def is_list_server_id(self,server_id):
  """サーバーIDがdic_listに登録されているか調べる"""
  return server_id in self.server_pic_list

 @commands.slash_command(name='画像返信機能を有効', description='画像返信機能を有効')
 async def dic_server_st(ctx,
                     server_st:Option(str, 'trueで有効、falseでこのサーバーの登録情報をすべて消し無効にする', choices=['true', 'false']),
                     self
                     ):
  """このbotの画像返信機能をサーバーで有効にする"""
  server_id = ctx.guild.id
  server_name = ctx.guild.name
  #bool result =サーバーIDが連想配列に登録されているか調べる
  result =self.is_list_server_id(server_id)



