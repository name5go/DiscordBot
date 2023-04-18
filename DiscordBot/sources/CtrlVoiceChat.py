 # -*- coding: Shift-JIS -*-

from VoiceVox import Voicevox

class VoiceChat():
 def __init__(self,discord):
  self.discord=discord
  self.vox=Voicevox()
  user_id=-1
  self.user_id_list={user_id:5}


 def join_vc(self,ctx):
  if ctx.author.voice is None:
   return False

  if ctx.guild.voice_client is None:
   self.join(ctx)

  a=ctx.author.voice.channel.id
  b=ctx.guild.voice_client.channel.id
  if a==b:
   return True

  return False

 async def join(self,ctx):
  await ctx.author.voice.channel.connect()

 async def change_speaker(self,ctx,speker):
  user_id={int(ctx.author.id):speker}
  self.user_id_list.update(user_id)

 async def speak_text(self,ctx,text):
   a=1
 #async def speak_vc(self,ctx)

