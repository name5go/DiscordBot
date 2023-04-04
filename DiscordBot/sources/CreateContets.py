class CreateContets():
    
 #server_pic_list‚Ö‚Ì‘€ì‚Ébot‚Ì‘—M‚·‚éEmbed‚ğ®”õ‚·‚é
 def set_embed_for_pic(
                      add_word,#“o˜^ˆ—‚Ì•¶š—ñ
                      add_url,#“¯ã‚Ìurl
                      add_description,#“¯ã‚Ì‚¿‚¢‚±‚¢à–¾
                      ):

    #embed‚Ö‚Ì“o˜^ˆ—
    title_color=0x00ff00#green‚ğ“o˜^

    embed=discord.Embed(title=add_word,#ƒ^ƒCƒgƒ‹
                        color=title_color,#‰¡‚ÌF
                        description=add_description,#‚¿‚¢‚±‚¢à–¾
                        url=add_url,#ƒ^ƒCƒgƒ‹•¶š—ñ‚ÉŠi”[‚·‚éurl
                        )

    embed.set_thumbnail(url=add_url)

    return embed

#server_pic_list‚Ö‚Ì‘€ì‚Ébot‚Ì‘—M‚·‚éEmbed‚ğ®”õ‚·‚é
 def set_embed_for_call(
                      add_word,#“o˜^ˆ—‚Ì•¶š—ñ
                      add_url,#“¯ã‚Ìurl
                      add_description,#“¯ã‚Ì‚¿‚¢‚±‚¢à–¾
                      ctx
                      ):

    #embed‚Ö‚Ì“o˜^ˆ—
    title_color=0x00ff00#green‚ğ“o˜^

    channel_id=server_call_list[add_word]["vc"]
    guild_id=ctx.guild.id

    embed=discord.Embed(title="***___"+add_word+"___***",#ƒ^ƒCƒgƒ‹
                        color=title_color,#‰¡‚ÌF
                        description=add_description,#‚¿‚¢‚±‚¢à–¾
                        url=f"https://discord.com/channels/{guild_id}/{channel_id}",#ƒ^ƒCƒgƒ‹•¶š—ñ‚ÉŠi”[‚·‚éurl
                        )

    embed.set_thumbnail(url=add_url)

    return embed


