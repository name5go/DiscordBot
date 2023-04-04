# -*- coding: Shift-JIS -*-

from discord.ext import commands

class Music(commands.Cog):
 def __init__(self, bot):
  self.bot = bot
  self.server_music_list={}