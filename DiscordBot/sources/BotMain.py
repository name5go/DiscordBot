 # -*- coding: Shift-JIS -*-

#bot�N���p
from SetupDiscordBot import SetupBot
#�R�}���h�p�N���X�̃C���|�[�g
from CommandsSystem import System
from CommandsPhotoReply import PhotoReply
from CommandsVoiceChat import VoiceChat
from CommandsMusic import Music

def main():
 """�G���g���[�|�C���g"""
 setup=SetupBot()
 
#�R�}���h�p�N���X�̃C���|�[�g
 setup.add(System)
 setup.add(PhotoReply)
 setup.add(VoiceChat)
 setup.add(Music)

#bot�̋N��
 print("bot�͐���ɋN���ł��܂���")
 setup.run_bot()
 

if __name__ == '__main__':
    main()
