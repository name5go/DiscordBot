# -*- coding: Shift-JIS -*-

from discord.ext import commands
from discord.commands import Option
import openai

#���ϐ��擾�p
import os

class ChatAI(commands.Cog):
 def __init__(self, bot):
  self.bot = bot
  self.openai.api_key=os.environ.get('OPENAI_TOKEN')
  self.messages_history=[{
                   "role": "system",
                   "content": "�u���񂾂���v�Ƃ������O�̉������̎q�̃L�����N�^�[������B���̃L�����͌�����u�Ȃ̂��v�A��l�̂́u�ڂ��v�������̃L�����N�^�[���B���ȏЉ�͕s�v�ł��B���̕��ȍ~�̕ԐM�����Ăق����A�����O�q�̃L�����N�^�[�ɂȂ肫���ĕԐM���āB"
                    },],
 @commands.slash_command(name='a_ai�Ɖ�b', description='AI�Ɖ�b�B���E�͂킩���')
 async def talk_ai(self,ctx,
                   message:Option(str, '���b�Z�[�W')
                   ):
  self.messages_history.apeend({"role":"user","content":message})
  response = openai.ChatCompletion.create(
                                           model="gpt-3.5-turbo",
                                           messsages=self.messages_history,
                                           )
  #await ctx.respond(message+'�T�[�o�[�����܂�')
  reply=str(response[0]["message"]["content"].strip())
  self.messages_history.apeend({"role":"assistant","content":reply})
  await ctx.respond(reply)