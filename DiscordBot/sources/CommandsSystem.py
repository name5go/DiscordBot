 # -*- coding: Shift-JIS -*-

import sys

from discord.ext import commands
from Checker import Checker

from CommandsPhotoReply import PhotoReply

class System(commands.Cog):
 def __init__(self, bot):
  self.bot = bot 

 def clear_lists(self):
  PhotoReply.clear_pic_list()

 @commands.slash_command(name='うんこします', description='ぶりっ')
 async def unko_suru(self,ctx):
   """うんこします"""
   await ctx.respond('うんこします')
   await ctx.send('ぶりっ')

 @commands.slash_command(name='熙_bot_close', description='終了します。bot作成者以外実行不可')
 async def this_end(self,ctx):
  """終了"""
  if Checker.is_admin_id(ctx.author.id):
   print("botは正常に終了しました")
   self.clear_lists()
   await ctx.respond('終了します')
   await self.bot.close()
   sys.exit()
  await ctx.respond('bot作成者じゃないと実行できないにょーんw')
   
 @commands.Cog.listener('on_message')
 async def on_message(self, message):
  """メッセージに反応"""
  if message.content == 'うんこ':
   await message.channel.send('うんko')
