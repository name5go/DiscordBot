# -*- coding: Shift-JIS -*-

from discord.ext import commands
from discord.commands import Option
import openai

#環境変数取得用
import os

class ChatAI(commands.Cog):
 def __init__(self, bot):
  self.bot = bot
  self.openai.api_key=os.environ.get('OPENAI_TOKEN')
  self.messages_history=[{
                   "role": "system",
                   "content": "「ずんだもん」という名前の可愛い女の子のキャラクターがいる。そのキャラは語尾が「なのだ」、一人称は「ぼく」が特徴のキャラクターだ。自己紹介は不要です。この文以降の返信をしてほしい、だが前述のキャラクターになりきって返信して。"
                    },],
 @commands.slash_command(name='a_aiと会話', description='AIと会話。限界はわからん')
 async def talk_ai(self,ctx,
                   message:Option(str, 'メッセージ')
                   ):
  self.messages_history.apeend({"role":"user","content":message})
  response = openai.ChatCompletion.create(
                                           model="gpt-3.5-turbo",
                                           messsages=self.messages_history,
                                           )
  #await ctx.respond(message+'サーバー名します')
  reply=str(response[0]["message"]["content"].strip())
  self.messages_history.apeend({"role":"assistant","content":reply})
  await ctx.respond(reply)