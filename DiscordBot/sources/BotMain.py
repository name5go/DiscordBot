 # -*- coding: Shift-JIS -*-

#bot起動用
from SetupDiscordBot import SetupBot
#コマンド用クラスのインポート
from CommandsSystem     import System
from CommandsPhotoReply import PhotoReply
from CommandsVoiceChat  import VoiceChat
from CommandsMusic      import Music
from CommandsChatAI     import ChatAI

class BotMain():
 def __init__(self):
  self.add_commands_list=[]

 def main(self):
  """エントリーポイント"""
  setup=SetupBot()
 
#コマンド用クラスのインポート
  self.add_commands_list.append(System)
  self.add_commands_list.append(PhotoReply)
  self.add_commands_list.append(VoiceChat)
  self.add_commands_list.append(Music)
  self.add_commands_list.append(ChatAI)
  
  for com in self.add_commands_list:
   setup.add(com)
   print('コマンドリスト'+str(com)+"を登録しました")

 #botの起動
  print("botを起動します")
  setup.run_bot()
 


if __name__ == '__main__':
    bot=BotMain()
    bot.main()
