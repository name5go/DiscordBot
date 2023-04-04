# -*- coding: Shift-JIS -*-

from discord.ext import commands

class VoiceChat(commands.Cog):
 def __init__(self, bot):
  self.bot = bot
  self.server_vc_cate_list={}
  self.server_vc_list={}
