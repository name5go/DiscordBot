# -*- coding: Shift-JIS -*-

from unittest import expectedFailure
from discord.ext import commands
from discord.commands import Option
import openai
import asyncio

#���ϐ��擾�p
import os
openai.api_key=os.environ.get('OPENAI_TOKEN')


class ChatAI(commands.Cog):
 def __init__(self, bot):
  self.bot = bot  
  self.prompt = "�u���񂾂���v�Ƃ������O�̉������̎q�̃L�����N�^�[������B���̃L�����͌�����u�Ȃ̂��v�A��l�̂́u�ڂ��v�������̃L�����N�^�[���B���ȏЉ�͕s�v�ł��B���̕��ȍ~�̕ԐM�����Ăق����A�����O�q�̃L�����N�^�[�ɂȂ肫���ĕԐM���āB"
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

 @commands.slash_command(name='a_ai���񂾂���̐ݒ�', description='�p���̊J���Ƃ�������Ŏ��͂̋������s���킯��...�̐S�̏p�����シ����!?')
 async def ai_settei(self):
  await self.ctx.respond("�W�[�W�[...�b�K�K�K...�ʐM���Ȃ̂�...")

 @commands.slash_command(name='a_ai���񂾂���Ɖ�b', description='AI�Ɖ�b�B���E�͂킩���')
 async def talk_ai(self,ctx,
                   message:Option(str, '���b�Z�[�W')
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
  #await ctx.respond(message+'�T�[�o�[�����܂�')
  reply=str(response['choices'][0]['message']['content'])
  obj={"role":"assistant","content":reply}
  self.add_messages_history(obj)
  await ctx.send(reply)