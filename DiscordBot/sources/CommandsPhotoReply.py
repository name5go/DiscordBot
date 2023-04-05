# -*- coding: Shift-JIS -*-

from discord.ext import commands
from discord.commands import Option

from distutils.util import strtobool

class PhotoReply(commands.Cog):
 def __init__(self, bot):
  self.bot = bot
  self.server_pic_list={}
  

 def get_pic_list(self):
  return self.server_pic_list


 def del_server_id(self,s_id):
  del self.server_pic_list[s_id]


 def is_list_server_id(self,server_id):
  """�T�[�o�[ID��dic_list�ɓo�^����Ă��邩���ׂ�"""
  return server_id in self.server_pic_list


 @commands.slash_command(name='a_�摜�ԐM�@�\��L��', description='�摜�ԐM�@�\��true�ŗL���Bfalse�Ŏ����ꎞ�ۑ��f�[�^�폜')
 async def dic_server_st(self,ctx,
                         status:Option(str, 'true�ŗL���Afalse�ł��̃T�[�o�[�̓o�^�������ׂď��������ɂ���', choices=['true', 'false'])
                         ):
  """����bot�̉摜�ԐM�@�\���T�[�o�[�ŗL���ɂ���"""
  server_id = ctx.guild.id
  server_name = ctx.guild.name
  #bool result =�T�[�o�[ID���A�z�z��ɓo�^����Ă��邩���ׂ�
  result =self.is_list_server_id(server_id)
  status_bool=bool(strtobool(status))
  
  if status_bool:
   if result:
    await ctx.respond('�T�[�o�[��['+str(server_name)+']�ł���bot�͂��łɗL���ł�')
    return
   await ctx.respond('�T�[�o�[��['+str(server_name)+']�ł���bot��L���ɂ��܂�')
   await ctx.send('�����^�u�T�[�o�[ID['+str(server_id)+']�v�I�u�W�F�N�g��[server_list]�ɍ쐬���܂���')
   self.server_pic_list[server_id]={}
  if  not status_bool:
   if not result:
    await ctx.respond('�T�[�o�[��['+str(server_name)+']�ł͊��ɂ���bot�͖����ł�')
    return
   await ctx.respond('�T�[�o�[��['+str(server_name)+']�ł���bot�𖳌��ɂ��܂�')
   await ctx.send('�����^�u�T�[�o�[ID['+str(server_id)+']�v���폜���܂���')
   self.del_server_id(server_id)


#@commands.slash_command(name='a_�摜�ԐM�@�\��L��', description='�摜�ԐM�@�\��true�ŗL���Bfalse�Ŏ����ꎞ�ۑ��f�[�^�폜')
