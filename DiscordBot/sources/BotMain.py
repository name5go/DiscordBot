 # -*- coding: Shift-JIS -*-

#bot�N���p
from SetupDiscordBot import SetupBot
#�R�}���h�p�N���X�̃C���|�[�g
from CommandsSystem     import System
from CommandsPhotoReply import PhotoReply
from CommandsVoiceChat  import VoiceChat
from CommandsMusic      import Music
from CommandsChatAI     import ChatAI

class BotMain():
 def __init__(self):
  self.add_commands_list=[]

 def main(self):
  """�G���g���[�|�C���g"""
  setup=SetupBot()
 
#�R�}���h�p�N���X�̃C���|�[�g
  self.add_commands_list.append(System)
  self.add_commands_list.append(PhotoReply)
  self.add_commands_list.append(VoiceChat)
  self.add_commands_list.append(Music)
  self.add_commands_list.append(ChatAI)
  
  for com in self.add_commands_list:
   setup.add(com)
   print('�R�}���h���X�g'+str(com)+"��o�^���܂���")

 #bot�̋N��
  print("bot���N�����܂�")
  setup.run_bot()
 


if __name__ == '__main__':
    bot=BotMain()
    bot.main()
