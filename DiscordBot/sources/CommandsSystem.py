 # -*- coding: Shift-JIS -*-

import sys
import discord
from discord.ext import commands
from Checker import Checker
from discord.commands import Option
from CreateContets import CreateContets
from SetupDiscordBot import SetupBot
from VoiceVox import Voicevox
from CtrlVoiceChat import VoiceChat

class System(commands.Cog):
 all_text_ch_id=[str(0)]
 def __init__(self, bot):
  self.bot = bot
  self.creater=CreateContets()
  self.checker=Checker()
  self.vox=Voicevox()
  self.vc=VoiceChat(discord)

 @commands.slash_command(name='z_bot_close', description='�I�����܂��Bbot�쐬�҈ȊO���s�s��')
 async def this_end(self,ctx):
  """�I��"""
  if not self.checker.is_admin_id(ctx.author.id):
   dm=await ctx.author.create_dm()
   await dm.send('bot�쐬�҂���Ȃ��Ǝ��s�ł��Ȃ��ɂ�[��w')
   return

  print("bot�͐���ɏI�����܂���")
  await ctx.respond('�I�����܂�')
  await self.bot.close()
  sys.exit()
  

 @commands.slash_command(name='z_���񂱂��܂�', description='�Ԃ��')
 async def unko_suru(self,ctx):
   """���񂱂��܂�"""
   r=self.vc.join_vc(ctx)
   await ctx.respond(str(r))
   await ctx.respond('���񂱂��܂�', delete_after=0)
   await ctx.send('�Ԃ��')
   sent=await ctx.channel.send(str(ctx.guild.get_channel(1082307099398242306)))
   iddd=sent.id
   message_obj=await ctx.channel.fetch_message(iddd)
   await message_obj.delete()
   dm=await ctx.author.create_dm()
   await dm.send('�Ԃ��')
   
   user_id={int(ctx.author.id):5}
   user_id_list={}
   user_id_list.update(user_id)
   await ctx.send(str(user_id_list))
   
   
   """
   if ctx.author.voice is None:
    return
   if ctx.guild.voice_client is None:
    await ctx.author.voice.channel.connect()
   """
   
   if r==True:
    await ctx.send(str(ctx.author.voice.channel.id)+str(ctx.author.voice.channel.id))
    voice=self.vox.speak(text='���񂱂��܂�')
    ctx.voice_client.play(discord.FFmpegPCMAudio(voice))

  
   #source=discord.FFmpegPCMAudio(voice)

   


 @commands.slash_command(name='z_embed', description='embed���쐬')
 async def send_embed(self,ctx,
                      title:Option(str, '�^�C�g��'),
                      title_url:Option(str, '�^�C�g��url'),
                      description:Option(str, '����'),
                      thumbnail:Option(str, '�T���l'),
                      ):
   if not self.checker.is_admin_id(ctx.author.id):
    dm=await ctx.author.create_dm()
    await dm.send('bot�쐬�҂���Ȃ��Ǝ��s�ł��Ȃ��ɂ�[��w')
    return
   embed= self.creater.set_embed(ctx,title,title_url,description,thumbnail)
   selecter=self.creater.get_text_ch_selecter_view(ctx,embed)
   await ctx.respond("���e��̃e�L�X�g�`�����l����I�����邽�߁A�܂��̓`�����l�����擾��I�����Ă�������",view=selecter)
   

 @commands.Cog.listener('on_message')
 async def on_message(self, message):
  """���b�Z�[�W�ɔ���"""
  if message.content == '����':
   await message.channel.send('����ko')
   bot=SetupBot()
   bot=bot.get_bot()
   await message.channel.send(str(bot.get_channel(1082307099398242306)))
