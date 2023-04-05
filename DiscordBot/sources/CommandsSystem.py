 # -*- coding: Shift-JIS -*-

import sys

from discord.ext import commands
from Checker import Checker
from discord.commands import Option
from CreateContets import CreateContets
from SetupDiscordBot import SetupBot

class System(commands.Cog):
 all_text_ch_id=[str(0)]
 def __init__(self, bot):
  self.bot = bot
  self.creater=CreateContets()
  self.checker=Checker()


 @commands.slash_command(name='z_bot_close', description='終了します。bot作成者以外実行不可')
 async def this_end(self,ctx):
  """終了"""
  if not self.checker.is_admin_id(ctx.author.id):
   dm=await ctx.author.create_dm()
   await dm.send('bot作成者じゃないと実行できないにょーんw')
   return

  print("botは正常に終了しました")
  await ctx.respond('終了します')
  await self.bot.close()
  sys.exit()
  

 @commands.slash_command(name='z_うんこします', description='ぶりっ')
 async def unko_suru(self,ctx):
   """うんこします"""
   await ctx.respond('うんこします', delete_after=0)
   await ctx.send('ぶりっ')
   sent=await ctx.channel.send(str(ctx.guild.get_channel(1082307099398242306)))
   iddd=sent.id
   message_obj=await ctx.channel.fetch_message(iddd)
   await message_obj.delete()
   dm=await ctx.author.create_dm()
   await dm.send('ぶりっ')


 @commands.slash_command(name='z_embed', description='embedを作成')
 async def send_embed(self,ctx,
                      title:Option(str, 'タイトル'),
                      title_url:Option(str, 'タイトルurl'),
                      description:Option(str, '説明'),
                      thumbnail:Option(str, 'サムネ'),
                      ):
   if not self.checker.is_admin_id(ctx.author.id):
    dm=await ctx.author.create_dm()
    await dm.send('bot作成者じゃないと実行できないにょーんw')
    return
   embed= self.creater.set_embed(ctx,title,title_url,description,thumbnail)
   selecter=self.creater.get_text_ch_selecter_view(ctx,embed)
   await ctx.respond("投稿先のテキストチャンネルを選択するため、まずはチャンネルを取得を選択してください",view=selecter)
   

 @commands.Cog.listener('on_message')
 async def on_message(self, message):
  """メッセージに反応"""
  if message.content == 'うんこ':
   await message.channel.send('うんko')
   bot=SetupBot()
   bot=bot.get_bot()
   await message.channel.send(str(bot.get_channel(1082307099398242306)))
