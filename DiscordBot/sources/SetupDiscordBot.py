 # -*- coding: Shift-JIS -*-

#discord_botセットアップ

#discord用
import discord
#環境変数取得用
import os
TOKEN_D=os.environ.get('DISCORD_TOKEN')

class SetupBot():
 def __init__(self):
  self.intents = discord.Intents.default()
  self.intents.message_content = True
  self.bot=discord.Bot(intents=self.intents)
  self.cog_list=[]
 
 def get_bot(self):
  return self.bot

 def add(self,com_class):
   """コマンドクラスを追加"""
   self.cog_list.append(com_class)

 def run_bot(self):
  """cog_listの中身をdiscord側に登録して起動"""
  for cogs in self.cog_list:
   self.bot.add_cog(cogs(self.bot))
  self.cog_list.clear()
  self.bot.run(TOKEN_D)
