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

 @commands.slash_command(name='���񂱂��܂�', description='�Ԃ��')
 async def unko_suru(self,ctx):
   """���񂱂��܂�"""
   await ctx.respond('���񂱂��܂�')
   await ctx.send('�Ԃ��')

 @commands.slash_command(name='�_bot_close', description='�I�����܂��Bbot�쐬�҈ȊO���s�s��')
 async def this_end(self,ctx):
  """�I��"""
  if Checker.is_admin_id(ctx.author.id):
   print("bot�͐���ɏI�����܂���")
   self.clear_lists()
   await ctx.respond('�I�����܂�')
   await self.bot.close()
   sys.exit()
  await ctx.respond('bot�쐬�҂���Ȃ��Ǝ��s�ł��Ȃ��ɂ�[��w')
   
 @commands.Cog.listener('on_message')
 async def on_message(self, message):
  """���b�Z�[�W�ɔ���"""
  if message.content == '����':
   await message.channel.send('����ko')
