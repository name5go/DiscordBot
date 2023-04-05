 # -*- coding: Shift-JIS -*-
#discord�p

import discord
from Checker import Checker


class CreateContets():
 def __init__(self):
  self.checker=Checker()


 def get_text_ch_selecter_view(self,ctx,content):
    return SelecterTextChannel(ctx,content)    


 #server_pic_list�ւ̑��쎞��bot�̑��M����Embed�𐮔�����
 def set_embed(self,ctx,
               embed_title,#�^�C�g��
               embed_title_url,#�^�C�g������url
               embed_description,#embed�̐���
               embed_thumbnail_url#�T���l
               ):

    #embed�ւ̓o�^����
    title_color=0x00ff00#green��o�^
    if not self.checker.is_url_string(str(embed_title_url)):
     embed_title_url=ctx.author.avatar.url

    if not self.checker.is_url_string(str(embed_thumbnail_url)):
     embed_thumbnail_url=ctx.author.avatar.url
    
    embed=discord.Embed(title=embed_title,#�^�C�g��
                        color=title_color,#���̐F
                        description=embed_description,#������������
                        url=embed_title_url,#�^�C�g��������Ɋi�[����url
                        )
    embed.set_thumbnail(url=embed_thumbnail_url)
    return embed


#server_pic_list�ւ̑��쎞��bot�̑��M����Embed�𐮔�����
 def set_embed_for_call(self,
                      server_call_list,
                      add_word,#�o�^�������̕�����
                      add_url,#�����url
                      add_description,#����̂�����������
                      ctx
                      ):

    #embed�ւ̓o�^����
    title_color=0x00ff00#green��o�^

    channel_id=server_call_list[add_word]["vc"]
    guild_id=ctx.guild.id

    embed=discord.Embed(title="***___"+add_word+"___***",#�^�C�g��
                        color=title_color,#���̐F
                        description=add_description,#������������
                        url=f"https://discord.com/channels/{guild_id}/{channel_id}",#�^�C�g��������Ɋi�[����url
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
        placeholder = "�e�L�X�g�`�����l�����擾��I��", 
        min_values = 1, 
        max_values = 1, 
        options=
        [ 
            discord.SelectOption
            (
                label="�e�L�X�g�`�����l�����擾",
                value="0",
                description="�e�L�X�g�`�����l�����擾"
            )
        ]
    )
 async def select_callback(self, select, interaction):
  if not self.checker.is_admin_id(interaction.user.id):
   dm=await interaction.user.create_dm()
   await dm.send('bot�쐬�҂���Ȃ��Ǝ��s�ł��Ȃ��ɂ�[��w')
   return
  if select.values[0]=="0" and self.added==0:
   self.added+=1
   for channel in self.ctx.guild.text_channels:
    select.add_option(label=channel.name, value=str(channel.id))
   await interaction.response.edit_message(view=self)
   await self.ctx.send("�e�L�X�g�`�����l���͐���Ɏ擾����܂����B�v���_�E�����������x���e��̑I������I�����Ă�������")
  else:
   if 'discord.embeds.Embed' in str(self.content):
    ch=self.ctx.guild.get_channel(int(select.values[0]))
    await ch.send(embed=self.content)
    await interaction.response.send_message(f"���e���܂���"+str(self.content))
   else:
    await interaction.response.send_message(f"���e���܂���"+str(self.content))


class InviterCall(discord.ui.View):
 def __init__(self,ctx,user_id,vc_id):
  self.ctx=ctx
  self.user_id=user_id
  self.vc_id=vc_id
  super().__init__()
 @discord.ui.button(label="�ʘb�ɎQ��", style=discord.ButtonStyle.primary, emoji=None)
 async def first_button_callback(self, button, interaction):
  member = interaction.user
  if member.voice is None:
   await interaction.response.send_message("�Ɂu�Q������v�{�^������Q������Ȃ��x�J�e�S���ǉ��pVC�ɐڑ����Ă��牟���Ă�")
  else:
   await member.move_to(discord.utils.get(interaction.guild.voice_channels, id=self.vc_id))

