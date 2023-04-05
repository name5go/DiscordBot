# -*- coding: Shift-JIS -*-

from unittest import expectedFailure
from discord.ext import commands
from discord.commands import Option
import openai
import asyncio

#環境変数取得用
import os
openai.api_key=os.environ.get('OPENAI_TOKEN')


class ChatAI(commands.Cog):
 def __init__(self, bot):
  self.bot = bot  
  self.prompt = "「ずんだもん」という名前の可愛い女の子のキャラクターがいる。そのキャラは語尾が「なのだ」、一人称は「ぼく」が特徴のキャラクターだ。自己紹介は不要です。この文以降の返信をしてほしい、だが前述のキャラクターになりきって返信して。"
  self.temperature = 0.5
  self.engine="text-davinci-002"
  self.messages_history=[]
  obj={
       "role": "system",
       "content": self.prompt
       } 
  self.add_messages_history(obj)


 def add_messages_history(self,add_obj):
  tuple_list=list(self.messages_history)
  tuple_list.append(add_obj)
  self.messages_history=tuple(tuple_list)
  return

 @commands.slash_command(name='a_aiずんだもんの設定', description='術式の開示という縛りで呪力の強化を行うわけか...肝心の術式が弱すぎる!?')
 async def ai_settei(self):
  await self.ctx.respond("ジージー...ッガガガ...通信中なのだ...")

 @commands.slash_command(name='a_aiずんだもんと会話', description='AIと会話。限界はわからん')
 async def talk_ai(self,ctx,
                   message:Option(str, 'メッセージ')
                   ):
  await ctx.respond(self.prompt)
  try:
   await asyncio.wait_for(self.reply(ctx,message), timeout=10)
  except asyncio.TimeoutError:
   await ctx.respond("Command timed out!")


 async def reply(self,ctx,message):
  obj={"role":"user","content":message}
  self.add_messages_history(obj)
  response = openai.ChatCompletion.create(
                                      model="gpt-3.5-turbo",
                                      messages=self.messages_history
                                      )
  #await ctx.respond(message+'サーバー名します')
  reply=str(response['choices'][0]['message']['content'])
  obj={"role":"assistant","content":reply}
  self.add_messages_history(obj)
  await ctx.send(reply)