class CreateContets():
    
 #server_pic_listへの操作時にbotの送信するEmbedを整備する
 def set_embed_for_pic(
                      add_word,#登録処理時の文字列
                      add_url,#同上のurl
                      add_description,#同上のちいこい説明
                      ):

    #embedへの登録処理
    title_color=0x00ff00#greenを登録

    embed=discord.Embed(title=add_word,#タイトル
                        color=title_color,#横の色
                        description=add_description,#ちいこい説明
                        url=add_url,#タイトル文字列に格納するurl
                        )

    embed.set_thumbnail(url=add_url)

    return embed

#server_pic_listへの操作時にbotの送信するEmbedを整備する
 def set_embed_for_call(
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


