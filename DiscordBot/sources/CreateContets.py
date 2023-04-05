 # -*- coding: Shift-JIS -*-
#discord用

import discord
from Checker import Checker


class CreateContets():
 def __init__(self):
  self.checker=Checker()


 def get_text_ch_selecter_view(self,ctx,content):
    return SelecterTextChannel(ctx,content)    


 #server_pic_listへの操作時にbotの送信するEmbedを整備する
 def set_embed(self,ctx,
               embed_title,#タイトル
               embed_title_url,#タイトル内蔵url
               embed_description,#embedの説明
               embed_thumbnail_url#サムネ
               ):

    #embedへの登録処理
    title_color=0x00ff00#greenを登録
    if not self.checker.is_url_string(str(embed_title_url)):
     embed_title_url=ctx.author.avatar.url

    if not self.checker.is_url_string(str(embed_thumbnail_url)):
     embed_thumbnail_url=ctx.author.avatar.url
    
    embed=discord.Embed(title=embed_title,#タイトル
                        color=title_color,#横の色
                        description=embed_description,#ちいこい説明
                        url=embed_title_url,#タイトル文字列に格納するurl
                        )
    embed.set_thumbnail(url=embed_thumbnail_url)
    return embed


#server_pic_listへの操作時にbotの送信するEmbedを整備する
 def set_embed_for_call(self,
                      server_call_list,
                      add_word,#登録処理時の文字列
                      add_url,#同上のurl
                      add_description,#同上のちいこい説明
                      ctx
                      ):

    #embedへの登録処理
    title_color=0x00ff00#greenを登録

    channel_id=server_call_list[add_word]["vc"]
    guild_id=ctx.guild.id

    embed=discord.Embed(title="***___"+add_word+"___***",#タイトル
                        color=title_color,#横の色
                        description=add_description,#ちいこい説明
                        url=f"https://discord.com/channels/{guild_id}/{channel_id}",#タイトル文字列に格納するurl
                        )
    embed.set_thumbnail(url=add_url)
    return embed


class SelecterTextChannel(discord.ui.View):
 def __init__(self,ctx, content):
  self.ctx=ctx
  self.content=content
  self.added=0;
  self.checker=Checker()
  super().__init__()
  

 @discord.ui.select( 
        placeholder = "テキストチャンネルを取得を選択", 
        min_values = 1, 
        max_values = 1, 
        options=
        [ 
            discord.SelectOption
            (
                label="テキストチャンネルを取得",
                value="0",
                description="テキストチャンネルを取得"
            )
        ]
    )
 async def select_callback(self, select, interaction):
  if not self.checker.is_admin_id(interaction.user.id):
   dm=await interaction.user.create_dm()
   await dm.send('bot作成者じゃないと実行できないにょーんw')
   return
  if select.values[0]=="0" and self.added==0:
   self.added+=1
   for channel in self.ctx.guild.text_channels:
    select.add_option(label=channel.name, value=str(channel.id))
   await interaction.response.edit_message(view=self)
   await self.ctx.send("テキストチャンネルは正常に取得されました。プルダウンからもう一度投稿先の選択肢を選択してください")
  else:
   if 'discord.embeds.Embed' in str(self.content):
    ch=self.ctx.guild.get_channel(int(select.values[0]))
    await ch.send(embed=self.content)
    await interaction.response.send_message(f"投稿しました"+str(self.content))
   else:
    await interaction.response.send_message(f"投稿しました"+str(self.content))


class InviterCall(discord.ui.View):
 def __init__(self,ctx,user_id,vc_id):
  self.ctx=ctx
  self.user_id=user_id
  self.vc_id=vc_id
  super().__init__()
 @discord.ui.button(label="通話に参加", style=discord.ButtonStyle.primary, emoji=None)
 async def first_button_callback(self, button, interaction):
  member = interaction.user
  if member.voice is None:
   await interaction.response.send_message("に「参加する」ボタンから参加するなら一度カテゴリ追加用VCに接続してから押してね")
  else:
   await member.move_to(discord.utils.get(interaction.guild.voice_channels, id=self.vc_id))

