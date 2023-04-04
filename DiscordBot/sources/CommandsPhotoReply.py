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
  """�T�[�o�[ID��dic_list�ɓo�^����Ă��邩���ׂ�"""
  return server_id in self.server_pic_list

 @commands.slash_command(name='�摜�ԐM�@�\��L��', description='�摜�ԐM�@�\��L��')
 async def dic_server_st(ctx,
                     server_st:Option(str, 'true�ŗL���Afalse�ł��̃T�[�o�[�̓o�^�������ׂď��������ɂ���', choices=['true', 'false']),
                     self
                     ):
  """����bot�̉摜�ԐM�@�\���T�[�o�[�ŗL���ɂ���"""
  server_id = ctx.guild.id
  server_name = ctx.guild.name
  #bool result =�T�[�o�[ID���A�z�z��ɓo�^����Ă��邩���ׂ�
  result =self.is_list_server_id(server_id)



