class CreateContets():
    
 #server_pic_list�ւ̑��쎞��bot�̑��M����Embed�𐮔�����
 def set_embed_for_pic(
                      add_word,#�o�^�������̕�����
                      add_url,#�����url
                      add_description,#����̂�����������
                      ):

    #embed�ւ̓o�^����
    title_color=0x00ff00#green��o�^

    embed=discord.Embed(title=add_word,#�^�C�g��
                        color=title_color,#���̐F
                        description=add_description,#������������
                        url=add_url,#�^�C�g��������Ɋi�[����url
                        )

    embed.set_thumbnail(url=add_url)

    return embed

#server_pic_list�ւ̑��쎞��bot�̑��M����Embed�𐮔�����
 def set_embed_for_call(
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


