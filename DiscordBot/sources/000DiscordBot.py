#実装したい処理
"""
文字列に画像urlの登録
urlが画像取得のできるurlか調べる関数は実装しないかも
"""

#終了コマンド用
from pickle import TRUE
import sys

#環境変数取得用
import os
#youtubeくん！
import youtube_dl
#urlのタイトル取得
#import urllib.request
#from bs4 import BeautifulSoup
#環境変数DISCORD_TOKEN取得
#discord_tokenは環境変数に名称は何でもいいけどとりあえずDISCORD_TOKENの名前で追加して取得
TOKEN_D=os.environ.get('DISCORD_TOKEN')
name5go_id=377632130718498826#bot制作者のdiscordアカウントID、強制終了コマンド this_end を実装しているので作成者以外実行できないようにするため

#discord用
import discord
from discord.commands import Option
from discord.ext import pages
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)
#bot = commands.Bot(command_prefix='!')

#連想型配列、ここにサーバー名でdict型配列をまた作りその中に登録する情報を保存していく





useChID=1082307099398242307









#server_music_listの操作時に














    

@bot.slash_command()
async def create_category(ctx: discord.Interaction, category_name:Option(str, '入力した名前のカテゴリで、その内部にVC及び聞き専チャットを自動作成')):
    """通話チャンネルの作成"""

    if ctx.author.avatar is not None:
        avatar_url=ctx.author.avatar.url
    else:
        avatar_url="https://i.gyazo.com/a183e43bafd521a540a754b845d2c501.jpg"

    if is_joined_user(ctx):
        await ctx.respond("コマンド入力者がVCに接続していないとコマンド実行できません")
        return
    channel_id = ctx.channel_id
    if channel_id!=useChID:
        await ctx.respond('チャンネルID'+str(channel_id)+'ではこのコマンドは実行できないよ！カテゴリ追加用VCに参加してそこでもう一度実行してください')
        return
    if category_name in server_call_list:
        em=set_embed_for_call(category_name,avatar_url,"カテゴリー"+category_name+"は既に作成済みだよ！\n別の名称でカテゴリ作成してね\nもしかして"+category_name+"に参加したいの？なら下の***___参加する___***ボタンを押してね",ctx)
        await ctx.respond(embed=em, view=MyView(category_name,ctx.author.id))
        return

    category=await ctx.guild.create_category(name=category_name)
    await category.create_text_channel(name=category_name+"聞き専")
    await category.create_voice_channel(name=category_name+"VC")

    category_dict={'category':category.id,'txt':category.text_channels[0].id,'vc':category.voice_channels[0].id}
    server_call_list[category_name]=category_dict

    await ctx.author.move_to(discord.utils.get(ctx.guild.voice_channels, id=server_call_list[category_name]['vc']))

    em=set_embed_for_call(category_name,avatar_url,ctx.author.mention+"がカテゴリー"+category_name+"を作成してくれたよ！\n参加したい人は下の***___参加する___***ボタンを押してね",ctx)
    await ctx.respond(embed=em, view=MyView(category_name,ctx.author.id)) 

    
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
            if delchid!=useChID and server_call_list[category_name]is not None:
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

from unko import unkoooo

def setup(bot):
   bot.add_cog(unkoooo(bot))
  

print("Hello, World!")
setup(bot)
bot.run(TOKEN_D)