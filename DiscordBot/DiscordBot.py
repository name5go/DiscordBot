#実装したい処理
"""
文字列に画像urlの登録
urlが画像取得のできるurlか調べる関数は実装しないかも
"""

#終了コマンド用
from pickle import TRUE
import sys
#文字列チェック
import re
#環境変数取得用
import os
#youtubeくん！
import youtube_dl
#urlのタイトル取得
#import urllib.request
#from bs4 import BeautifulSoup
#環境変数DISCORD_TOKEN取得
#discord_tokenは環境変数に名称は何でもいいけどとりあえずDISCORD_TOKENの名前で追加して取得
#TOKEN_D=os.environ.get('DISCORD_TOKEN')
TOKEN_D="MTAzMDc4ODg0OTkxNzUwNTY0Nw.GnlIVx.lQpyq-QeSDNWARjBUQFC91X_Uv7fHol-aC7UDU"
name5go_id=377632130718498826#bot制作者のdiscordアカウントID、強制終了コマンド this_end を実装しているので作成者以外実行できないようにするため

#discord用
import discord
from discord.commands import Option
from discord.ext import pages

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)


#連想型配列、ここにサーバー名でdict型配列をまた作りその中に登録する情報を保存していく
server_pic_list={}
server_music_list={}

server_call_list={}

useChID=1082307099398242307

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

#画像および音楽系の関数のためのlist機能が送るためのページネーションを整備
def set_pic_list_pagenator(
                           server_id,
                           ):
    pic_page=(list(server_pic_list[server_id].keys()))
    paginator = pages.Paginator(pages=pic_page)

    return paginator


#server_music_listの操作時に

#チェック系の関数↓
#文字列がurlの書式かどうか調べる
def is_url(url):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    if re.match (pattern, url):
        return True
    else:
        return False

#文字列がサーバー辞書に登録されているか
def is_added_word(server_id,word):
    if word in server_pic_list[server_id]:
        return True
    else:
        return False

#サーバーIDがdic_listに登録されているか調べる
def is_added_server_id(server_id):
    result=server_id in server_pic_list
    if result:
        return True
    else:
        return False

#コマンド実行者ががボイスチャンネルに加入しているか調べる
def is_joined_user(ctx):
    if ctx.author.voice is None:
        return True
    else:
        return False

#BOTがボイスチャンネルに加入しているか調べる
def is_joined_bot(ctx):
    if ctx.guild.voice_client is None:
        return True
    else:
        return False

#どこのurlか調べる
def where_url(url):
    youtube="youtube"
    no="not applied"
    if re.match(youtube, url):
        return youtube
    return no

#class Commands

#bot作成者のアカウントＩＤ以外では動かないようにしたい
@bot.slash_command()
async def this_end(ctx):
    """終了します(bot作成者以外実行不可)"""
    if ctx.author.id==name5go_id:
        await ctx.respond('終了します')
        server_pic_list.clear()
        await bot.close()
        sys.exit()
    if ctx.author.guild_permissions.administrator:
        await ctx.respond('管理者でもbot作成者じゃないと実行できないにょーんw')
        return
    else:
        await ctx.respond('bot作成者じゃないと実行できないにょーんw')    


@bot.slash_command()
async def unko_suru(ctx):
    """うんこします"""
    await ctx.respond('うんこします')
    await ctx.send('ぶりっ')
        
    """
    await ctx.defer()
    test_pages = ['Page-One', 'Page-Two', 'Page-Three', 'Page-Four', 'Page-Five']
    paginator = pages.Paginator(pages=test_pages)
    #await ctx.respond(paginator)
    await paginator.send(ctx)
    """
    """
    if ctx.author.guild_permissions.administrator:
        await ctx.respond('管理者かぁ？おまえがうんこしろよ！！！')
        return
    else:
        await ctx.respond('うんこします')
        await ctx.send('ぶりっ')
        """

#サーバーIDと同名の辞書リストを作成しdict型server_list{}に追加します
#pythonの処理的に重複処理時に既存の内容が多分全部初期化されちゃうかもなので
#trueでもfalseでも一応リストに登録済みかどうか調べて安全を図ってる
@bot.slash_command()
async def dic_server_st(ctx,
                     server_st:Option(str, 'trueで有効、falseでこのサーバーの登録情報をすべて消し無効にする', choices=['true', 'false']),
                     ):#server_st: Option(bool,'このサーバーで有効にするか',choices=['true', 'false'])
    """このbotをサーバーで有効にする"""
    server_id = ctx.guild.id
    server_name = ctx.guild.name
    #bool result =サーバーIDが連想配列に登録されているか調べる
    result=is_added_server_id(server_id)
    #有効化
    if server_st=='true':
        #リスト型にサーバーIDが登録されていなければ処理を実行する
        if result==True:
            await ctx.respond('サーバー名['+str(server_name)+']でこのbotはすでに有効です')
            return
        #登録されていなかったのでサーバーID名で作ったdict型のオブジェクトをリストに追加する
        await ctx.respond('サーバー名['+str(server_name)+']でこのbotを有効にします')
        await ctx.send('dict型「サーバーID['+str(server_id)+']」オブジェクトをdict[server_list]に追加しました')
        server_pic_list[server_id]={}
    #無効化
    elif server_st=='false':
        #リスト型にサーバーIDが登録されていれば処理を実行する
        if result==False:
            await ctx.respond('サーバー名['+str(server_name)+']では既にこのbotは無効です')
            return
        await ctx.respond('サーバー名['+str(server_name)+']でこのbotを無効にします')
        await ctx.send('dict型「サーバーID['+str(server_id)+']」オブジェクトをlistから削除しました')
        del server_pic_list[server_id]
    #discord.pyで作成していた際のtrueとfalse以外の文字列が引数に投げられていた場合の処理
    #pycordに切り替えて引数のオプションの設定もしたので万が一にも無いとは思うが一応残しとく
    else:
        await ctx.respond('コマンドの後にtrueかfalseを入力したら有効無効の切り替えができるよ！')


class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    def __init__(self, name):
        super().__init__()
        self.name = name
    @discord.ui.button(label="参加する", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        member = interaction.user
        if member.voice is None:
            await interaction.response.send_message(self.name+"に「参加する」ボタンから参加するなら一度カテゴリ追加用VCに接続してから押してね") # Send a message when the button is clicked
        else:
            await member.move_to(discord.utils.get(interaction.guild.voice_channels, id=server_call_list[self.name]['vc']))  
    

@bot.slash_command()
async def create_category(ctx: discord.Interaction, category_name:Option(str, '入力した名前のカテゴリで、その内部にVC及び聞き専チャットを自動作成')):

    if ctx.author.avatar is not None:
        avatar_url=ctx.author.avatar.url
    else:
        avatar_url="https://i.gyazo.com/a183e43bafd521a540a754b845d2c501.jpg"

    """通話チャンネルの作成"""
    if is_joined_user(ctx):
        await ctx.respond("コマンド入力者がVCに接続していないとコマンド実行できません")
        return
    channel_id = ctx.channel_id
    if channel_id!=useChID:
        await ctx.respond('チャンネルID'+str(channel_id)+'ではこのコマンドは実行できないよ！カテゴリ追加用VCに参加してそこでもう一度実行してください')
        return
    if category_name in server_call_list:
        em=set_embed_for_call(category_name,avatar_url,"カテゴリー"+category_name+"は既に作成済みだよ！\nそういうわけではないなら別の名称でカテゴリ作成してね\nもしかして"+category_name+"に参加したいなら下の***___参加する___***ボタンを押してね",ctx)
        await ctx.respond(embed=em, view=MyView(category_name))
        return

    category=await ctx.guild.create_category(name=category_name)
    await category.create_text_channel(name=category_name+"聞き専")
    await category.create_voice_channel(name=category_name+"VC")

    category_dict={'category':category.id,'txt':category.text_channels[0].id,'vc':category.voice_channels[0].id}
    server_call_list[category_name]=category_dict

    await ctx.author.move_to(discord.utils.get(ctx.guild.voice_channels, id=server_call_list[category_name]['vc']))

    em=set_embed_for_call(category_name,avatar_url,ctx.author.mention+"がカテゴリー"+category_name+"を作成してくれたよ！\n参加したい人は下の***___参加する___***ボタンを押してね",ctx)
    await ctx.respond(embed=em, view=MyView(category_name)) 

    
@bot.slash_command()
async def delete_category(ctx: discord.Interaction, category_name:Option(str, '入力した名前のカテゴリで')):
    category=await ctx.guild.create_category(name=category_name)
    #await category.delete()
    for channel in category.channels:
      await channel.delete()
    # カテゴリーを削除する
    await category.delete()
    return

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is not None:
        category_name=before.channel.category.name
        if len(before.channel.members) ==0 and category_name!=bot.get_channel(useChID).category.name:
            delchid=server_call_list[category_name]["vc"]
            if delchid!=useChID:
                await bot.get_channel(useChID).send(category_name+"カテゴリは誰もいなくなったから削除するよ")
                await bot.get_channel(server_call_list[category_name]["vc"]).delete()
                await bot.get_channel(server_call_list[category_name]["txt"]).delete()
                await bot.get_channel(server_call_list[category_name]["category"]).delete()
                del server_call_list[category_name]

    return

#画像を文字列に登録。引数は単語、画像url
@bot.slash_command()
async def dic_add(ctx,
                  word:Option(str,'好きな文字列'),
                  url:Option(str,'文字列に登録する画像URL'),
                  ):
    """画像を文字列に登録。引数は単語、画像url"""
    server_id = ctx.guild.id
    server_name = ctx.guild.name
    result=is_added_server_id(server_id)
    if result==False:
        await ctx.respond('サーバー名['+str(server_name)+']ではこのbotは無効です。コマンド[/server_st]でまずはこのサーバーを有効化しましょう')
        return
    if is_url(url)==False:
        await ctx.respond(url+'はurlじゃなくねぇ？画像urlを入力してもっかい試してみて')
        return
    if is_added_word(server_id,word):
        await ctx.respond(word+'にはすでに別の文字列が登録されてるくさいね[/dic_del]コマンドに'+word+'を入力して文字列'+word+'を消してからもう一度コマンド実行したらいけるかも')
        return
    #連想配列server_list内の連想配列server_idに連想配列 l {キーword:値url}を追加する
    server_pic_list[server_id][word]=url
    #送信コメント
    em=set_embed_for_pic(word,url,"サーバー辞書に文字列"+word+"の情報を保存しました")
    await ctx.respond(embed=em)
    return


#文字列削除コマンド
@bot.slash_command()
async def dic_del(ctx,
                  word:Option(str,'削除したい文字列'),
                  ):
    """文字列削除コマンド"""
    server_id = ctx.guild.id
    server_name = ctx.guild.name
    result=is_added_server_id(server_id)
    if result==False:
        await ctx.respond('サーバー名['+str(server_name)+']ではこのbotは無効です。コマンド[/server_st]でまずはこのサーバーを有効化しましょう')
        return
    if is_added_word(server_id,word):
        em=set_embed_for_pic(word,server_pic_list[server_id].get(word),"サーバー辞書から文字列"+word+"の情報を削除しました")
        await ctx.respond(embed=em)
        del server_pic_list[server_id][word]
        return
    await ctx.respond('消そうにも'+word+'がないっす！w')


#画像の貼り付けコマンド
@bot.slash_command()
async def dic_pst(ctx,word):
    """画像の貼り付けコマンド"""
    server_id = ctx.guild.id
    server_name = ctx.guild.name
    result=is_added_server_id(server_id)
    if result==False:
        await ctx.respond('サーバー名['+str(server_name)+']ではこのbotは無効です。コマンド[/server_st]でまずはこのサーバーを有効化しましょう')
        return
    if is_added_word(server_id,word):
        await ctx.respond(server_pic_list[server_id].get(word))
        return
    await ctx.respond(word+'には何も登録されてないよ！[!dic_add]で画像urlを登録してきてね')


#登録された単語のリストを送信する
@bot.slash_command()
async def dic_list(ctx):
    """現在登録されている単語のリストを送信する"""
    server_id = ctx.guild.id
    server_name = ctx.guild.name
    result=is_added_server_id(server_id)
    if result==False:
        await ctx.respond('サーバー名['+str(server_name)+']ではこのbotは無効です。コマンド[/server_st]でまずはこのサーバーを有効化しましょう')
        return
    #pgs=set_pic_list_pagenator(server_id)
    pic_list_len=len(server_pic_list[server_id])
    if pic_list_len==0:
        await ctx.respond('サーバー名['+str(server_name)+']のライブラリにはなにも登録されていません。コマンド[/dic_add]で辞書に追加しましょう')
        return
    await ctx.defer()
    pic_page=(list(server_pic_list[server_id].keys()))
    paginator = pages.Paginator(pages=pic_page)
    await paginator.send(ctx)

@bot.slash_command()
async def test_pages(ctx):
    await ctx.defer()
    test_pages = ['Page-One', 'Page-Two', 'Page-Three', 'Page-Four', 'Page-Five']
    paginator = pages.Paginator(pages=test_pages)
    await paginator.send(ctx)

#メッセージに反応して登録された画像で返す
@bot.listen('on_message')  # かっこが必要
async def dic_respond_pic(message):
    server_id = message.guild.id
    result=is_added_server_id(server_id)
    if result==False:
        return
    if message.author == bot.user:
        return
    word=message.content
    #配列に文字列が登録されていればその文字列に登録されたurlでリプライする
    if is_added_word(server_id,word):
       #await ctx.channel.send("<@{}> ".format(message.author.id))
        await message.reply(server_pic_list[server_id].get(word))
       #await message.delete()
        return



"""
ここから音楽再生機能用のコマンドとか関数とか
"""

#VCに加入
@bot.slash_command()
async def dc_join(ctx):
    """ボイスチャンネルに接続"""
    if is_joined_user(ctx):
        await ctx.respond("コマンド入力者がVCに接続してないとこのコマンド実行できんよぉ～～")
        return
    if is_joined_bot(ctx):
        #ボイスチャンネルに接続する
        server_id = ctx.guild.id
        server_name = ctx.guild.name
        server_music_list[server_id]=[] #list型のプレイリストを作成
        await ctx.author.voice.channel.connect()
        await ctx.respond("VCに接続します")
        await ctx.send('サーバー名['+str(server_name)+']でlist型['+str(server_id)+']プレイリストを作成しました')
        return
    await ctx.respond("既にVCに加入してるよ～？")       

#切断
@bot.slash_command()
async def dc_leave(ctx):
    """ボイスチャンネルから切断"""
    if is_joined_bot(ctx):
        await ctx.respond("このbotはまだVCに接続されていません")
        return
    # 切断
    server_id = ctx.guild.id
    server_name = ctx.guild.name

    del server_music_list[server_id]#list型のプレイリストを削除
    await ctx.voice_client.disconnect()
    await ctx.respond("切断します")
    await ctx.send('サーバー名['+str(server_name)+']のlist型['+str(server_id)+']プレイリストを削除しました')


#添付された曲を再生する
@bot.slash_command()
async def dc_play(ctx,
                  url:Option(str,'プレイリストに登録する音楽URL'),
                  ):
    """プレイリストに音楽を追加する"""
    if is_joined_bot(ctx):
        await ctx.respond("このbotはまだVCに接続されていません")
        return
    if is_url(url)==False:
        await ctx.respond(url+'はurlじゃなくねぇ？画像urlを入力してもっかい試してみて')
        return
    server_id = ctx.guild.id
    server_name = ctx.guild.name
    server_music_list[server_id].append(url) 
    await ctx.respond('> ```'+'サーバー名['+str(server_name)+']のlist型['+str(server_id)+']プレイリストに'+url+' を追加しました'+'```')
    if server_music_list[server_id][0]==url:
        await ctx.send('```'+url+'の再生を開始します'+'```')
        #youtubeとnicoに対応させるつもりなのでurllの種類によって処理を分ける
    if where_url(url)=="youtube":
        await ctx.send('```'+url+'はようつべだね'+'```')
        return 
    else:
        await ctx.send('```'+url+'はようつべじゃないね'+'```')
        return 
        
#bot起動
bot.run(TOKEN_D)
