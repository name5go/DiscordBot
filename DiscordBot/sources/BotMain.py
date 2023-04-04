 # -*- coding: Shift-JIS -*-

#bot起動用
from SetupDiscordBot import SetupBot
#コマンド用クラスのインポート
from CommandsSystem import System
from CommandsPhotoReply import PhotoReply
from CommandsVoiceChat import VoiceChat
from CommandsMusic import Music

def main():
 """エントリーポイント"""
 setup=SetupBot()
 
#コマンド用クラスのインポート
 setup.add(System)
 setup.add(PhotoReply)
 setup.add(VoiceChat)
 setup.add(Music)

#botの起動
 print("botは正常に起動できました")
 setup.run_bot()
 

if __name__ == '__main__':
    main()
