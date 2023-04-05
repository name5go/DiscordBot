# -*- coding: Shift-JIS -*-

from discord.ext import commands
from discord.commands import Option
from CreateContets import CreateContets
from VoiceVox import Voicevox
import openai
import asyncio
import discord
#環境変数取得用
import os
openai.api_key=os.environ.get('OPENAI_TOKEN')


class ChatAI(commands.Cog):
 def __init__(self, bot):
  self.bot = bot  
  self.creater=CreateContets()
  self.vox=Voicevox()

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
 async def ai_settei(self,ctx):

  await ctx.respond(self.prompt)

 @commands.slash_command(name='a_aiずんだもんと会話', description='AIと会話。限界はわからん')
 async def talk_ai(self,ctx,
                   message:Option(str, 'メッセージ')
                   ):
  await ctx.respond("process...", delete_after=0)
  emb=self.creater.set_embed(ctx,str(ctx.author.name)+"が送信したメッセージ["+message+"]への返信を考えているよ","a","ジージー...ッガガガ...通信中なのだ...","https://i.gyazo.com/f493aff882c43bea1b494cb1a2cf9e97.png")
  sent_message=await ctx.send(embed=emb)
  sent_id=sent_message.id
  try:
   await asyncio.wait_for(self.reply(ctx,message,sent_id), timeout=1000000)
  except asyncio.TimeoutError:
   await ctx.respond("Command timed out!")


 async def reply(self,ctx,message,message_id):
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
  emb=self.creater.set_embed(ctx,str(ctx.author.name)+"さんのメッセージ ["+message+"] へのreplyなのだ！","reply",reply,"https://i.gyazo.com/ea6a503753a58a1b4929a077298d60cb.png")
  message_obj=await ctx.channel.fetch_message(message_id)
  await message_obj.delete()
  await ctx.send(embed=emb)

  if ctx.author.voice is None:
   return
  if ctx.guild.voice_client is None:
   await ctx.author.voice.channel.connect()
  voice=self.vox.speak(text=reply)
  ctx.voice_client.play(discord.PCMAudio(voice))